
                                    
                                    
                                            # OOP Class Method as a Constructor 


# in this programm we going to make our one constructor 


class Person:
    count_object = 0
    def __init__(self,first_name,last_name,age):
        Person.count_object +=1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def counted(cls):
        return f'you have created {cls.count_object}'

    def fullName(self):
        return f'{self.first_name} {self.last_name}'

    def is_above_18(self):
        self.age > 18

  