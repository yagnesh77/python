d=[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
def fetch(l,s):
    result=[a[i] for a in l for i in a.keys() if s==i]
    return result
print(fetch(d,'Math'))
print(fetch(d,'Science'))