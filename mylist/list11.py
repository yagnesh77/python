s=[1,2,3,4,5]
s1=[1,5,7]
def check(l,l1):
    for x in s:
        for y in s1:
            if x==y:
                return True
                break
            else:
                return False
print(check(s,s1))