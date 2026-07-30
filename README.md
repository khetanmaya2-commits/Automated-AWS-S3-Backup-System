# 🚀 Automated Backup System with GitHub Actions CI

A Python automation project that creates compressed `.tar.gz` backups of a directory and validates the backup process automatically using GitHub Actions CI.

## ✨ Features

- 📂 Automated directory backup
- 🗜️ Creates compressed `.tar.gz` archives
- ⚙️ GitHub Actions CI pipeline
- 📦 Uploads backup to AWS S#
- 🐍 Built using Python

## 🛠️ Tech Stack

- Python
- Git & GitHub
- GitHub Actions
- YAML
- AWS S3
- Boto3

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

## 🏗️ Architecture

```text
        Developer
            │
            ▼
      Push Code to GitHub
            │
            ▼
     GitHub Actions CI
            │
    ┌───────┼────────┐
    ▼       ▼        ▼
 Checkout  Setup   Configure AWS
   Code    Python      CLI
                     │
                     ▼
           Create Backup & Upload To AWS S3
                     │
                     ▼
              Pipeline Success ✅
```

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

## 🚀 Future Enhancements

- Delete old backups automatically
- Add logging
- Schedule daily backups using GitHub Actions
