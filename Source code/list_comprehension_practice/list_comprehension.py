# list comprehension 
# with the help of list comprehension we can create of list in one line
#  
# create a list of squares from 1 to 10 normal way.

# squares = []
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)

# create a list of squares from 1 to 10 list comprehension

# squares = [i**2 for i in range(1,11)]
# print(squares)

#   another list comprehension example

# negative = []
# for i in range(1,11):
#     negative.append(-i)
# print(negative)

# with list comprehension

# negative = [-i for i in range(1,11)]
# print(negative)

# another example

# name = ['MD','Shajid','Rayhan']
# name2 = []
# for car in name:
#     name2.append(car[0])
# print(name2)

# with list comprehension

# name = ['MD','Shajid','Rayhan']
# name2 = [i[0] for i in name]
# print(name2)