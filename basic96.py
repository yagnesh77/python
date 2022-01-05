import traceback
def first():
    print('first')
    return second()
def second():
    print('second')
    traceback.print_stack()
first()