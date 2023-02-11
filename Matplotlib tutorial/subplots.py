
import pandas as pd
import numpy as np

# Importing
import matplotlib.pyplot as plt

df=pd.read_csv('food_data.csv')
print(df.head)
fig,ax=plt.subplots(nrows=1,ncols=3,figsize=(20,5))


fig,ax=plt.subplots(nrows=1,ncols=3,figsize=(20,5))
orders_by_area = df.groupby(['op_area'])['num_orders'].sum()





# Axes 0 
ax[0].scatter(orders_by_area.index,orders_by_area, c ="blue")

# Axes 1
area_by_center = df.groupby(['center_type'])['op_area'].unique()
ax[1].boxplot([x for x in area_by_center],labels=[x for x in area_by_center.index])

# Axes 3
orders_by_center_type = df.groupby(['center_type'])['num_orders'].sum()
ax[2].bar(orders_by_center_type.index, orders_by_center_type , color ='green',width = 0.2)


plt.show()


area_by_center = df.groupby(['center_type'])['op_area'].unique()
area_by_center 
