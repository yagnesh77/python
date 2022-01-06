d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
keys = d.keys()
vals = zip(*[d[k] for k in keys])
result = [dict(zip(keys, v)) for v in vals]
print(result)