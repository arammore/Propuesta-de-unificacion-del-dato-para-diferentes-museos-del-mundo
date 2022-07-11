import json
import pandas as pd
from pathlib import Path


class BronzeToSilver:
    def __init__(self):
        self.bronze_path = Path("datalake/bronze/rijksmuseum/response.json")
        self.silver_path = Path("datalake/silver/rijksmuseum/rijksmuseum.csv")

    def reader(self):
        with open(self.bronze_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def bronze_to_silver(self):
        df_input = self.reader()
        cols = ['title', 'principalOrFirstMaker', 'longTitle']

        df_output = pd.DataFrame(columns=['title', 'principalOrFirstMaker', 'longTitle'])

        for row in df_input['artObjects']:
            df_output = df_output.append(dict(zip(cols, (row[x] for x in cols))), ignore_index=True)

        self.silver_path.parent.mkdir(parents=True, exist_ok=True)
        df_output.to_csv(self.silver_path, sep=";", index=False)
