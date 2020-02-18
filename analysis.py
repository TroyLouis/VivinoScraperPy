import pandas as pd

df_white_wine = pd.read_excel('white_wine_0to400_anyrating.xlsx')
df_red_wine = pd.read_excel('red_wine_0to400_anyrating.xlsx')
df_sparkling_wine = pd.read_excel('sparkling_wine_0to400_anyrating.xlsx')

df_list = (df_white_wine, df_red_wine, df_sparkling_wine)  
appended_df = pd.concat(df_list)

df = appended_df.drop(columns = 'Unnamed: 0')

df.index = np.arange(0, len(df))

df = df.dropna()

df = df[~df['Price'].str.contains('View shops')]
df = df[~df['Price'].str.contains('ratings')]

for item in df['Price']:
    if '$' in item:
        df['Price'] = df['Price'].str.replace('$','')

