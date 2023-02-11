import pandas as pd
import numpy as np

# Importing
import matplotlib.pyplot as plt

df=pd.read_csv('food_data.csv')
print(df.head)

orders_by_area = df.groupby(['op_area'])['num_orders'].sum()
plt.scatter(orders_by_area.index,orders_by_area, c ="blue")
plt.show()
orders_by_area.index

