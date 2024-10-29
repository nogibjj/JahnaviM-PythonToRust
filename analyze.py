'''This file reads a crime dataset based on LAPD.
It produces summary statistics and data visualizations'''

import pandas as pd

def descriptive_stats(csv_file = 'data/bad-drivers.csv'):
    df = pd.read_csv('data/bad-drivers.csv')
    print(df.describe())
    print(df.describe().shape)
    return df.describe()

if __name__ == '__main__':
    descriptive_stats()
