import pandas as pd
movies_df = pd.read_csv("movies_data.csv", index_col="Title")
print(movies_df.columns)

print(movies_df.rename(columns={ 'Runtime (Minutes)': 'Runtime', 'Revenue (Millions)': 'Revenue_millions'}, inplace=True))
print(movies_df.columns)


movies_df.columns = ['rank', 'genre', 'description', 'director', 'actors', 'year', 'runtime', 
                     'rating', 'votes', 'revenue_millions', 'metascore']

print(movies_df.columns)

movies_df.columns = [col.lower() for col in movies_df]

print(movies_df.columns)


movies_df.columns = [col.lower() for col in movies_df]

print(movies_df.columns)