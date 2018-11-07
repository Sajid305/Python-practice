


                        # Decoretor Exersice 



# first we have to make a decoretor name @calculate_time
# then we will make a functin def func():
#     print('this is function')
 
# then we return this func()
# # and then we will calculate how much time this function take to run


                        # Decoretor Exersice Solution


from functools import wraps
import time

def decoretor(any_function):
    @wraps(any_function)
    def wrapper(*args,**kwargs):
        print(f"Exicuting....{any_function.__name__}")
        t1 = time.time()
        returnd_value = any_function(*args,**kwargs)
        t2 = time.time()
        total = t1-t2
        print(f"this function take {total} seconds")
        return returnd_value
    return wrapper

@decoretor
def square_finder(n):
    return [i**2 for i in range(1,n+1)]
 
square_finder(1000)