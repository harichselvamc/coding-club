import time
import numpy as np

#python list
list1=[i for i in range(10000000)]
list2=[i for i in range(10000000)]

start= time.time()
multi=[list1[i]*list2[i] for i in range(10000000)]
end=time.time()

print('time taken by list to perform multiplication',(round(end-start),2),'milliseconds')


#numpy array
array1=np.arange(10000000)
array2=np.arange(10000000)
start1=time.time()

numpy_multi=array1*array2
end1=time.time()

print('time taken by numpy to perform multiplication',(round(end1-start1),2),'milliseconds')
