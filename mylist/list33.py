from itertools import combinations
l1 = [10, 20, 30, 40]
subs=[]
for i in range(0, len(l1)+1):
    temp = [list(x) for x in combinations(l1, i)]
    if len(temp) > 0:
        subs.extend(temp)
print(subs)