import numpy as np

# loadtxt function
filedata = np.loadtxt('data.txt', delimiter=',',dtype='int32')
print(filedata)

filedata = np.loadtxt('incompletefile.txt', delimiter=',',dtype='int32')
print(filedata)

# genfromtxt function

filedata = np.genfromtxt('incompletefile.txt', delimiter=',',filling_values=0)
filedata = filedata.astype('int32')
print(filedata)

# save to csv file

data = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
np.savetxt('data.csv', data, delimiter=',')