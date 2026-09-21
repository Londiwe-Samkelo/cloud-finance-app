import boto3
from botocore.exceptions import ClientError

#Initialize S3 client
s3 = boto3.client('s3')

BUCKET_NAME = 'sam-finance-tracker-bucket'
LOCAL_FILE = '../personal-finance-tracker/data/transactions.csv'
S3_FILE_NAME = 'transactions.csv'

def upload_file_to_s3():
    """Upload the transactions CSV to an S3 bucket"""
    print(f"Uploading {LOCAL_FILE} to S3 bucket '{BUCKET_NAME}'...")
    try:
        s3.upload_file(LOCAL_FILE, BUCKET_NAME, S3_FILE_NAME)
        print("Upload successful!")

    except ClientError as e:
        print(f"Upload failed: {e}")


def download_file_from_s3():
    """Download the transactions CSV from S3"""
    print(f"Downloading {S3_FILE_NAME} from S3 bucket '{BUCKET_NAME}'...")
    try:
        s3.download_file(BUCKET_NAME, S3_FILE_NAME, 'downloaded_transactions.csv')
        print("Download successful!")
    except ClientError as e:
        print(f"Download failed: {e}")


def list_bucket_contents():
    """List all files currently in the S3 bucket"""
    print(f"Listing contents of bucket '{BUCKET_NAME}'...")
    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME)
        if 'Contents' in response:
            for obj in response['Contents']:
                print(f" - {obj['Key']} ({obj['Size']} bytes)")
        else:
            print("Bucket is empty.")
    except ClientError as e:
        print(f"Could not list bucket contents: {e}")

if __name__ == "__main__":
    upload_file_to_s3()
    list_bucket_contents()
    download_file_from_s3()