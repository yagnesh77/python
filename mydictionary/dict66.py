d=[{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
def test(d,s,s1):
    if any(i[s]==s1 for i in d):
        return True
    else:
        return False
print(test(d,'student_id', 1))
print(test(d,'name', 'Brian Howell'))
print(test(d,'class', 'VII'))
print(test(d,'class', 'I'))
print(test(d,'name', 'Brian Howelll'))
print(test(d,'student_id', 11))