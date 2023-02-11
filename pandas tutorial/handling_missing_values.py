import pandas as pd
movies_df = pd.read_csv("movies_data.csv", index_col="Title")

print(movies_df.isnull())
print(movies_df.isnull().sum())
#removing null values
print(movies_df.dropna())
print(movies_df.dropna(inplace=True))
#imputation
revenue = movies_df['revenue_millions']
print(revenue.head())

revenue_mean = revenue.mean()
print(revenue_mean)

revenue.fillna(revenue_mean, inplace=True)
movies_df.isnull().sum()