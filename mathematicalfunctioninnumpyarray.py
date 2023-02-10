# now we will be discussing the different methods associated with numpy array, as well as the different array  operations and mathematical functions that can be performed on numpy arrays So moving on, let us consider a number and I will be filling that edit with a different integer.

#let me consider 20 random numbers from zero to hundred
import numpy as np
A=np.random.randint(0,100,20)
print(A)
#to find the shape of the array
print(A.shape)

#im going to reshape the array
print(A.reshape(4,5))
print(A.reshape(2,10))

#transpose of the array
print(A.reshape(4,5).T)#T stands for transpose of the array

b=np.arange(1,20)
print(b)
#multiply the array
#print(b*b)#its shows output as 2nd power of its owm like 2 4 . 3 9, 4 16 like that so
#add,sub so on
print(b-4)

