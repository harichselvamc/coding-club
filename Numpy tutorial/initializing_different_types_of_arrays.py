import numpy as np
# Creating All Ones 1D array
print(np.ones(5))

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
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis=0)
print(r1)

# Get Array from range of values
evenNumbers= np.arange(10,50,2)
print(evenNumbers)


a = np.array([1,2,3,4,5,6])
b = a
print("Original Array",a)
print("So Called Copied Array",b)

b[0] = 100
print("Original Array",a)
print("So Called Copied Array",b)


c = np.array([1,2,3,4,5,6])
d = c.copy()
print("Original Array",c)
print("Copied Array",d)
c[0]=100
print("After Updating...")
print("Original Array",c)
print("Copied Array",d)

