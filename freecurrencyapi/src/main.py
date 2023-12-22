from api_collector import FreeCurrencyCollector
from file_handle import FileHandler


def start():
    collector = FreeCurrencyCollector()
    file_explore = FileHandler()
    api_data = collector.get_latest()
    file_explore.save_json(api_data)


if __name__ == "__main__":
    start()
