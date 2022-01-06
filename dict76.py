l=['a', 'b', 'c', 'd', 'e', 'f']
l1=[1, 2, 3, 4, 5]
result=dict([i,j] for i,j in zip(l,l1))
print(result)