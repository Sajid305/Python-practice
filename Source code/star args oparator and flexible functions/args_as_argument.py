
                                    # args_as_argument

def multiply_num(*args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

list_ = [1,2,3,4] # here i use this args list as argument
# print(multiply_num(1,2,3,4))
print(multiply_num(*list_))   # this * will unpack theis list