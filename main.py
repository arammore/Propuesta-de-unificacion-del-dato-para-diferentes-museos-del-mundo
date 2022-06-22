# import json
# import random
# from utils.ArtistClass import *
# import pandas as pd
# from pandas import read_excel
import pandas as pd
import json
from data_treatment import RijksmuseumTreat
from utils.Treatment import GetInfoArtObjects
from utils.Treatment import lev_dist, get_similarity

if __name__ == '__main__':

    rijks = RijksmuseumTreat.ConvertToCSV().reader()

    #  Extraemos la info del json y guardamos en csv
    save_csv = GetInfoArtObjects(rijks).save_in_csv()

    #     probamos similitud entre nombres

    # a = "Da Vinci, Leonardo"
    # b = "Leonardo da Vinci"
    # c = "Leonardo Di Caprio"
    # d = "L & L AIR CONDITIONING"
    # e = "L & L AIR CONDITIONING Service"
    #
    #
    # # Levenshtein distance
    # print(a == b)
    #
    # print(lev_dist(d, e))
    # print(get_similarity(d, d))
