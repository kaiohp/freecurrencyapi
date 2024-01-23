from google.cloud import storage, secretmanager
import google_crc32c
from datetime import datetime
import json


class GClient():
    def __init__(self):
        self.client = storage.Client()

    def create_path(self, prefix):
        now_timestamp = datetime.now()
        year = now_timestamp.year
        month = now_timestamp.month
        day = now_timestamp.date().isoformat()
        path = f"{prefix}/{str(year)}/{str(month)}/{prefix}_{day}.json"
        return path

    def send_json_object(self, data, destination, bucket_name):
        bucket = self.client.get_bucket(bucket_name)
        blob = bucket.blob(destination)
        blob.upload_from_string(json.dumps(data), 'text/json')
        return print(f"Data saved on Cloud Storage in {bucket_name}/{destination}")

    def access_secret(self, project_id, secret_id, version_id):
        secret_path = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

        with secretmanager.SecretManagerServiceClient() as client:
            client = secretmanager.SecretManagerServiceClient()
            response = client.access_secret_version(request={"name": secret_path})

        crc32c = google_crc32c.Checksum()
        crc32c.update(response.payload.data)
        if response.payload.data_crc32c != int(crc32c.hexdigest(), 16):
            print("Data corruption detected.")
            return response
        payload = response.payload.data.decode("UTF-8")
        return payload
