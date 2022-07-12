import json
import pandas as pd
from pathlib import Path
from utils import Treatment


class RijksmuseumTreat:
    def __init__(self):
        self.bronze_path = Path("datalake/bronze/rijksmuseum/response.json")
        self.silver_path = Path("datalake/silver/rijksmuseum/rijksmuseum.csv")
        self.gold_path = Path("datalake/gold/rijksmuseum/RijksmuseumGold.csv")

    def read_bronze(self):
        with open(self.bronze_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def read_silver(self):
        return pd.read_csv(self.silver_path, sep=";", encoding='utf-8')

    def bronze_to_silver(self):
        df_input = self.read_bronze()
        cols = ['title', 'principalOrFirstMaker', 'longTitle']

        df_output = pd.DataFrame(columns=cols)

        for row in df_input['artObjects']:
            df_output = df_output.append(dict(zip(cols, (row[x] for x in cols))),
                                         ignore_index=True)

        self.silver_path.parent.mkdir(parents=True, exist_ok=True)
        df_output.to_csv(self.silver_path, sep=";", index=False)

    def silver_to_gold(self):
        renamed_dict = {"title": "TituloObra", "principalOrFirstMaker": "Artista", "longTitle": "TítuloCompleto"}
        df_silver = self.read_silver()

        # Renombrado de columnas
        df_silver.rename(columns=renamed_dict, inplace=True)

        # Mergeo con catálogo
        df_output = Treatment.merge_catalogue(df_silver, "Artista")

        # Añadimos nombre del museo
        df_output["Museo"] = "RIJKSMUSEUM"
        self.gold_path.parent.mkdir(parents=True, exist_ok=True)
        df_output.to_csv(self.gold_path, sep=";", index=False)
