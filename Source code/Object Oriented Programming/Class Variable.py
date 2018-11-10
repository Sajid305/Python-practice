

                                    # Class variable

                            # create a programme with classs variable


class Laptop:
    discount_percent = 10 # this is class variable
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def apply_discount(self):# becuse of we diclear class variable that's whay we dont need to apply another argument on this function
        off_price = (Laptop.discount_percent/100)*self.price
        return self.price - off_price

leptop1 = Laptop('Hp',8460,40000)
leptop2 = Laptop('Apple','Macbook Pro',260000)

print(leptop2.apply_discount())


                                    # another programme with class variable



class Circle:
    pi = 3.14 # classs variable
    def __init__(self,radius):
        self.radius = radius
    def cal_circumference(self):
        return 2*Circle.pi*self.radius

Circle1 = Circle(4) # this is taking radius of a circle for class variable pi we dont have to put pi for every circle
Circle2 = Circle(12)

print(Circle1.cal_circumference())


                            # using different class vaiable in different object


class LaptopOne:
    discount = 10
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def apply_discount(self):
        off_price = (self.discount/100)*self.price
        return self.price  - off_price

leptop = LaptopOne('Hp',8460,40000)
print(leptop.__dict__) # this line will show a dict of object that are using different class variable for diferent product
print(leptop.apply_discount())

# using another class variable for different product

LaptopOne.discount = 50 # changeing class variable form 10% to 50% for this product and applying different discount price
leptop3 = LaptopOne('Apple','Macbook pro',230000)
print(leptop3.__dict__)
print(leptop3.apply_discount())