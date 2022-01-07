list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']
print('Missing values in first list: ', ','.join(set(list2).difference(set(list1))))
print('Additional values in first list: ', ','.join(set(list1).difference(set(list2))))