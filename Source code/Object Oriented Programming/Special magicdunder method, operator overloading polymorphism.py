# # special magic methods / dunder methods
# # operator overloading 
# # polymorphism - method overriding
 
 
# class Phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
     
#     def phone_name(self):
#         return f"{self.brand} {self.model}"
     
#     # str , repr
#     def __str__(self):
#         return f'{self.brand} {self.model} and price is {self.price}'
     
#     def __repr__(self):
#         return f'Phone(\'{self.brand}\', \'{self.model}\', {self.price})'
     
#     def __len__(self):
#         return len(self.phone_name())
     
#     # def __mul__(self, other):
#     #     return self.price * other.price
 
# class SmartPhone(Phone):
#     def __init__(self, brand, model, price, camera):
#         super().__init__(brand,model, price)
#         self.camera = camera
     
#     def phone_name(self):
#         return f"{self.brand} {self.model} and price is {self.price}"
 
#     def __len__(self):
#         return self.price
 
# my_phone = Phone('nokia', '1100', 1000)
# my_phone2 = Phone('nokia', '1600', 1200)
# my_smartphone = SmartPhone('oneplus','5t',33000,'16 MP')
# print(my_smartphone.phone_name())
# print(my_phone.phone_name())
# print(len(my_smartphone))
# print(len(my_phone))

class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = max(price,0)

    def name(self):
        return f'{self.brand} {self.model}'


    def __str__(self):
        return f'{self.brand} {self.model} {self.price}' # for presentetion

    def __repr__(self):
        return f"Phone(\'{self.brand}\'{self.model}\'{self.price}\')" # for devloper


class SmartPhone(Phone):
    def __init__(self,brand,model,price,ram,internal_memory,front_camera):
        super().__init__(brand,model,price)
        


phone1 = Phone('nokia','1100',2000)

print(Phone.__repr__(phone1))