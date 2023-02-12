import numpy as np
# a=np.arange(1,10)
# print(a)
# #we can search array elements by reference index
# print(a[4])#Show me the element present in the 4th index
# print(a[[0,6,8]])#multiple index WE SHOuld use two square brakets
# print(a[0:5])#zero to fifth index this is array slicing

# #replace  the value in the array 
# a[0]=99
# print(a)
# a[3:7]=76


# a2=np.arange(1,21).reshape(4,5)
# print(a2)


# #boolean functions on array

# block=np.arange(1,21)
# print(block<4)


oneDarray=a = np.array([1,2,3,4,5,6,7])
print('One Dimensional arrays : ', oneDarray)

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print('two Dimensional arrays : ',a)
# Get a specific element [rowIndex, columnIndex]
print('specific element present in the index of 1 and 5 : ',a[1, 5])

# Negative Index
print('negative index of the element: ',a[0,-2]) # if i want 1st row last before element i use negative index

# One Dimensional Array Slicing
print('One Dimensional Array Slicing : ',oneDarray[1:5]) # we can also extract elements from one given index to another given index its called slicing

print(oneDarray[0:])


# 2D array slicing
print('2D array slicing :  ',a[0,1:5])



# Get a specific row 
print('Get a specific row : ',a[0, :])


# Get a specific column
print('Get a specific column : ',a[:, 2])

# Steps [rowStartindex:endindex , columnStartindex:columnEndindex:stepsize]
print(a[0,1:5:2])


a[1,1:5] = 100
print(a)