import pandas as pd

df = pd.read_csv('data/tcc_ceds_music.csv', sep=',')

print(df[df['artist_name'] == 'the beatles'])
print(df[df['artist_name'] == 'queen']['genre'].unique())

print(df.columns)