
                            
                                    # OOP Exercise
                            # create a programme that apply discount 

class Laptop:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def apply_discount(self,num):
        off_price = (num/100)*self.price
        return self.price - off_price

CorI5 = Laptop('Hp','8460',40000)
CorI7 = Laptop('Apple','Macbook pro',230000)

print(CorI7.apply_discount(20))
print(CorI5.apply_discount(10)) # returning discounted price
