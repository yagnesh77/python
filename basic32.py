n1=abs(int(input('1st number: ')))
n2=abs(int(input('2nd number: ')))
if n1>n2:
    n=n1
else:
    n=n2
while(True):
    if n%n1==0 and n%n2==0:
        print(n)
        break
    else:
        n+=1
