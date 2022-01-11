fname=input('Enter a file name: ')
with open(fname) as f:
    a=[]
    for i in f:
        a.append(i)
print(a)