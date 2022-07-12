import pandas as pd
from pathlib import Path


class FinalEnrichment:
    def __init__(self):
        self.moma_gold_path = Path("datalake/gold/moma_collection/MomaGold.csv")
        self.rijksmuseum_gold_path = Path("datalake/gold/rijksmuseum/RijksmuseumGold.csv")
        self.tate_gold_path = Path("datalake/gold/tate_collection/TateGold.csv")
        self.artists_catalogue = "datalake/gold/artists_catalogue/artists_catalogue.csv"
        self.final_data_path = "datalake/gold/final_data.csv"

    def generate_final_data(self):
        moma = pd.read_csv(self.moma_gold_path, sep=";", encoding='utf-8')
        rijksmuseum = pd.read_csv(self.rijksmuseum_gold_path, sep=";", encoding='utf-8')
        tate = pd.read_csv(self.tate_gold_path, sep=";", encoding='utf-8')
        artists_catalogue = pd.read_csv(self.artists_catalogue, sep=",", encoding='utf-8',
                                        dtype={'AñoNacimiento,': 'Int64', 'AñoMuerte': 'Int64'})

        common_cols = ["TituloObra", "ArtistaCatálogo", "Museo"]

        moma_selected = moma[common_cols]
        rijksmuseum_selected = rijksmuseum[common_cols]
        tate_selected = tate[common_cols]

        union = pd.concat([moma_selected, rijksmuseum_selected, tate_selected])

        final = union.merge(artists_catalogue, how='left', left_on='ArtistaCatálogo', right_on='Artista')

        final_cols = ["TituloObra", "Artista", "AñoNacimiento", "AñoMuerte", "Movimiento", "Museo"]

        final[final_cols].to_csv(self.final_data_path, sep=";", index=False)
