a=int(input('Enter a number: '))
sum=0
a-=1
while a>0 :
    sum+=a**3
    a-=1
print(sum)

#or

for i in range(1,a-1):
    sum+=i**3
print(sum)