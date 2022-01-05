a=[15,30,90,60,125,77]
print([i for i in a if i%15==0])
print(list(filter(lambda x:(x%15==0),a)))
