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

    df_tate = TateModernTreat.TateTreat()
    df_tate.bronze_to_silver()
