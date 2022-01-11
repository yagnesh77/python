fname=input('Enter a file name: ')
with open(fname,'w') as f:
    f.write('yagnesh nayi')
txt = open(fname)
print(txt.read())