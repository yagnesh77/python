myDict = {'a':7,'y':77,'c':3,'d':4}
k=input('Enter a key which you ant to remove: ')
del myDict[k]
print(myDict)

#or
print("\n second one")
myDict = {'a':1,'b':2,'c':3,'d':4}
print(myDict)
if 'a' in myDict:
    del myDict['a']
print(myDict)
