import pandas as pd
from pathlib import Path

bronze_path = "datalake/bronze/artists_catalogue"
silver_path = "datalake/silver/artists_catalogue"
gold_path = "datalake/gold/artists_catalogue"


class ArtistCatalogueTreat:
    def __init__(self):
        self.bronze_path = Path(bronze_path + "/artists_catalogue.xlsx")
        self.silver_path = Path(silver_path + "/artists_catalogue.csv")
        self.gold_path = Path(gold_path + "/artists_catalogue.csv")

    def read(self):
        return pd.read_excel(self.bronze_path, dtype={'AñoNacimiento': 'Int64', 'AñoMuerte': 'Int64'})

    def bronze_to_silver(self):
        df_input = self.read()

        self.silver_path.parent.mkdir(parents=True, exist_ok=True)
        df_input.to_csv(self.silver_path, index=None, header=True)

    def silver_to_gold(self):
        df = pd.read_csv(self.silver_path, sep=",", encoding='utf-8',
                         dtype={'AñoNacimiento': 'Int64', 'AñoMuerte': 'Int64'})

        self.gold_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(self.gold_path, index=None, header=True)
