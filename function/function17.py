def make_bold(fn):
    return '<b>' + fn +'</b>'
def make_italic(fn):
    return '<i>' + fn + '</i>'
def make_underline(fn):
    return '<u>' + fn + '</u>'
s='Hello World'
print(make_bold(s))
print(make_underline(s))
print(make_italic(s))