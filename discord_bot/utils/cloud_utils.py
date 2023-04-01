from config import DISCORD
from google.cloud import storage
from google.oauth2 import service_account


class CloudStorage(object):
    def __init__(self, key_path = DISCORD.gcp.key, bucket = DISCORD.gcp.bucket):
        # Load the service account key file and create a credentials object
        self.credentials = service_account.Credentials.from_service_account_file(
            key_path,
            scopes=['https://www.googleapis.com/auth/cloud-platform']
        )
        self.client = storage.Client(credentials=self.credentials)
        self.bucket = self.client.bucket(bucket)
        return None
    
    def upload_image(self, file_path, filename):
        destination_blob_name = f'{DISCORD.gcp.blob}/{filename}.jpg'
        blob = self.bucket.blob(destination_blob_name)
        self.upload_image_to_blob(blob, file_path)
        return f"https://storage.googleapis.com/{destination_blob_name}"
    
    @staticmethod
    def upload_image_to_blob(blob, file_path):
        # Upload the local file to the Cloud Storage bucket
        return blob.upload_from_filename(file_path)