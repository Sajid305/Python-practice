                                    
                                    

                                                # Generotors
                                            # generators are iterator


def making_generotors(n):
    for i in range(1,n+1):
        yield i #----> yield is for generotors and it save memori and time more then list
                # and yield is a key we can also write it like yield(i)

# print(making_generotors(10)) # --->this is giveing us the type of object

# for number in making_generotors(10): # -----> this line is showing us that generator only call when he calld by need
#     print(number)

# we can not call generator function twich becuse it delete every eliment when it worked is over

number = making_generotors(10)
# print(number)

for num in number:
    print(num)

for num in number:
    print(num)

# this is whay we use generator when we need to call somthing for only once