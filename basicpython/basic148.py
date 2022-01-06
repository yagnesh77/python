def min_max(y):
    min=y[0]
    max=y[0]
    for i in y:
      if i<min:
        min=i
      elif i>max:
        max=i
    return min,max
y=[]
z=int(input("range :-"))
for j in range(0,z):
    x=int(input(''))
    y.append(x)
print(min_max(y))



