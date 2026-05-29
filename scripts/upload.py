import boto3
import os
import logging

logging.basicConfig(level=logging.INFO)

FILE_PATH = os.path.join("data", "forecast.csv")
BUCKET_NAME = os.getenv("BUCKET_NAME")
S3_KEY = "forecast/forecast.csv"


def upload_to_s3():
    try:
        s3 = boto3.client('s3')
        s3.upload_file(FILE_PATH, BUCKET_NAME, S3_KEY)

        logging.info("Upload to S3 successful")

    except Exception as e:
        logging.error(f"Upload failed: {e}")
        raise


if __name__ == "__main__":
    upload_to_s3()
