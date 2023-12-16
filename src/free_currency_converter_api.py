import requests
import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
from datetime import datetime
import json


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
        self._dotenv_path = find_dotenv()
        load_dotenv(self._dotenv_path)
        self._apikey = os.getenv("API_TOKEN")

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


class FileHandler:
    """
    The Great docs here
    """
    def __init__(self):
        self.run_datetime = datetime.now().date().isoformat()
        self.local = Path("../data/raw")
        self.file_name = "apidata_"+self.run_datetime+".json"

    def save_json(self, data, local=None, file_name=None):

        if local is None:
            local = self.local

        if file_name is None:
            file_name = self.file_name

        full_path = local / file_name

        with full_path.open(mode='w') as file:
            json.dump(data, file, indent=4)
