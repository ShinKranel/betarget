from contextlib import asynccontextmanager
from pathlib import Path

from aiobotocore.session import get_session

from backend.src.config import settings
from backend.src.logger import logger


class S3Client:
    def __init__(self, access_key: str, secret_key: str, bucket_name: str, end_point_url: str):
        self.bucket_name = bucket_name
        self.access_key = access_key
        self.secret_key = secret_key
        self.end_point_url = end_point_url
        self.session = get_session()

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client(
            's3',
            endpoint_url=self.end_point_url,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
        ) as client:
            yield client

    async def upload_file(self, object_name: str, file_path: Path | None = None, file_data: bytes | None = None):
        async with self.get_client() as client:
            if file_path:
                with open(file_path, 'rb') as f:
                    file_data = f.read()
            if file_data:
                await client.put_object(
                    Bucket=self.bucket_name,
                    Key=object_name,
                    Body=file_data
                )
                logger.info(f"File {object_name} is uploaded")
            else:
                logger.warning(f"File {object_name} can't be uploaded")

    async def download_file(self, object_name: str) -> bytes:
        async with self.get_client() as client:
            response = await client.get_object(
                Bucket=self.bucket_name,
                Key=object_name
            )
            file_data = await response['Body'].read()
            logger.info(f"File {object_name} is downloaded")
            return file_data


s3_settings = settings.s3
s3_client = S3Client(
    access_key=s3_settings.S3_ACCESS_KEY,
    secret_key=s3_settings.S3_SECRET_KEY,
    bucket_name=s3_settings.S3_BUCKET_NAME,
    end_point_url=s3_settings.S3_ENDPOINT_URL
)
