import pandas as pd
movies_df = pd.read_csv("movies_data.csv", index_col="Title")

condition = (movies_df['director'] == "Ridley Scott")

condition.head()

movies_df[movies_df['director'] == "Ridley Scott"]

movies_df[movies_df['rating'] >= 8.6].head(3)


movies_df[(movies_df['director'] == 'Christopher Nolan') | (movies_df['director'] == 'Ridley Scott')].head()

print(movies_df[movies_df['director'].isin(['Christopher Nolan', 'Ridley Scott'])].head())

movies_df[
    ((movies_df['year'] >= 2005) & (movies_df['year'] <= 2010))
    & (movies_df['rating'] > 8.0)
    & (movies_df['revenue_millions'] < movies_df['revenue_millions'].quantile(0.25))
]



print(movies_df.describe())