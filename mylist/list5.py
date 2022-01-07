l1=['abc', 'xyz', 'aba', '1221',"aa"]
count=0
for i in l1:
    if len(i)>=2:
        if i[0]==i[-1]:
            count+=1
print(count)
