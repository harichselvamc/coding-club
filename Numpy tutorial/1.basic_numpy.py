import numpy as np
a=np.array([1,2,3]) #one-dimensional array
print(a)
b=np.array([4,5,6],dtype=np.int32) #one-dimensional array
print(b)
c=np.array([[1,2,3],[4,5,6]]) # by adding list of lists we can convert to 2nd array.
print(c)

#get dimensions of the array
print('the dimension of the array')
print(a.ndim)
print(b.ndim)
print(c.ndim)


#get shape of the array
print('the shape of the array')
print(a.shape)
print(b.shape)
print('rows and columns',c.shape)

#get type of the array
print('the type of the array')
print(a.dtype)
print(b.dtype)
print(c.dtype)

#get size of the array #int=4,float64=8,complex128=16
print('the size of the array')
print(a.itemsize)
print(b.itemsize)
print(c.itemsize)

#get total size of the array
print('total size of the array')
print(a.nbytes)
print(b.nbytes)
print(c.nbytes)

#get total number of elements in the array
print('total number of element present in the array')
print(a.size)
print(b.size)
print(c.size)



