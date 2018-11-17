
                                                        # know how many seconds you have lived in your age #

# print("enter your age if you want to see your age in seconds")
# age = input("enter your age: ")
# age_in_seconds = int(age)*360*24*60*60
# print('you lived for {} seconds in your age'.format(age_in_seconds))

# age = int(input("enter your age: "))
# def seconds_in_life(int_):
#     life_in_seconds = int_*360*24*60*60                   # functional way....
#     return life_in_seconds
# ans = seconds_in_life(age)
# print(f"You have lived {ans} seconds in your life....get a girl hehehe")

# def age_in_seconds():
#     user_age = int(input("enter your age: "))
#     age_seconds = user_age*365*24*60*60                                          # more simplifying way
#     print(age_seconds)
# age_in_seconds()


                                                # another version... :)
def age_program():
    second_or_years = input("enter (s) if you want to convert second in years or enter (y) for years to second ")
    if second_or_years == "s":
        user_input = input("enter the number of second you have lived for: ")
        print(f"you have lived for {int(user_input)/60/60/24/365} years")
    elif second_or_years == "y":
        user_input = input("enter the number of year you have lived for: ")
        print(f"you have lived for {int(user_input)*365*24*60*60} Seconds")
age_program()
