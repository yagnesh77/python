str=input('Enter a string: ')
n=int(input('Enter length: '))
l=str.split(' ')

l1=[]
for i in l:
    if len(i)>=n:

        l1.append(i)
print(l1)




