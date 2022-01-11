fname=input('Enter file name: ')
with open(fname) as f:
    l=f.readlines()
print(l)