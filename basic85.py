import os
fname=input('Enter a file name: ')
if os.path.isfile(fname):
    print('Its a file')
elif os.path.isdir(fname):
    print('Its a directory')
else:
    print("it is a special. ")
