"""

This python file takes backup from local to AWS S3
boto3 -> used to do AWS tasks using python

"""
import boto3, os 

from backups import backup_files

s3= boto3.resource("s3")

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def bucket_exists(bucket_name):
    for bucket in s3.buckets.all():
        if bucket.name == bucket_name:
            return True        
    return False    

def create_bucket(s3, bucket_name, region):
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
        'LocationConstraint': region,
    },)
    print("bucket created successfully")    


def upload_backup(s3,file_name, bucket_name, key_name):
    if not os.path.exists(file_name):
        print("Backup file not found")
        return
    
    data=open(file_name,'rb') #binary me read hoga
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)

    print("backup uploaded successfully")
    print("Successful")


bucket_name="maya-python-123"
region="ap-south-1"
source= "sample_data"
destination= "backup"
backup_path= backup_files(source,destination)
key_name= os.path.basename(backup_path)

if bucket_exists(bucket_name):
    print("Bucket alredy exists.")
else:
    create_bucket(s3,bucket_name, region)



show_buckets(s3)
upload_backup(s3,backup_path,bucket_name,key_name)

