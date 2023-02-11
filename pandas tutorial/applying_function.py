def rating_function(x):
    if x >= 8.0:
        return "good"
    else:
        return "bad"
    

import pandas as pd
movies_df = pd.read_csv("movies_data.csv", index_col="Title")

movies_df["rating_category"] = movies_df["rating"].apply(rating_function)
print(movies_df.head(2))


movies_df["rating_category"] = movies_df["rating"].apply(lambda x: 'good' if x >= 8.0 else 'bad')

print(movies_df.head(2))