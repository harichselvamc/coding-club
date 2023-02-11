import pandas as pd
import numpy as np

# Importing
import matplotlib.pyplot as plt

df=pd.read_csv('food_data.csv')
print(df.head)

df['revenue'] = df.apply(lambda x: x.checkout_price*x.num_orders,axis=1) 
df.head()

df['month'] = df['week'].apply(lambda x: x//4) 
df.head()

weekly_sales = df.groupby(['week'])['revenue'].sum()
monthly_sales = df.groupby(['month'])['revenue'].sum()
print(weekly_sales.head())
print(monthly_sales.head())

plt.plot(weekly_sales.index, weekly_sales, 'bo-')
plt.show()


plt.plot(monthly_sales.index, monthly_sales, 'go-')
plt.show()