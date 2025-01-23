"""
Amazon S3 (Simple Storage Service):

    Amazon S3 is a scalable, highly durable, and secure object storage service provided by AWS. It is designed to store and retrieve any amount of data from anywhere on the web, making it ideal for a wide range of use cases, including web applications, backups, and big data analytics.

Example with Python Code:
"""

import boto3
from botocore.exceptions import NoCredentialsError

# AWS S3 Configuration
AWS_ACCESS_KEY_ID = "your-access-key-id"
AWS_SECRET_ACCESS_KEY = "your-secret-access-key"
AWS_REGION = "your-region"  # e.g., 'us-west-2'
BUCKET_NAME = "your-bucket-name"

# Initialize the S3 client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)


# Upload File to S3
def upload_file_to_s3(file_path, s3_key):
    """
    Upload a file to an S3 bucket.
    :param file_path: Local file path to upload.
    :param s3_key: The key (path) for the file in S3.
    """
    try:
        s3_client.upload_file(file_path, BUCKET_NAME, s3_key)
        print(f"File uploaded successfully to {BUCKET_NAME}/{s3_key}")
    except FileNotFoundError:
        print("The file was not found.")
    except NoCredentialsError:
        print("AWS credentials not available.")
    except Exception as e:
        print(f"Error occurred: {e}")


# Fetch File from S3
def fetch_file_from_s3(s3_key, download_path):
    """
    Fetch a file from S3 and save it locally.
    :param s3_key: The key (path) of the file in S3.
    :param download_path: Local path where the file should be saved.
    """
    try:
        s3_client.download_file(BUCKET_NAME, s3_key, download_path)
        print(f"File downloaded successfully to {download_path}")
    except NoCredentialsError:
        print("AWS credentials not available.")
    except Exception as e:
        print(f"Error occurred: {e}")


# Example Usage
if __name__ == "__main__":
    # Upload a file
    local_file_path = "path/to/your/local/file.txt"
    s3_key = "uploads/file.txt"
    upload_file_to_s3(local_file_path, s3_key)

    # Fetch the same file
    download_file_path = "path/to/downloaded/file.txt"
    fetch_file_from_s3(s3_key, download_file_path)


# Example with DRF

# Integration with DRF
# Views for Upload and Fetch

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import boto3
from botocore.exceptions import NoCredentialsError


class S3FileUploadView(APIView):
    def post(self, request):
        file = request.FILES.get("file")
        if not file:
            return Response(
                {"error": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST
            )

        s3_client = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION,
        )
        s3_key = f"uploads/{file.name}"

        try:
            s3_client.upload_fileobj(file, settings.BUCKET_NAME, s3_key)
            return Response(
                {"message": f"File uploaded to {settings.BUCKET_NAME}/{s3_key}"}
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class S3FileFetchView(APIView):
    def get(self, request, s3_key):
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION,
        )

        download_path = f"/tmp/{s3_key.split('/')[-1]}"
        try:
            s3_client.download_file(settings.BUCKET_NAME, s3_key, download_path)
            with open(download_path, "rb") as file:
                return Response(file.read(), content_type="application/octet-stream")
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
