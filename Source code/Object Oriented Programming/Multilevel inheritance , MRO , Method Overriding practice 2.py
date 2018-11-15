
class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price =max(price,0)
   
    def fullname(self):
        return f'{self.brand} {self.model}'


class Smartphone(Phone):
    def __init__(self,brand,model,price,ram,internal_memory,front_camera):
        super().__init__(brand,model,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.front_camera = front_camera

    def smartphone(self):
        return f'{self.brand} {self.model} {self.price} {self.ram} {self.internal_memory}'

class Iphone(Smartphone):
    def __init__(self,brand,model,price,ram,internal_memory,front_camera,sensor,face_recognation):
        super().__init__(brand,model,price,ram,internal_memory,front_camera)
        self.sensor = sensor
        self.face_recognation = face_recognation

    def iphone(self):
        return f'{self.brand} {self.model} {self.price} {self.sensor} {self.face_recognation}'

    def call(self,number):
        return f'calling from {self.brand} {self.model} to this number {self.number}'


phone1 = Phone('Nokia','1110',1000)
smartphone1 = Smartphone('samsung','j1',6990,'4gb','5mp','10mp')
iphone1 = Iphone('Iphone','X',120000,'4gb','8gb','20mp','14s','Shajid')
print(iphone1.fullname())
print(help(Iphone))