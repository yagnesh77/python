d={"x":10,"y":20}
d1={"a":30,"b":40}
d2=d.copy()
d2.update(d1)
print(d2)

#or

d3={**d,**d1}
print(d3)