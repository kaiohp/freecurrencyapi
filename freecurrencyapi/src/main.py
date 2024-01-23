from api_collector import FreeCurrencyCollector
from file_handle import FileHandler
from gcloud import GClient
from dotenv import load_dotenv, find_dotenv
import os


def start(request):
    load_dotenv(find_dotenv())
    if request == "Local":
        secret = os.getenv("API_TOKEN")
        collector = FreeCurrencyCollector(api_token=secret)
        api_data = collector.get_latest()
        file_explore = FileHandler()
        file_explore.save_json(api_data)
    else:
        google_cloud = GClient()
        project_id = os.getenv("PROJECT_ID")
        secret_id = os.getenv("SECRET_ID")
        version_id = os.getenv("VERSION_ID")
        secret = google_cloud.access_secret(project_id, secret_id, version_id)
        collector = FreeCurrencyCollector(api_token=secret)
        api_data = collector.get_latest()
        currency = collector.base_currency
        path = google_cloud.create_path(currency)
        google_cloud.send_json_object(
            api_data,
            destination=path,
            bucket_name='free_currency_exchange_data'
        )
    return None


if __name__ == "__main__":
    start("Remoto")
