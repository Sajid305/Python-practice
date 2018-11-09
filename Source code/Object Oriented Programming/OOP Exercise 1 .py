

                                        # OOP Exercice 1

# Create a laptop class with attributes like brand name , model name , price 
# create two objects/instance of your laptop class 

class Leptop:
    def __init__(self,brand_name,model_number,price):
        # instance variables
        self.brand_name = brand_name
        self.model_name = model_number
        self.price = price

corI5 = Leptop('Hp',8460,30000)
corI7 = Leptop('Dell',2432,34000)


# print(f'Brand is {corI5.brand_name}')
print(f'Model is {corI5.model_name}')
print(f'Price is {corI5.price} taka')



     
    
 
     
 
 