l1=[1,7,'yagnesh',(77,777),2,3]
l2=[]
count=0
for i in l1:
    if type(i)!=tuple:
        count+=1
    else:
        print(i)
        break
print(count)
