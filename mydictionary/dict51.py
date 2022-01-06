d={'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
def update(l):
    l['Math']=[x+1 for x in l['Math']]
    return l
print(update(d))