d={'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}
min_value=1
result = [k for k, v in d.items() if len(v) == (min_value)]
print(result)