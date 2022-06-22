from os import listdir
from os.path import isfile, join
import random
from PIL import Image
import pandas as pd
import numpy as np
import re
from functools import lru_cache
import re, math
from collections import Counter

WORD = re.compile(r'\w+')


def get_cosine(vec1, vec2):
    # print vec1, vec2
    intersection = set(vec1.keys()) & set(vec2.keys())
    print(intersection)
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    print(numerator)

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    print(denominator)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    print(Counter(WORD.findall(text)))
    return Counter(WORD.findall(text))


def get_similarity(a, b):
    a = text_to_vector(a.strip().lower())
    b = text_to_vector(b.strip().lower())

    return get_cosine(a, b)


def lev_dist(a, b):
    '''
    This function will calculate the levenshtein distance between two input
    strings a and b

    params:
        a (String) : The first string you want to compare
        b (String) : The second string you want to compare

    returns:
        This function will return the distnace between string a and b.

    example:
        a = 'stamp'
        b = 'stomp'
        lev_dist(a,b)
        >> 1.0
    '''

    @lru_cache(None)  # for memorization
    def min_dist(s1, s2):

        if s1 == len(a) or s2 == len(b):
            return len(a) - s1 + len(b) - s2

        # no change required
        if a[s1] == b[s2]:
            return min_dist(s1 + 1, s2 + 1)

        return 1 + min(
            min_dist(s1, s2 + 1),  # insert character
            min_dist(s1 + 1, s2),  # delete character
            min_dist(s1 + 1, s2 + 1),  # replace character
        )

    return min_dist(0, 0)


def get_work_date(obj_long_title: str):
    x = re.findall("\d+", obj_long_title.split(',')[-1])

    return '-'.join(x)


class GetInfoArtObjects:
    def __init__(self, json):
        self.json = json

    def save_in_csv(self):
        for obj in self.json["artObjects"]:
            obj_title = obj["title"]
            obj_longTitle = obj["longTitle"]
            obj_principalOrFirstMaker = obj["principalOrFirstMaker"]

            # Nombres definitivos que se guardarán en el csv

            title = obj_title
            work_date = get_work_date(obj_longTitle)
            print(title)
            print(work_date)
            print('-' * 50)
