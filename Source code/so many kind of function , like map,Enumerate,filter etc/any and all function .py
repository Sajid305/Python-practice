
                                            # any and all function

#  finding even number from a list if all of the number
#  is even then we will print true if one of them are odd then we will return false
#  i will do it with the help of all function
 

                                # first with normal way of using all() function

# number1 = [2,4,6,8,10]

# even_number = []
# for num in number1:
#     even_number.append(num % 2 == 0)
# print(all([True,True,True,True,True])) # -----> True
# print(all([True,True,True,False,True])) # ----> if we change value then it will show us false

                         
                                # now with list comprehension of all() function


# number1 = [2,4,6,8,10]

# print(all([num%2==0 for num in number1]))

                                        
                                        # same work with any() function

# number1 = [2,4,6,8,10]
# number2 = [1,3,5,7,9]

# even_number = []
# for num in number2:
#     even_number.append(num%2 == 0)
# print(any(even_number)) # -----------> it will return us flase becuse any one of them is not true as given by condition

 
                                    # now with list comprehension of any() function


# number1 = [2,4,6,8,10]
# print(any([num%2==0 for num in number1]))



                # in this practice we will be make a function that allow us to sum of int 
            # but is there any string present then it will through us a messsg

# def is_int_or_float(*args):

#     if all([(type(arg) == int or type(arg) == float) for arg in args]):

#         total = 0   #------------> this block of code will run when input type is right if not then it will show wrong input
#         for num in args:
#             total += num
#         return total

#     else:
#         return "wrong input type"
        
# print(is_int_or_float(1,2,3,4,5))

