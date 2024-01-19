from api_collector import FreeCurrencyCollector
from file_handle import FileHandler
from cloud_storage import CSClient
from dotenv import load_dotenv, find_dotenv
import os


def start(request):
    load_dotenv(find_dotenv())
    local_env = os.getenv("LOCAL")
    collector = FreeCurrencyCollector()
    api_data = collector.get_latest()

    if local_env == "1":
        file_explore = FileHandler()
        file_explore.save_json(api_data)
    else:
        cloud_storage_client = CSClient()
        currency = collector.base_currency
        path = cloud_storage_client.create_path()
        destination = f"{currency}/{currency}_{path}"
        return cloud_storage_client.send_json_object(
            api_data,
            destination=destination,
            bucket_name='free_currency_exchange_data'
        )


if __name__ == "__main__":
    start({"Local": "Mudei a conta de serviço"})
