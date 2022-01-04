import os.path,time
filename=input('Enter file name: ')
print(time.ctime(os.path.getmtime(filename)))
print(time.ctime(os.path.getctime(filename)))