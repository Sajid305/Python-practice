
class Person:
    count_instance = 0
    def __init__(self,first_name,last_name,age):
        Person.count_instance +=1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    @classmethod
    def count(clse):
        print(f"this take {Person.count_instance} time")

person1 = Person('shajid','rayhan',23)
person2 = Person('shajid','rayhan',23)
person3 = Person('shajid','rayhan',23)
person4 = Person('shajid','rayhan',23)

print(person1.first_name)
print(person1.count())