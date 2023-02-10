#memory consuptions by numpy
import numpy as np

numpy_array =np.arange(100)
print(numpy_array)
print('length of numpy array',len(numpy_array))
print('type of array',type(numpy_array))
print('memory consuptions by the element in the numpy array : ',numpy_array.itemsize)
print('memory usage by the element in the numpy array : ',numpy_array.itemsize*numpy_array.size)