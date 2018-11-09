

                                    # OOP Instance Methods practice

class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def fullName(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self): # doing some random practice if person is not above 18 it return false
        return self.age>18

p1 = Person('Shajid','Rayhan',23)

print(p1.fullName())
print(p1.is_above_18())