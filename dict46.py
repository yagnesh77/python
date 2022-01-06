d=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d1={}
for i,j in d:
    d1.setdefault(i, []).append(j)
print(d1)
