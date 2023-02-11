import pandas as pd
movies_df = pd.read_csv("movies_data.csv", index_col="Title")

print(movies_df.corr())