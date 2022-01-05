Data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
s=set()
for v in Data:
    for value in v.values():
        if value not in s:
            s.add(value)
print(s)