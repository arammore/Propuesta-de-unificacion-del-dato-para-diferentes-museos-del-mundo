import pandas as pd


class ArtistTreat:
    def __init__(self):
        self.path = "sources/moma_collection/artists.csv"

    def read(self):
        return pd.read_csv(self.path, sep=",")


class ArtworksTreat:
    def __init__(self):
        self.path = "sources/moma_collection/artworks.csv"

    def read(self):
        return pd.read_csv(self.path, sep=",", header=True)
