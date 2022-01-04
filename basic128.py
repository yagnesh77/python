str=input('Enter a string: ')
if str.islower():
    print('Lower letter exists')
else:
    print('Not letter exists')

    #or

print()
str1 = 'A8238i823acdeOUEI'
print(any(c.islower() for c in str1))
