import pandas as pd
from pathlib import Path
from utils import Treatment

bronze_path = "datalake/bronze/moma_collection"
silver_path = "datalake/silver/moma_collection"
gold_path = "datalake/gold/moma_collection"


class ArtistTreat:
    def __init__(self):
        self.bronze_path = Path(bronze_path + "/artists.csv")
        self.silver_path = Path(silver_path + "/moma_artists.csv")

    def read(self):
        return pd.read_csv(self.bronze_path, sep=",", encoding='utf-8',
                           dtype={'Birth Year': 'Int64', 'Death Year': 'Int64'})

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
        self.bronze_path = Path(bronze_path + "/artworks.csv")
        self.silver_path = Path(silver_path + "/moma_artworks.csv")

    def read(self):
        return pd.read_csv(self.bronze_path, sep=",", encoding='utf-8')

    def lost_data(self):
        df = self.read()
        print('Artworks datos no informados:')
        for i in df.columns:
            print(i, f'{100 * df[i].isnull().sum() / df.shape[0]:.2f}%')

    def bronze_to_silver(self):
        df_input = self.read()
        cols = ['Artist ID', 'Title', 'Date', 'Medium', 'Dimensions', 'Acquisition Date', 'Catalogue', 'Department',
                'Classification']
        df_output = df_input[cols]

        self.silver_path.parent.mkdir(parents=True, exist_ok=True)
        df_output.to_csv(self.silver_path, sep=";", index=False)


class SilverToGold:
    def __init__(self):
        self.silver_path_artists = Path(silver_path + "/moma_artists.csv")
        self.silver_path_artworks = Path(silver_path + "/moma_artworks.csv")
        self.gold_path = Path(gold_path + "/MomaGold.csv")
        self.renamed_dict = {"Title": "TituloObra",
                             "Date": "Fecha",
                             "Name": "Artista",
                             "Nationality": "Nacionalidad",
                             "Gender": "Género",
                             "Birth Year": "AñoNacimiento",
                             "Death Year": "AñoMuerte",
                             "Medium": "Técnica",
                             "Dimensions": "Dimensiones",
                             "Acquisition Date": "FechaAdquisicion",
                             "Catalogue": "Catálogo",
                             "Department": "Departamento",
                             "Classification": "Clasificación"
                             }

        self.output_cols = ['TituloObra', 'Fecha', 'Artista', 'ArtistaCatálogo', 'Nacionalidad', 'Género',
                            'AñoNacimiento', 'AñoMuerte',
                            'Técnica', 'Dimensiones', 'FechaAdquisicion', 'Catálogo', 'Departamento', 'Clasificación',
                            'Museo']

    def silver_to_gold(self):
        moma_artists = pd.read_csv(self.silver_path_artists, sep=";",
                                   dtype={'Birth Year': 'Int64', 'Death Year': 'Int64'})
        moma_artworks = pd.read_csv(self.silver_path_artworks, sep=";")

        regex = "^\d+$"
        moma_artworks = moma_artworks[moma_artworks["Artist ID"].notnull()]
        moma_artworks = moma_artworks[moma_artworks["Artist ID"].str.match(regex)]
        moma_artworks = moma_artworks.astype({'Artist ID': 'int'})

        df_output = pd.merge(moma_artists, moma_artworks, on="Artist ID")

        del df_output["Artist ID"]

        df_output.rename(columns=self.renamed_dict, inplace=True)
        df_output["Museo"] = "MOMA"

        df_final = Treatment.merge_catalogue(df_silver=df_output, artist_col_silver="Artista")

        self.gold_path.parent.mkdir(parents=True, exist_ok=True)
        df_final[self.output_cols].to_csv(self.gold_path, sep=";", index=False)
