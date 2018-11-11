

#                                    OOP Static method


class Person:
    count_object = 0
    def __init__(self,first_name,last_name,age):
        Person.count_object +=1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def counted(cls):
        return f'you have created {cls.count_object} object'

    def fullName(self):
        return f'{self.first_name} {self.last_name}'

    def is_above_18(self):
        self.age > 18

    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',') # here we have make our one constructor
        return cls(first,last,age)

    @staticmethod # ---> here is we use static method it dose't need any argument
    def hello():
        print('hello Static Method called')


# p1 = Person('shajid','rayhan',23)
# p2 = Person('shjaid','rayhan',25)
# p3 = Person.from_string('shajid ,rayhan,23')
# counted = Person.counted()

# print(p1.counted())
# print(p2.fullName())
# print(p3.fullName())

Person.hello()
