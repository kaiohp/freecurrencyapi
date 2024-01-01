import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
from datetime import datetime
import json


class FileHandler:
    """
    The Great docs here
    """
    def __init__(self, local="freecurrencyapi/data/raw", file_name="apidata"):

        self.run_datetime = datetime.now().date().isoformat()
        self.local = Path(local)
        self.file_name = f"{file_name}_{self.run_datetime}.json"
        load_dotenv(find_dotenv())
        self._GCLOUD = os.getenv("GCLOUD")

    def save_json(self, data):

        full_path = Path(self.local, self.file_name).resolve()

        with full_path.open(mode='w') as file:
            json.dump(data, file, indent=4)


if __name__ == "__main__":
    test_data = json.dumps({"Test": "Sucess"})
    file_explore = FileHandler(local="freecurrencyapi/tests/data", file_name="test_data")
    file_explore.save_json(test_data)
