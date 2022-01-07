l1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
l1.pop(0)
l1.pop(4)
del l1[-1]
print(l1)


#or
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)
