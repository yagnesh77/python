l = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
 (7, 8), (9, 10)]
print(sorted(set().union(*l)))

#or

l1=[]
for i in l:
    for j in i:
        if j in l1:
            pass
        else:
            l1.append(j)
print(l1)