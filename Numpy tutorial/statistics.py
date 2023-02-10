# Statistics

## mean - returns the mean of all the element in the ndarray

## min - returns the minimum element in the ndarray

## max - returns the maximum element in the ndarray

## sum - returns the sum of the elements in the ndarray

## prod - returns the product of the elements in the ndarray

## std - returns the standard deviation of the elements in the ndarray.

## var - returns the variance of the elements in the ndarray.
import numpy as np
stats = np.array([[1,2,3,4,5],[4,5,6,7,8]])
print('The element in the array: ',stats)
print('The mean value of te array ',np.mean(stats))
print('this the minimum element in the array',np.min(stats))
print(np.max(stats, axis=1))
print('this the maximum element in the array',np.max(stats))
print('This the sum element in the array',np.sum(stats))
print(np.sum(stats, axis=0))
print('this the product  of element in the array',np.prod(stats))
print('this the standard of element in the array',np.std(stats))
print('this the varience of element in the array',np.var(stats))