s1 = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
d={}
for i,j in s1.items():
    i=i.replace('- ','-')
    d[i]=j
print(d)