import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
                'new york city': 'new_york_city.csv',
                'washington': 'washington.csv' }


city = 'chicago'
df = pd.read_csv(CITY_DATA[city])

if df.empty:
    print('Dataframe is empty')
else:
    print('Dataframe has data')

month = "January"



df['Start Time'] = pd.to_datetime(df['Start Time'])





