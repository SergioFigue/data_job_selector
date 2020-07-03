import pandas as pd
pd.set_option('mode.chained_assignment', None)
# acquisition functions

def acquire():
    data = pd.read_csv('./data/processed/glob_data.csv')
    print(data.head())
    return data
