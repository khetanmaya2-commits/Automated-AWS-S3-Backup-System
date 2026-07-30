import boto3

s3= boto3.client('s3')

def lambda_handler(event, context):

    bucket_name = event['Records'][0]['s3']['bucket']['name']

    file_name = event['Records'][0]['s3']['object']['key']

    response = s3.head_object(Bucket=bucket_name, Key=file_name)

    file_size = response['ContentLength']

    print("========BACKUP VERIFICATION=========")
    print(f"Bucket: {bucket_name}")
    print(f"File: {file_name}")
    print(f"Size: {file_size} bytes")

    if file_name.endswith(".tar.gz"):
        print("Status: Valid Backup")

    else:
        print("Status: Invalid Backup")
    return {
        'statusCode': 200,
        'body': "Backup verification completed"
    }
