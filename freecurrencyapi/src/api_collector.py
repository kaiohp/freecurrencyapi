import requests


class FreeCurrencyCollector:
    """
    Nice description here
    """
    def __init__(self, base_currency="BRL", api_token=None):
        """
        The init method
        """
        self.base_currency = base_currency
        self.base_url = "https://api.freecurrencyapi.com"
        self._APIKEY = api_token

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
