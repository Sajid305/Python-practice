

                            # Define a function take any number of lists containing number 

     # [1,2,3] , [4,5,6], [7,8,9]

     # return average 
                                        
     # (1+4+7)/3 , (2,5,8)/3 , (3,6,9)/3 


# l1 =  list(range(1,5))
# l2 =  list(range(5,11))
# l3 =  list(range(11,21))
# def average_finder(*args):
#     avarage = []
#     for pair in zip(*args):                       # this will unpack thos list
#         avarage.append(sum(pair)/len(pair))
#     return avarage

# print(average_finder(l1,l2,l3))


                            # trying to make this anonymous function in one line using lambda 😃😃


# l1 =  list(range(1,5))
# l2 =  list(range(5,11))
# l3 =  list(range(11,21))

# # with lambda function
# avarege = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]

# print(avarege(l1,l2,l3))