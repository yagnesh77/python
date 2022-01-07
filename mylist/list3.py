s1 =[1,2,3,4,5,77,777]
print(max(s1))
#or using function

def num(d1):
    a=[]
    max=0
    for i in range(d1):
        n=int(input('Enter value: '))
        if max<n:
           max=n
    a.append(max)
    return a
print(num(5))
