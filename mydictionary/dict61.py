d={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
d1={}
for i in d.values():
    d1[i]=d1.get(i,0)+1
print(d1)