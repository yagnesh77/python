t1=(1,2,3,4,7,77)
print("before removing:-",t1)
l=list(t1)
l.remove(3)
l.remove(4)
l.remove(2)
t=tuple(l)
print("after removing:-",t)