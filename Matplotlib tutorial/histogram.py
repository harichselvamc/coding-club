import pandas as pd
import numpy as np

# Importing
import matplotlib.pyplot as plt

df=pd.read_csv('food_data.csv')
print(df.head)

plt.hist(df['base_price'],histtype='bar',color='green',bins=15,edgecolor='red',orientation='vertical') 
plt.xlabel('Base price') 
plt.ylabel('Distinct Orders') 
plt.title('Inspecting Base Price')  
plt.show();

orders_by_center_type = df.groupby(['center_type'])['num_orders'].sum()
print(orders_by_center_type )

plt.bar(orders_by_center_type.index, orders_by_center_type , color ='green',width = 0.2)
plt.show()