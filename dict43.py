s=['S001', 'S002', 'S003', 'S004']
s1=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
s2= [85, 98, 89, 92]
print([{i:{j:k}} for i,j,k in zip(s,s1,s2)])