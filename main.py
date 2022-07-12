from data_treatment import MomaTreat
from data_treatment import TateModernTreat
from data_treatment import RijksmuseumTreat
from data_treatment import ArtistsCatalogueTreat
from utils.Treatment import GetInfoArtObjects
import pandas as pd
import matplotlib
from utils.Treatment import lev_dist, get_similarity

if __name__ == '__main__':
    pd.options.display.max_rows = None
    pd.options.display.max_columns = None

    # df_raw = RijksmuseumTreat.RijksmuseumTreat()
    # df_raw.silver_to_gold()

    # df_artists_catalogue = ArtistsCatalogueTreat.ArtistCatalogueTreat()
    # df_artists_catalogue.silver_to_gold()

    # df_moma = MomaTreat.SilverToGold()
    # df_moma.silver_to_gold()
    #
    # #
    # #
    # df_moma = MomaTreat.SilverToGold()
    # df = df_moma.silver_to_gold()

    with_catalogue = TateModernTreat.TateTreat()
    with_catalogue.silver_to_gold()
