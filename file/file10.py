fname=input('Enter a file name: ')
with open(fname) as f:
    d={}
    for i in f:
        l=i.split()
        for j in l:
          d[j]=d.get(j,0)+1
print(d)