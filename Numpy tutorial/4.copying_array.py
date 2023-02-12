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