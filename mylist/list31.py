def cnt(a,b,c):
    ctr = 0
    for i in a:
        if b<=i<=c:
            ctr+=1
    return ctr
list1 = [10,20,30,40,40,40,70,80,99]
list2 = ['a','b','c','d','e','f']
print(cnt(list1,40,80))
print(cnt(list2,'a','b')),