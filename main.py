from data_treatment import MomaTreat
from data_treatment import TateModernTreat
from data_treatment import RijksmuseumTreat
from utils.Treatment import GetInfoArtObjects
import pandas as pd
import matplotlib
from utils.Treatment import lev_dist, get_similarity

if __name__ == '__main__':
    pd.options.display.max_rows = None
    pd.options.display.max_columns = None

    # df_raw = RijksmuseumTreat.BronzeToSilver()
    # df_raw.bronze_to_silver()
    #

    df_moma = MomaTreat.ArtworksTreat()
    df_moma.bronze_to_silver()
