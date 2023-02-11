import pandas as pd
import numpy as np

# Importing
import matplotlib.pyplot as plt

# only "explode" the 3rd slice (i.e. 'Italian')
df=pd.read_csv("food_data.csv")
df.head()

explode = (0, 0, 0.1, 0)  
total = df['num_orders'].sum()
orders_by_cuisine = df.groupby(['cuisine'])['num_orders'].sum()
orders_by_cuisine

plt.pie([x/total for x in orders_by_cuisine],labels=[x for x in orders_by_cuisine.index],autopct='%0.1f',explode=explode) 

plt.title('Cuisine share %') 
plt.show()