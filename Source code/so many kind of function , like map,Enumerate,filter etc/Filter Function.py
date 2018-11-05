


                                         # filtering even number from a list using filter function


# number = [1,2,3,4,5,6,7,8,9]
# def is_even(l):
#     return l%2 == 0

# filterd = list(filter(is_even, number))
# print(filterd)

                                                # filter function with lambda 

# number = list(range(1,20))
# filterd = filter(lambda a : a%2==0 ,number)
# filterd = list(filter(lambda a : a%2==0 ,number))
# print(filterd)

# for i in filterd:
#     print(i)


                                                # with list comprehension


# number = list(range(1,30))
# is_odd = [i for i in number if i%2 !=0]
# print(is_odd)