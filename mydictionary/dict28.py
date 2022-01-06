num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
d={}

for i,j in num.items():
    d[i]=sorted(j)
print(d)