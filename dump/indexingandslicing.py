import numpy as np
a=np.arange(1,10)
print(a)
print(a[4])#Show me the element present in the 4th index
print(a[[0,6,8]])#multiple index WE SHOuld use two square brakets
print(a[0:5])#zero to fifth index this is array slicing

#replace  the value in the array 
a[0]=99
print(a)
a[3:7]=76


a2=np.arange(1,21).reshape(4,5)
print(a2)


#boolean functions on array

block=np.arange(1,21)
print(block<4)
