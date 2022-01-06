d={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
result=[dict([i,a] for i,j in d.items() for a in j)]
print(result)