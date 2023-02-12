import numpy as np
# Creating All Ones 1D array
a=np.ones(5)
print(np.dtype)
print(np.ones((5,4),dtype='int32'))

# All 0s matrix
print(np.zeros((2,3)))

# Initialise with any other number
print(np.full((2,2), 60))

# Random decimal numbers
print(np.random.rand())
print(np.random.rand(4,2))


# The identity matrix
print(np.identity(4))

# Repeat an array
a=np.repeat(5,3)
print(a)

arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis=0)#the axis along with the repeated values,by default its flated input array
print(r1)

# Get Array from range of values
evenNumbers= np.arange(10,50,2) # start stop and steps of the arguments

print(evenNumbers)




