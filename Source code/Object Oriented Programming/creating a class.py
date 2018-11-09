

                                    
                                        # OBJECT ORIENTED PROGRAMMING 


# COMMON TOPIC IN ALMOST ALL POPULAR PROGRAMMING LANGUAGES(PYTHON, C++, JAVA)
# WITH COMMON IDEA BUT WITH DIFFERENT SYNTAX 
  
# OOP IS JUST A STYLE/WAY TO WRITE A CODE 
 
# VERY HELPFUL IN CREATING REAL WORLD PROGRAMS 
 
# class , object(instance), method
# we are going make a class 
# list class    l = [1,2,3,4,5]
# list object   
# method   l.append(8) in this append is a method

# thing we need to know first to create an class

# OBJECTIVES 
# WHAT IS CLASS 
# HOW TO CREATE AN CLASS 
# WHAT IS INIT METHOD , constructor
# WHAT ARE ATTRIBUTES, INSTANCE VARIABLES
# HOW TO CREATE OUR OBJECT

class Person:                                        # we are definig our class called Person 
    def __init__(self,first_name,last_name,age):     # with a special method called init method    
        # INSTANCE VARIABLES
        print('init method / constructor get called first when every object get called')
        self.first_name = first_name # self represent our object in this case it is self_is_variable1 is our object
        self.last_name = last_name 
        self.age = age

self_is_a_variable1 = Person('shajid','rayhan',23) # this is one object of my person class
self_is_a_variable2 = Person('ahad','rahaman',30) # this is another object of my person class
self_is_a_variable3 = Person('Mehedi','Hasan',25) # this is another object of my person class

print(self_is_a_variable2.first_name) # calling a object when we call a object at first init method get called first

