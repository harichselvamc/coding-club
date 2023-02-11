import pandas as pd
import numpy as np

# Importing
import matplotlib.pyplot as plt

df=pd.read_csv('food_data.csv')
print(df.head)

base_price_by_cuisine = df.groupby(['cuisine'])['base_price'].unique()
print(base_price_by_cuisine)

plt.boxplot([x for x in base_price_by_cuisine],labels=[x for x in base_price_by_cuisine.index])

plt.xlabel('Cuisine') 
plt.ylabel('Price') 
 
plt.title('Analysing cuisine price') 
plt.show()