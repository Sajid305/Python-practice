

                                    # OOP Property and Setter Decorator 

class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self._price = price

    @property
    def complete_specification(self):
        return f"{self.brand} {self.model} and price is {self._price}"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)


b1 = Phone('nokia','1100',1000)
b1.price = -500
print(b1.price)
print(b1.complete_specification)



     