import boto3
import os
from botocore.exceptions import NoCredentialsError
from loguru import logger
from typing import List

class AWS:
    @staticmethod
    def send_image_s3_bucket(file, email) -> str:
        session = boto3.session.Session(
            aws_access_key_id=os.environ["AWS_ACCESS_KEY"],
            aws_secret_access_key=os.environ["AWS_SECRET_KEY"]
        )
        bucket = os.environ["AWS_BUCKET"]

        s3_client = session.client('s3')
        file_key = f"avatars/{email}/{file.filename}"
        logger.debug(f"file_key: {file_key}")

        logger.debug(f"send image to s3")
        s3_image_url = f"https://{bucket}.s3.amazonaws.com/{file_key}"
        logger.debug(f"image url: {s3_image_url}")
        try:
            s3_client.upload_fileobj(file.file, bucket, file_key)
        except FileNotFoundError as e:
            logger.error(f"File not found: {e}")
            raise e
        except NoCredentialsError as e:
            logger.error("Error with credentials: {e}")
            raise e

        return s3_image_url

    @staticmethod
    def send_images_to_s3(files, destination_id: str) -> List[str]:
        session = boto3.session.Session(
            aws_access_key_id=os.environ["AWS_ACCESS_KEY"],
            aws_secret_access_key=os.environ["AWS_SECRET_KEY"]
        )
        bucket = os.environ["AWS_BUCKET"]

        s3_client = session.client('s3')
        urls = []

        for file in files:
            file_key = f"guidances/{destination_id}/{file.filename}"
            s3_image_url = f"https://{bucket}.s3.amazonaws.com/{file_key}"
            try:
                s3_client.upload_fileobj(file.file, bucket, file_key)
                urls.append(s3_image_url)
            except FileNotFoundError as e:
                logger.error(f"File not found: {e}")
                raise e
            except boto3.exceptions.NoCredentialsError as e:
                logger.error(f"Credentials error: {e}")
                raise e

        return urls
        
