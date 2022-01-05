l = [("x", 7), ("x", 77), ("x", 777), ("y", 1), ("y", 2), ("z", 1)]
d = {}
for a, b in l:
    d.setdefault(a, []).append(b)
print (d)
