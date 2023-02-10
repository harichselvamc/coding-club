#now we will be discussing some more functions that are associated with numpy arrays
#LET ME Create new array

import numpy as np
a=np.arange(1,10)

print(a)

print(np.sqrt(a))#sqrt sqare root of the array

b=np.random.randint(1,100,20)
print(b)
print(np.max(b))#max to find the largest number present in the array

#So moving on, if we can find the maximum number one that, isn't it obvious that there will be a minimum function.

print(np.min(b))#min to find the smallest number present in the array

print(np.argmax(b))#max to find the largest number index place  in the array
print(np.argmin(b))#min to find the smallest number index place in the array


#So now the functions that we're discussing will be not only in mathematics, for example, finding sign,although, of course of a given number.So moving on your full discourse about the log function.NoW, consider.I want to find the log value of each and every element that is present in my area.

print(np.log(b))


#same as through for sign value
print(np.sin(b))

#also for tan 
print(np.tan(b))





c=np.random.randn(3,4)#two dimensional array
print(c)



#OK, you know, if I want to round off all the elements that are present in this matrix to see a second decimal place up to go decimals, or if I want to run this all up to two decimals, in that case, I can simply use round function.


print(np.round(c, decimals=3)) #And the second parameter would be the decimals of two, which I want to do each and every number that is already I'll be putting decimals equal to see. I want to run this up to three decimal places and put three has the value and on this.OK, so you can see I have rounded the values that are present in this, adding up to three decimal


print(c.dtype) #this is used to find the data type of the array  , float64 means decimal valus so i got float

# Mathematical Functions
# So by now, you must have experimented with different functions taught in the course. Consider an array, then the functions are:

# array-10  = to subtract from elements in the array.

# np.sqrt(array) = to find the square root of elements in the array.

# np.min(array) = to find the minimum number from the array.

# np.argmin(array) = to find an index of the minimum number from the array.

# np.log(array) = to find log values of elements in the array.

# np.sin(array) = to find sin values of elements in the array.

# np.tan(array) = to find tan values of elements in the array.

# np.round(array , decimals = 2) = to round off elements up to two decimals in the array.