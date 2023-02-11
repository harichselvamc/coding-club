import pandas as pd
movies_df = pd.read_csv("movies_data.csv", index_col="Title")


movie_by_genre=movies_df.groupby(['genre'])
print(movie_by_genre.groups)

print(movie_by_genre['revenue_millions'].mean())

import numpy as np
movies_pivot_by_genre = pd.pivot_table(data=movies_df,index='genre',values='revenue_millions',aggfunc=np.mean)
print(movies_pivot_by_genre)