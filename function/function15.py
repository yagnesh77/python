s= 'green-red-yellow-black-white'
def hyphen_Sort(s):
    s1=s.split('-')
    s1.sort()
    print('--'.join(s1))

print(hyphen_Sort(s))
