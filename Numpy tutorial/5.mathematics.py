import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a)
#we can add scalar values by simply using +,- like that so on
a=a + 5
print(a)

a=a-5
print(a)

a=a-3
print(a)

a=a*3
print(a)

a=a/2
print(a)

a=a**2
print(a)

b = np.array([2,0,2,0,2,2,0,2,0,2])
print(a + b)

mat1 = np.full((3,3),10)
print(mat1)

mat2 = np.full((3,3), 2)
print(mat2)

# Element wise multiplication
mat1*mat2

# Standard Matrix Multiplication
print(np.matmul(mat1,mat2))


# Take cos
print(np.cos(a))

# Take sin
np.sin(a)


