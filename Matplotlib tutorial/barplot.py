import pandas as pd
import numpy as np

# Importing
import matplotlib.pyplot as plt

df=pd.read_csv('food_data.csv')
print(df.head)

orders_per_category = pd.pivot_table(data=df,index='category',values='num_orders',aggfunc=np.sum)
print(orders_per_category)
plt.bar(orders_per_category.index,orders_per_category['num_orders'])
plt.show()

plt.bar(orders_per_category.index,orders_per_category['num_orders'])

# Rotating x ticks.
plt.xticks(rotation=70) 


plt.show()

plt.bar(orders_per_category.index,orders_per_category['num_orders'])
plt.xticks(rotation=70) 

plt.xlabel('Food item')
plt.ylabel('Number of orders') 

plt.savefig("plot.png")
plt.show()

total = df['num_orders'].sum()
orders_by_cuisine = df.groupby(['cuisine'])['num_orders'].sum()
orders_by_cuisine