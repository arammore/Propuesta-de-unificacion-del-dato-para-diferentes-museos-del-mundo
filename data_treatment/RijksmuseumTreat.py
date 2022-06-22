import json


class ConvertToCSV:
    def __init__(self):
        self.path = "sources/rijksmuseum/response.json"

    def reader(self):
        with open(self.path, 'r') as f:
            return json.load(f)

    def save_to_csv(self):
        reader = self.reader()
