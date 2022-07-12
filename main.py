from data_treatment import ArtistsCatalogueTreat
from data_treatment import MomaTreat
from data_treatment import TateModernTreat
from data_treatment import RijksmuseumTreat
from data_treatment import FinalEnrichment

from utils.Treatment import GetInfoArtObjects
import pandas as pd
import matplotlib
from utils.Treatment import lev_dist, get_similarity

if __name__ == '__main__':
    pd.options.display.max_rows = None
    pd.options.display.max_columns = None

    # CATÁLOGO DE ARTISTAS
    print("Generamos catálogo de artistas")
    artists_catalogue = ArtistsCatalogueTreat.ArtistCatalogueTreat()
    print("Catálogo de artistas de Bronze a Silver")
    artists_catalogue.bronze_to_silver()
    print("Catálogo de artistas de Silver a Gold")
    artists_catalogue.silver_to_gold()

    # MOMA
    moma_artists = MomaTreat.ArtistTreat()
    moma_artists.bronze_to_silver()
    moma_artworks = MomaTreat.ArtworksTreat()
    moma_artworks.bronze_to_silver()

    print("Catálogo de MOMA de Silver a Gold")
    moma_silver_to_gold = MomaTreat.SilverToGold()
    moma_silver_to_gold.silver_to_gold()

    # TATE
    tate = TateModernTreat.TateTreat()
    print("Catálogo de TATE de Bronze a Silver")
    tate.bronze_to_silver()
    print("Catálogo de TATE de Silver a Gold")
    tate.silver_to_gold()

    # RIJKS
    rijks = RijksmuseumTreat.RijksmuseumTreat()
    print("Catálogo de RIJKSMUSEUM de Bronze a Silver")
    rijks.bronze_to_silver()
    print("Catálogo de RIJKSMUSEUM de Silver a Gold")
    rijks.silver_to_gold()

    # Unificación de los tres datasets y enriquecimiento final con el Catálogo de Artistas
    print("Unificación de los tres datasets y enriquecimiento final con el Catálogo de Artistas")
    final = FinalEnrichment.FinalEnrichment()
    final.generate_final_data()
