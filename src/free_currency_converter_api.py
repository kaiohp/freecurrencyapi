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

    def GetHistoricalData(self):
        server = "https://free.currconv.com"
        query = self.fromCurrency + "_" + self.toCurrency
        module = f"/api/v7/convert?q={query},{query}&compact=ultra&date=[{self.startDate}]&endDate=[{self.endDate}]&apiKey=[{self._apitoken}]"
        url = server+module
        response = requests.get(url)
        return response
