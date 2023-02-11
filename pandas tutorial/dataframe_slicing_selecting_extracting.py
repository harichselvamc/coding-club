import pandas as pd
movies_df = pd.read_csv("movies_data.csv", index_col="Title")

genre_col=movies_df['genre']
print(type(genre_col))

genre_col=movies_df[['genre']]
print(type(genre_col))

subset = movies_df[['genre', 'rating']]

print(subset.head())

# Fetching Data by Rows

## .loc - locates by name
## .iloc- locates by numerical index


prom = movies_df.loc["Prometheus"]

print(prom)

prom = movies_df.iloc[1]
print(prom)

movie_subset = movies_df.loc['Prometheus':'Sing']

movie_subset = movies_df.iloc[1:4]

print(movie_subset)