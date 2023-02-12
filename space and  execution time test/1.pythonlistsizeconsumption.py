#python list size consumption
import sys
python_list=[i for i in range(100)]


print(python_list)

print('length of list array : ',len(python_list))

print('type of array : ',type(python_list))

print('memory consumption of elements present in array index 0 : ',sys.getsizeof(python_list[0]))

print('memory usage by the list array: ',sys.getsizeof(python_list[0])*len(python_list))