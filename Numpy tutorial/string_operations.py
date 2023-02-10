import numpy as np
print(np.char.lower(['FIRst', 'SeconD']))  
print(np.char.split("first-second",sep ='-')) 
print(np.char.join("," ,"1234567"))
print(np.char.strip("   String with whitespace    "))
#string operations
arr=np.array(['aaaa','aba','bc'])
print(np.char.count(arr,'a'))

arr=np.array(['aa','ab','bc'])

print(np.char.find(arr,'a'))
arr=np.array(['1','2','3','a','2b'])

print(np.char.isnumeric(arr))

arr=np.array(['a',' ','C'])

print(np.char.isspace(arr))

# equal
print(np.char.equal('aa','aa'))

# greater than
print(np.char.greater('abc','aa'))

print(np.char.less('a','aaav'))