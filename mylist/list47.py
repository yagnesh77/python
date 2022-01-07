color = ['Red', 'Green', 'Black']
color1=[]
for i in color:
    color1.append('c')
    color1.append(i)
print(color1)

#or

color = [v for elt in color for v in ('c', elt)]
print(color)