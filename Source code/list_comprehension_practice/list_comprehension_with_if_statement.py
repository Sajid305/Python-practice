# list comprihension with if statement
# separate odd even numbers from list

# normal way

# list_ = list(range(1,20))
# even = []
# for number in list_:
#     if number%2 == 0:
#         even.append(number)        
# print(even)

# with list comprihension

# numbers = list(range(1,20))
# list_ = [i for i in numbers if i%2 == 0]
# print(list_)

# separate odd number from list
# normal way

# numbers = list(range(1,20))
# list_=[]
# for i in numbers:
#     if i%2 != 0:
#         list_.append(i)    
# print(list_)

# with list comprehension

# numbers = list(range(1,20))
# list_ = [i for i in numbers if i%2 != 0]
# print(list_)

                                # list comprehension exercise

# num to string from a list
# [True, False , [1,2,3], 1, 1.0, 3]

# list_=[False,True, [1,2,3,4,5,6], [1.3,1.5,1.67]]

# def num_to_string(l):
#     return[str(i) for i in l if(type(i) == int or type(i) == float or type(i) == list)]

# print(num_to_string(list_))

                                # list comprehension exercise

# useing if else3 without list comprihension

# number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# output = []
# for i in number:
#     if i%2 == 0:
#         output.append(i*2)
#     else:
#         output.append(-i)
# print(output)


# useing if else with list comprehension

# number = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# output = [i*2 if (i%2 == 0) else(-i) for i in number]
# print(output)
                    