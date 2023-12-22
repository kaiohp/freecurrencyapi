import requests
import os
from dotenv import load_dotenv, find_dotenv


class FreeCurrencyCollector:
    """
    Nice description here
    """
    def __init__(self, base_currency="BRL"):
        """
        The init method
        """
        self.base_currency = base_currency
        self.base_url = "https://api.freecurrencyapi.com"
        load_dotenv(find_dotenv())
        self._APIKEY = os.getenv("API_TOKEN")

    def get_latest(self):
        """
        The GetLatest method
        """
        endpoint = "/v1/latest"
        request_url = self.base_url + endpoint
        params = {"base_currency": self.base_currency}

        with requests.session() as session:
            session.headers.update({"apikey": self._APIKEY})
            response = session.get(
                request_url,
                params=params
            )

        if response.status_code in range(200, 300):
            return response.json()
        else:
            raise Exception(response.status_code)


if __name__ == "__main__":
    collector = FreeCurrencyCollector()
    api_data = collector.get_latest()
    print(type(api_data))
    print(api_data)
