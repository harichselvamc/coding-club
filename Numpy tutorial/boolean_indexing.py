import numpy as np
x = np.array([[11, 51, 2],[23, 24, 5], [16, 47, 8] ,[91, 10, 11]]) 
print(x)
print(x[x>11])
a = np.array([np.nan, 1, 12, np.nan, 3, 41, 54]) 
print(a)
print("After omitting NaN the output array is :")
print (a[~np.isnan(a)])

