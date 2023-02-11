#   readings from files 
import pandas as pd
df=pd.read_csv('fruits_data.csv')
print(df)


df=pd.read_csv('fruits_data.csv',index_col=0)
print(df)

#reading data from json

df=pd.read_json('fruits_data.json')
print(df)


#saving to a csv,json
df.to_csv('new_purchases.csv')

df.to_json('new_purchases.json')




