from google.cloud import storage
from datetime import datetime
import json


class CSClient():
    def __init__(self):
        self.client = storage.Client()

    def create_path(self):
        now_timestamp = datetime.now()
        year = now_timestamp.year
        month = now_timestamp.month
        day = now_timestamp.date().isoformat()
        path = f"{str(year)}/{str(month)}/{day}.json"
        return path

    def send_json_object(self, data, destination, bucket_name):
        bucket = self.client.get_bucket(bucket_name)
        blob = bucket.blob(destination)
        blob.upload_from_string(json.dumps(data), 'text/json')
        return f"Data saved on Cloud Storage in {bucket_name}/{destination}"
