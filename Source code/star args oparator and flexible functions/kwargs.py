# kwargs (keyword arguments)
# **kwargs (duble star arguments)


# kwargs as a parameter
def function(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")

# function(fist_name = 'shajid', last_name = 'rayhan')
# d = {"first_name":"shajid","last_name":"Rayhan"}
# function(**d) # unpacking dictionary