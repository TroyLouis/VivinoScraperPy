import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_white_wine = pd.read_excel('/Users/troy/PycharmProjects/Vivino/white_wine_0to400_anyrating.xlsx')
df_red_wine = pd.read_excel('/Users/troy/PycharmProjects/Vivino/red_wine_0to400_anyrating.xlsx')
df_sparkling_wine = pd.read_excel('/Users/troy/PycharmProjects/Vivino/sparkling_wine_0to400_anyrating.xlsx')

df_white = df_white_wine.drop(columns = 'Unnamed: 0')
df_white.index = np.arange(0, len(df_white))
df_white = df_white.dropna()
df_white = df_white[~df_white['Price'].str.contains('View shops')]
df_white = df_white[~df_white['Price'].str.contains('ratings')]

for item in df_white['Price']:
    if '$' in item:
        df_white['Price'] = df_white['Price'].str.replace('$','')
        df_white['Price'] = df_white['Price'].astype(float)

df_red = df_red_wine.drop(columns = 'Unnamed: 0')
df_red.index = np.arange(0, len(df_red))
df_red = df_red.dropna()
df_red = df_red[~df_red['Price'].str.contains('View shops')]
df_red = df_red[~df_red['Price'].str.contains('ratings')]

for item in df_red['Price']:
    if '$' in item:
        df_red['Price'] = df_red['Price'].str.replace('$','')
        df_red['Price'] = df_red['Price'].astype(float)

df_sparkling = df_sparkling_wine.drop(columns = 'Unnamed: 0')
df_sparkling.index = np.arange(0, len(df_sparkling))
df_sparkling = df_sparkling.dropna()
df_sparkling = df_sparkling[~df_sparkling['Price'].str.contains('View shops')]
df_sparkling = df_sparkling[~df_sparkling['Price'].str.contains('ratings')]

for item in df_sparkling['Price']:
    if '$' in item:
        df_sparkling['Price'] = df_sparkling['Price'].str.replace('$','')
        df_sparkling['Price'] = df_sparkling['Price'].astype(float)

