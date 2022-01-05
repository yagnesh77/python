class dictObj(object):
    def __init__(self):
        self.x = "yagnesh"
        self.y = 'nayi'


    def do_nothing(self):
        pass


test = dictObj()
print(test.__dict__)
