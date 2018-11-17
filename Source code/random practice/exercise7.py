# exercise
# define a function that takes a number(n)
# return a dictionary containing cube of numbers from 1 to n
 
# example 
# cube_finder(3)
# {1:1, 2:8, 3:27}

#Solution

# def number(n):
#     cubes = {}
#     for i in range(1,n+1):
#         cubes[i] = i**3
#     return cubes

# print(number(11))


def finder(n):
    cubs={}
    for i in range(1,n+1):
        cubs[i]=i**3
    return cubs
print(finder(20))
