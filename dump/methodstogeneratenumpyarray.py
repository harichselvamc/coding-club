#Welcome to this Topic, here we will be discussing how to generate the numpy 
# the first way

#Now  I want to generate a number which is holding consecutive numbers.

#ill be using a range function the function name is arange 

#built in method to generate numpy arrays
import numpy as np
#In this arange function, I would be giving the lower and upper limit of the range of values that I give
a=np.arange(0,10)#printing values from 0 to 10-1
print(a)
b=np.arange(0,20)
print(b)

#Now, for example, I want to bring the values that are not conservative, but that having equal difference
c=np.arange(0,10,2)# start , end , step values
#Basically the first parameter is the start, the second parameter is the end and the third parameter is a step.
print(c)

#The line space function brings a set of numbers that are equally spaced in an endeavour.
d=np.linspace(0,10,2)# third number(2) the total numbers wants to print in the given interval
print(d)

e=np.zeros(5)#generates an array of zeros
print(e)
f=np.ones(5)#generates an array of ones
print(f)

#matrix
g=np.zeros((3,4))#three rows and four column
print(g)

h=np.eye(5)#generates an array of identity matrix
print(h)

i=np.random.rand(4,5)#two dimensional array
print(i)

j=np.random.rand(5)#one dimensional array
print(j)

k=np.random.randint(1,20,2)
print(k)

# The different methods to generate random NumPy arrays are:

# arange() = returns values from the specified range.

# linspace() = returns evenly spaced numbers from the given range.

# ones() = returns an array of ones.

# zeroes() = returns an array of zeroes.

# eye() = returns identity matrix.

# random.rand() = returns an array of random values.

# random.randn() = returns an array of normalized values.

# random.randint = returns an array of integers from a given range.

