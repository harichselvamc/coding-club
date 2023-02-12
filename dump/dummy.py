import numpy as np
# a=np.array([1,2,3])
# print(a)

# print('the itemsize of the array')
# print(a.itemsize)

# print('total size of the array')
# print(a.nbytes)

# print('total number of element present in the array')
# print(a.size)


# print('the type of the array')
# print(a.dtype)

# print('the shape of the array')
# print(a.shape)

# print('the dimension of the array')
# print(a.ndim)

# array_A = np.array([1,2,3],dtype=np.complex128)
# print(array_A.ndim)
# print(array_A.shape)
# print(array_A.size)
# print(array_A.dtype)
# print(array_A.itemsize)
# print(array_A.nbytes)

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# print('two Dimensional arrays : ',a)
# # Get a specific element [rowIndex, columnIndex]
# print('specific element present in the index of 1 and 5 : ',a[1, 5])
# print(a[0,3])
r1=np.repeat(a,5,axis=0)
print(r1)
