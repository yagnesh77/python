n1=abs(int(input('1st number: ')))
n2=abs(int(input('2nd number: ')))
if n1>n2:
    n=n2
else:
    n=n1
while(True):
    if n1%n==0 and n2%n==0:
        print(n)
        break
    else:
        n-=1