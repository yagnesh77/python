d=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
d1=[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
def convert(x):
    result = [dict([a, int(c)] for a, c in b.items()) for b in x]
    return result
def convert1(y):
    result = [dict([a, float(c)] for a, c in b.items()) for b in y]
    return result
print(convert(d))
print(convert1(d1))