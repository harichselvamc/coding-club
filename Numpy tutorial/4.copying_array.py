import numpy as np
a = np.array([1,2,3,4,5,6])
b = a
print("Original Array",a)
print("So Called Copied Array",b)

b[0] = 100
print("Original Array",a)
print("So Called Copied Array",b) # at ere we didn't copy the original array we just modified the original array so we use copy fuction to copy the original array
#numpy arrays are mutable
c = np.array([1,2,3,4,5,6])
d = c.copy()
print("Original Array",c)
print("Copied Array",d)
c[0]=100
print("After Updating...")
print("Original Array",c)
print("Copied Array",d)