l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
def even(l):
    for i in l:
        if i%2!=0:
            l.remove(i)
    return l
print(even(l))