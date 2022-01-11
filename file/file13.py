from shutil import copyfile
fname='file1.py'
fname1='file2.py'
copyfile(fname,fname1)
a=open(fname1)
print(a.read())