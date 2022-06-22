from os import listdir
from os.path import isfile, join
import random
from PIL import Image
import pandas as pd
import numpy as np


class DataReader:
    def __init__(self, path):
        self.path = path

    def df_generator(self):
        data = pd.read_excel(self.path, sheet_name=0, header=0)

        df = pd.DataFrame(data)

        return df

