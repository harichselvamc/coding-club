import numpy as np
a=np.arange(0,10)
print(a)
b=np.save("d",a)#the file saved in binary format the extension of the file would be .npy


print(np.load("d.npy"))# TO LOAD The file in the formate of binary

c=np.arange(10)
d=np.savetxt("e",c)
f=np.savez("m",c)

# There are different saving formats in NumPy. One can save the NumPy arrays into these different files.

# Like you can use:

# np.savetxt() = to save arrays in csv file.

# np.save() = to save arrays in a binary file.

# np.savez() = to save arrays in a zip file.

