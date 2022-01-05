import os
fname=input('Enter a file name: ')
s1 =os.path.getsize(fname)
print("the size of "+fname+" is",s1,"bytes")
