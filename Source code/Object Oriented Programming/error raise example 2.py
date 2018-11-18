

class Mobile:
    def __init__(self,name):
        self.name = name

class Mobilestore:
    def __init__(self):
        self.mobile = []

    def add_mobile(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobile.append(new_mobile)
        else:
            raise TypeError('new mobile should be object of Mobile class')


mobile1 = Mobile('nokia 1110')
string = 'oppo 11'

is_bad_mobile = Mobilestore()
is_bad_mobile.add_mobile(string)
print(is_bad_mobile.mobile)