import pandas as pd
from pathlib import Path
from utils import Treatment


class TateTreat:
    def __init__(self):
        self.bronze_path = Path("datalake/bronze/tate_collection/the-tate-collection.csv")
        self.silver_path = Path("datalake/silver/tate_collection/tate.csv")
        self.gold_path = Path("datalake/gold/tate_collection/TateGold.csv")

    def read_bronze(self):
        return pd.read_csv(self.bronze_path, sep=";", encoding='utf-8')

    def read_silver(self):
        return pd.read_csv(self.silver_path, sep=";", encoding='utf-8',
                           dtype={'dateText,': 'Int64', 'year': 'Int64', 'acquisitionYear': 'Int64'})

    def lost_data(self):
        df = self.read_bronze()
        print('Artists datos no informados:')
        for i in df.columns:
            print(i, f'{100 * df[i].isnull().sum() / df.shape[0]:.2f}%')

    def add_age(self):
        df = self.read_bronze()
        df['Age'] = df['Death Year'] - df['Birth Year']
        return df

    def bronze_to_silver(self):
        df_input = self.read_bronze()
        cols = ['artist', 'artistRole', 'title',
                'dateText', 'medium', 'year', 'acquisitionYear',
                'dimensions', 'width', 'height']

        df_output = df_input[cols]

        self.silver_path.parent.mkdir(parents=True, exist_ok=True)
        df_output.to_csv(self.silver_path, sep=";", index=False)

    def silver_to_gold(self):
        renamed_dict = {"artist": "Artista",
                        "artistRole": "PapelArtista",
                        "title": "TituloObra",
                        "dateText": "FechaDeTexto",
                        "medium": "Medio",
                        "year": "Año",
                        "acquisitionYear": "AñoAdquisicion",
                        "dimensions": "Dimensiones",
                        "width": "Ancho",
                        "height": "Alto"
                        }
        df_silver = self.read_silver()

        df_silver.rename(columns=renamed_dict, inplace=True)

        silver_catalogue_merge = Treatment.merge_catalogue(df_silver=df_silver, artist_col_silver="Artista")

        silver_catalogue_merge["Museo"] = "TATE"

        self.gold_path.parent.mkdir(parents=True, exist_ok=True)
        silver_catalogue_merge.to_csv(self.gold_path, sep=";", index=False)
