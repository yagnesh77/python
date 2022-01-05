d= {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
print(sorted(d.items(),key = lambda x:x[1],reverse=True)[:3])

