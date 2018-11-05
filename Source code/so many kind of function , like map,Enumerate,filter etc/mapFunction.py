                                                  
                                                  
                                                    # Map function



# number = [1,2,3,4]

# def square(a):                # if we use lambda function then we dont need to define this square function
#     return a**2
# ans = list(map(square,number))
# print(ans)

                            # with lambda function

# square = list(map(lambda a : a**2, number))
# print(square)

                            # with list comprehension

# square_new = [i**2 for i in number]
# print(square_new)

                                        # without lambda map and list comprehension

# number = [1,2,3,4]
# def square(n):
#     return n**2

# new_list = []

# for i in number:
#     new_list.append(square(i))
# print(new_list)


                                        # checking length of a list

# name = ['shajid','rayhan','talokdar']
# length = map(len,name)                    # we can loop only one time in map function but if we convert it into a list then we can use loop savarel time
# for i in length:
#     print(i)

# name = ['shajid','rayhan','talokdar']
# length = list(map(len,name))
# for l in length:
#     print(l)