                                    
                                            
                                                #  [1]   multitasking


# Executing several task simultaneously is the concept of multitasking

                                        
                                                # There are 2 types of multitasking

# [1] process based multitasking : Executing several task simultaneously where each task is
#  a seperate independent process

# [2] Thread based multitasking : Executing several task simultaneously
#  where each task is a seperate independent part of same programm and each independent part is called thread

# with multitasking

# [1] we can reduce Execution time and incris performance

# * animation
# * multi media graphics
# video games
# web servers and aplication servrs use this thread base

# gmail is from jboss server


                                                # the ways of creating Theread Example

# [1] : Creating a therad without any class
# [2] : Creating a therad by extending therad class
# [3] : Creating a therad without extending therad class


# [1] creating a therad without any class
import threading
from threading import *

def whoIsthis():
    for i in range(3):   
        print('Executing Therad : child') # it will show that it is executing main therad
c = Thread(target=whoIsthis) # this will make whoIsthis as a child therad
c.start()# now whoIsthis will replace main therad 
# print(whoIsthis())
print('Executing Therad : main_thread')


# [2] : Creating a therad by extending therad class

class MyThread(Thread): # MyThread is child class of Therad
    def run(self):# overwriting
        for i in range(5):
            print('Child Thread')
t=MyThread()
t.start()

print('This is ',current_thread().getName())



# [3] Creating a therad without extending therad class

class Test:
    def another_class(self):
        for i in range(2):
            print('child thread')
obj = Test()
thread2= Thread(target=obj.another_class)
thread2.start()


