d={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
d1={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
def length(l):
    result= dict([i,len(i)] for i in l.values())
    return result

print(length(d))
print(length(d1))