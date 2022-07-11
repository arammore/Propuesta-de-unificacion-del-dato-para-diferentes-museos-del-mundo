import json
import pandas as pd
from pathlib import Path


class ArtistTreat:
    def __init__(self):
        self.path = Path("sources/tate_collection/the-tate-collection.csv")

    def read(self):
        return pd.read_csv(self.path, sep=";")

    def lost_data(self):
        df = self.read()
        print('Artists datos no informados:')
        for i in df.columns:
            print(i, f'{100 * df[i].isnull().sum() / df.shape[0]:.2f}%')

    def add_age(self):
        df = self.read()
        df['Age'] = df['Death Year'] - df['Birth Year']
        return df


class ArtworksTreat:
    def __init__(self):
        self.path = "sources/moma_collection/artworks.csv"

    def read(self):
        return pd.read_csv(self.path, sep=",")

    def lost_data(self):
        df = self.read()
        print('Artworks datos no informados:')
        for i in df.columns:
            print(i, f'{100 * df[i].isnull().sum() / df.shape[0]:.2f}%')
