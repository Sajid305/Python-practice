# can we derive more than one class from base class ? 
# multilevel inheritance 
# method resolution order
# method overriding
# isinstance(), issubclass()
 
 
class Phone: # base class / parent class
    def __init__(self, brand,model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)
     
    def full_name(self):
        return f"{self.brand} {self.model_name}"
     
    def make_a_call(self,number):
        return f"calling {number}...."
 
 
class Smartphone(Phone): # derived / child class
    def __init__(self, brand,model_name, price, ram, internal_memory, rear_camera):
        #two ways
        # Phone.__init__(self,brand,model_name, price) # uncommon way
         
        super().__init__(brand,model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera
     
    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"
 
class FlagshipPhone(Smartphone):
    def __init__(self, brand,model_name, price, ram, internal_memory, rear_camera, front_camera):
        super().__init__(brand,model_name, price, ram, internal_memory, rear_camera)
        self.front_camera = front_camera
     
    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price} and front_camera = {self.front_camera}"
 
 
 
 
 
 
# phone = Phone('nokia', '1100', 1000)
oneplus5 = Smartphone('onePlus', '5', 30000, '6 GB', '64 GB', '20 MP')
oneplus5t = FlagshipPhone('onePlus', '5t', 30000, '6 GB', '64 GB', '20 MP', '16 MP')
# print(oneplus.full_name())
# print(help(FlagshipPhone))
# isinstance 
# print(isinstance(oneplus5, FlagshipPhone))
# print(isinstance(oneplus5t,Phone))
# print(issubclass(FlagshipPhone, Smartphone))