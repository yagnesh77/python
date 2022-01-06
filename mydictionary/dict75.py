d=students = {
  'Theodore': 19,
  'Roxanne': 20,
  'Mathew': 21,
  'Betty': 20
}
l=[]
n=int(input('Enter a key: '))
for i in d:
  if d[i]==n:
    l.append(i)
print(l)