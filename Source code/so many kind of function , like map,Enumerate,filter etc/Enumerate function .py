                
                
                
                        # We use enumerate function with for loop to track position of our 
                        # item in iterable 
 
 
                                # How we can do this without enumerate function

# name = ['shajid','rayhan','fatema']

# 0 ------> shajid
# 1 ------> rayhan
# 2 ------> fatema

# pos = 0
# for names in name:
#     print(f"{pos} ----> {names}")
#     pos += 1


                                        # with enumerate function 

# name = ['shajid','rayhan','fatema']

# pos = 0
# for pos,i in enumerate(name):
#     print(f"{pos} ----> {i}")



# Define a function that take two arguments 
# 1.) list containing string
# 2.) string that want to find in your list 
# and this function will return the index of string in your list and
# if string is not present then return -1




# def find_pos(l,target):
#     for pos,i in enumerate(l):
#         if i == target:
#             return pos
#     return -1
# print(find_pos(name,"none"))