d={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
d1={}
for i,j in d.items():
        if j[0] >= 6 and j[1]>= 70:
            d1[i]=list(j)
print(d1)