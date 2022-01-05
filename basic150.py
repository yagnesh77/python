def prod_check(num):
    for i in range(len(num)):
        for j in range(len(num)):
            product=num[i]*num[j]
            if product%2!=0:
                return True
            else:
                return False
c=[1,3,5,6,4,15,19,21,50,27]
d=[2,4,6,8]
print(prod_check(c))
print(prod_check(d))