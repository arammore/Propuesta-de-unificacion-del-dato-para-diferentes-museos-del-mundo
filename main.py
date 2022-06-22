from data_treatment import RijksmuseumTreat, MomaTreat
from utils.Treatment import GetInfoArtObjects
import pandas as pd

if __name__ == '__main__':
    moma_df = MomaTreat.ArtistTreat()
    print(moma_df.read)

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
