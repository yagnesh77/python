d={'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
total=0
for i in d.values():
    total+=len(i)
print(total)