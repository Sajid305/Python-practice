
    # function
    # list , reverse_str = true
    # list

def function(L,**kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in L]
    else:
        return [name.title() for name in L]
names = ['shajid','rayhan']
print(names)
print(function(names,reverse_str = True)) # this line with **kwargs