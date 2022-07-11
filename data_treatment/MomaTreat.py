import pandas as pd
from pathlib import Path


class ArtistTreat:
    def __init__(self):
        self.bronze_path = Path("datalake/bronze/moma_collection/artists.csv")
        self.silver_path = Path("datalake/silver/moma_collection/artists_moma.csv")

    def read(self):
        return pd.read_csv(self.bronze_path, sep=",", encoding='utf-8')

    def lost_data(self):
        df = self.read()
        print('Artists datos no informados:')
        for i in df.columns:
            print(i, f'{100 * df[i].isnull().sum() / df.shape[0]:.2f}%')

    def add_age(self):
        df = self.read()
        df['Age'] = df['Death Year'] - df['Birth Year']
        return df

    def bronze_to_silver(self):
        df_input = self.read()
        cols = ['Artist ID', 'Name', 'Nationality', 'Gender', 'Birth Year',
                'Death Year']
        df_output = df_input[cols]

        self.silver_path.parent.mkdir(parents=True, exist_ok=True)
        df_output.to_csv(self.silver_path, sep=";", index=False)


class ArtworksTreat:
    def __init__(self):
        self.bronze_path = Path("datalake/bronze/moma_collection/artworks.csv")
        self.silver_path = Path("datalake/silver/moma_collection/artworks_moma.csv")

    def read(self):
        return pd.read_csv(self.bronze_path, sep=",")

    def lost_data(self):
        df = self.read()
        print('Artworks datos no informados:')
        for i in df.columns:
            print(i, f'{100 * df[i].isnull().sum() / df.shape[0]:.2f}%')

    def bronze_to_silver(self):
        df_input = self.read()
        cols = ['Title', 'Artist ID', 'Date', 'Medium', 'Dimensions', 'Acquisition Date', 'Catalogue', 'Department',
                'Classification']
        df_output = df_input[cols]

        self.silver_path.parent.mkdir(parents=True, exist_ok=True)
        df_output.to_csv(self.silver_path, sep=";", index=False)
