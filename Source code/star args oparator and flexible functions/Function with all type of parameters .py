# Function With all parameters
# very importent to understand

# p > Parameter
# A > *Args
# D > Defult parameters
# K > keyword arguments or **kwargs
#PADK

def function(name,*args, last_name = "unknown", **kwargs):
    print(name) 
    print(args) 
    print(last_name)
    print(kwargs)
function('shajid',*[1,2,3],a = 1,b = 2,)
