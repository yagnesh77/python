d=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
a='#FF0000'

d[:] = [i for i in d if i.get('id') != a ]
print(d)

#or


for i in d:
    if i.get('id')==a:
        del i[0]
print(d)