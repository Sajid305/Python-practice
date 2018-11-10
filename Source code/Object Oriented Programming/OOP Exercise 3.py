



                                        # Object Oriented Programming Exercise 3
# define a class
# Create a object
# count how many object is created


# Solution

class Person:
    count_instance = 0
    def __init__(self,first_name,last_name,age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

count = Person('shajid','rayhan',23)
count2 = Person('shajid','rayhan',23)
count3 = Person('shajid','rayhan',23)
count4 = Person('shajid','rayhan',23)
count5 = Person('shajid','rayhan',23)
print(Person.count_instance)
print(count.first_name)