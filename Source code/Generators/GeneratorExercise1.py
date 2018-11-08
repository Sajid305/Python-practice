
# Generator Exercise 1 and solution

# define generator function 
# take one number as argument 
# generate a sequence of even numbers from 1 to that number 
# 5 --> 2,4 
# 7 --> 2,4,6


def generator(n):
    for i in range(1,n+1,2): 
        # if i%2 == 0: # we dont need this line i used step for thet
            yield i

# all_even = generator(14)

# num = generator(20)

for i in generator(20):
    print(i)
