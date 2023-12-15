import requests
import os
from dotenv import load_dotenv


class CurrencyAPI:

    def __init__(self, startDate, endDate, fromCurrency, toCurrency):
        self.startDate = startDate
        self.endDate = endDate
        self.fromCurrency = fromCurrency
        self.toCurrency = toCurrency
        load_dotenv()
        self._apitoken = os.getenv('API_TOKEN', None)

    def GetHistoricalData(self):
        server = "https://free.currconv.com"
        query = self.fromCurrency + "_" + self.toCurrency
        module = f"/api/v7/convert?q={query},{query}&compact=ultra&date=[{self.startDate}]&endDate=[{self.endDate}]&apiKey=[{self._apitoken}]"
        url = server+module
        response = requests.get(url)
        return response
