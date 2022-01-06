
def avg(s):
    for i in s:
            n1=i.pop('V')
            n2=i.pop('VI')
            i['V+VI']=(n1+n2)/2
    return s
student_details= [
  {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
  {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
  {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
]

print(avg(student_details))