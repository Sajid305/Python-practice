    
    
        
            # Decoretor with argument and nested Decoretor this decoretor will only take string as argument

from functools import wraps

def only_string_alow(data_type): # ----> this decoretor made for only take str as argument
    def nested_decoretor(any_function):# ----> this decoretor is for taking function
        @wraps(any_function)
        def wrapper(*args,**kwargs):
            if all([type(arg)== data_type for arg in args]):
                return any_function(*args,**kwargs)
            print('only string alowed')
        return wrapper
    return nested_decoretor

@only_string_alow(str) 
def string_join(*args): # --> this function one or more argument and joind them together
    joind = ''
    for i in args:
        joind += i
    return joind

var = string_join('shajid',' rayhan') # --> if we pass a int on this this will return out else message
print(var)














