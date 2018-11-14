

                                # inheritance



class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = max(price,0)

    def full_name(self):
        return f'{self.brand} {self.model}'

class Smartphone(Phone):
    def __init__(self,brand,model,price,ram,internal_memory,rear_camra):
        # Phone.__init__(self,brand,model,price) # uncommon way
        super().__init__(brand,model,price) #common way
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camra = rear_camra    

    def all(self):
        return f'{self.brand} {self.model} {self.price} {self.ram} {self.internal_memory} {self.rear_camra}' 





phone1 = Phone('nokia','1110',-1200)
phone2 = Smartphone('oppo','s7',13000,'4gb','64gb','15mg')
print(phone2.ram)
print(phone1.full_name())
print(phone2.all())

