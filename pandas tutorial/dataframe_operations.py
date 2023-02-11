import pandas as pd

movies_df = pd.read_csv("movies_data.csv", index_col="Title")
print(movies_df.head())

print(movies_df.head(10))

print(movies_df.tail())
movies_df.tail(10)


#gettin info about data
print(movies_df.info())
print(movies_df.shape())
