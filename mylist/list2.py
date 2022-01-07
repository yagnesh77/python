s1 =[7,77,777,1,2]
s2 =1
for i in s1:
    s2*=i
print(s2)

#or using function
def fun(num):
    d1 =1
    for x in num:
        d1 =d1*x
    return d1
print(fun([7,77]))


