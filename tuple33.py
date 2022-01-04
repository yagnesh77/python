t=[(1, 2), (2, 3), (3, 4)]
t1=[(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
l=[]
def convert(l1):
    l.clear()
    for i in l1:
        l.append(list(i))
    return l

print(convert(t))
print(convert(t1))