d={'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
r=[i for i in d.values()]
r.sort(reverse=True)
result=[i for i in d if d[i]==r[-1] or d[i]==r[0]][::-1]
print(result)