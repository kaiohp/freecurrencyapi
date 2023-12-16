import requests
import os
from dotenv import load_dotenv


class FreeCurrencyAPI:
    """
    Nice description here
    """
    def __init__(self, base_currency="BRL"):
        """
        The init method
        """
        self.base_currency = base_currency
        self.base_url = "https://api.freecurrencyapi.com"
        load_dotenv()
        self._apikey = os.getenv("API_TOKEN", None)

    def GetLatest(self):
        """
        The GetLatest method
        """
        endpoint = "/v1/latest"
        request_url = self.base_url + endpoint
        params = {"base_currency": self.base_currency}

        with requests.session() as session:
            session.headers.update({"apikey": self._apikey})
            response = session.get(
                request_url,
                params=params
            )
        if response.status_code == 200:  # API docs: success -> status code 200
            return response.json()
        else:
            raise Exception(response.status_code)
