from collections import defaultdict
d={'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
d1={'x': 300, 'y': 'Red', 'z': 600}

def test(*d2):
    result= defaultdict(list)
    for e in d2:
        for key in e:
            result[key].append(e[key])
    return dict(result)

print(test(d,d1))