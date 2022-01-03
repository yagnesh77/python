print('Accept two values a and b: ')
a,b=map(int,input().split())
if a%b==0:
    print('a is divisible by b')
elif b%a==0:
    print('b is divisible by a')
else:
    pass