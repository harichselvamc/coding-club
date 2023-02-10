import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)

new3Darr = arr.reshape(2, 3, 2)

print(new3Darr)

newarr = arr.reshape(4,4)

print(newarr)

newarr=arr.reshape(4,-1)
print(newarr)

newarr=arr.reshape(2,-1,-1)
print(newarr)

# Vertically stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack([v1,v2,v1,v2]))

# Horizontal  stack
h1 = np.ones((2,4))
h2 = np.zeros((2,2))
print(h1)
print(h2)
print(np.hstack((h1,h2)))
