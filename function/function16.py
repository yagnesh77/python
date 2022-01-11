def rang(a,b):
    l=[]
    for i in range(a,b+1):
        l.append(i*i)
    return l

print(rang(1,30))