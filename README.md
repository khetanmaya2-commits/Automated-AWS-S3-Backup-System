# 🚀 Automated Backup System with GitHub Actions CI

A Python automation project that creates compressed `.tar.gz` backups of a directory and validates the backup process automatically using GitHub Actions CI.

## 🚀 Features

* Automated backup creation using Python
* Compresses files into a `.tar.gz` archive
* Uploads backups securely to Amazon S3
* Uses AWS IAM credentials with least-privilege access
* GitHub Actions automatically runs the backup workflow
* Amazon S3 ObjectCreated event automatically triggers AWS Lambda
* AWS Lambda verifies uploaded backup files
* Retrieves backup metadata using the Amazon S3 HeadObject API
* CloudWatch Logs records every Lambda execution for monitoring and debugging
* Event-driven serverless architecture
* Secure cloud storage for backup files
* Easy to extend with email notifications or backup validation


## 🛠️ Technologies Used

* Python
* AWS S3
* AWS Lambda
* AWS IAM
* Amazon CloudWatch
* GitHub Actions
* Git
* GitHub
* Boto3


## 📂 Project Structure

```text
backup-project/
│
├── backups.py
├── s3_backup.py
├── sample_data/
├── backup/
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md

```

## ⚙️ Workflow

1. Developer pushes code to GitHub.
2. GitHub Actions automatically starts the workflow.
3. The Python backup script compresses the target files into a `.tar.gz` archive.
4. The backup archive is uploaded to Amazon S3.
5. Amazon S3 generates an **ObjectCreated** event.
6. The event automatically triggers an AWS Lambda function.
7. Lambda verifies that the backup file was uploaded successfully.
8. Lambda retrieves metadata using the Amazon S3 HeadObject API.
9. CloudWatch Logs records the execution details for monitoring and troubleshooting.


                Developer
                    │
            git push origin main
                    │
                    ▼
             GitHub Repository
                    │
                    ▼
             GitHub Actions CI
                    │
                    ▼
        Python Automated Backup Script
                    │
          Creates .tar.gz Backup
                    │
                    ▼
               Amazon S3 Bucket
                    │
        ObjectCreated Event Trigger
                    ▼
              AWS Lambda Function
                    │
        Verify Uploaded Backup File
                    │
        Retrieve Object Metadata
                    │
                    ▼
          Amazon CloudWatch Logs

## ▶️ Running Locally

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd backup-project
```

Run the backup script

```bash
python s3_backup.py
```

The backup archive will be created and uploaded to the AWS S3 Bucket 

---

## 📚 Learning Outcomes

Through this project, I gained practical experience with:

* Python automation
* AWS Identity and Access Management (IAM)
* Amazon S3 object storage
* Event-driven serverless architecture
* AWS Lambda functions
* Amazon CloudWatch monitoring and logging
* GitHub Actions CI automation
* AWS SDK for Python (Boto3)
* Secure cloud authentication
* Backup automation and cloud storage best practices

## 🚀 Future Enhancements

- Delete old backups automatically
- Add logging
- Schedule daily backups using GitHub Actions
