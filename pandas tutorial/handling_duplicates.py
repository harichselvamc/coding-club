import pandas as pd
movies_df = pd.read_csv("movies_data.csv", index_col="Title")
print(movies_df.duplicated())

print(movies_df.duplicated().sum())

temp_df = movies_df.append(movies_df)

print(temp_df.shape())

print(temp_df.duplicated().sum())


temp_df = temp_df.drop_duplicates()
print(temp_df.duplicated().sum())

print(temp_df.drop_duplicates(inplace=True))

temp_df = movies_df.append(movies_df)

print(temp_df.drop_duplicates(inplace=True, keep=False))

print(temp_df.shape())