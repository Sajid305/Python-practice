

                                                #         Decoretor practice 



from functools import wraps

def decoretor(any_function):
    @wraps(any_function)
    def function(*args,**kwargs):
        if all([type(arg)==int for arg in args]): # we can also use list comprehension for this 
            return any_function(*args,**kwargs)
        else:
            print("un suported data type")
    
    #     data_type = []
    #     for arg in args:
    #         data_type.append(type(arg)==int) # ---> we could use if els for check is thet int or not but this return same thing
    #     if all(data_type):
    #         return any_function(*args,**kwargs)
    #     else:
    #         return "un suported data type"
    return function



@decoretor
def addition(*args):
    total = 0
    for i in args:
        total += i
    return total

print(addition(1,2,3,4,5,6,7,8,9,'adsfsdaf'))
