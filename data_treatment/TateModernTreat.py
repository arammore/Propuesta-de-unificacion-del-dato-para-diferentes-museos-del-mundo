import pandas as pd
from pathlib import Path


class TateTreat:
    def __init__(self):
        self.bronze_path = Path("datalake/bronze/tate_collection/the-tate-collection.csv")
        self.silver_path = Path("datalake/silver/tate_collection/tate.csv")

    def read(self):
        return pd.read_csv(self.bronze_path, sep=";", encoding='utf-8')

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
        cols = ['artist', 'artistRole', 'title',
                'dateText', 'medium', 'year', 'acquisitionYear',
                'dimensions', 'width', 'height']

        df_output = df_input[cols]

        self.silver_path.parent.mkdir(parents=True, exist_ok=True)
        df_output.to_csv(self.silver_path, sep=";", index=False)
