

                                        # min and max function

number = [1,2,3,4,5,6,7]
print(min(number))
print(max(number))

name = ['shajid rayhan', 'ahad', 'ab' ,'shaid rayhan talokdar'] # ------> but in this list max function not
                                                                # returning us the true value we need
                                                                 # to solved this problem i have use a function first
def func(item):
    return len(item) #----->now that's working :)
print(max(name, key = func))

                        # but we dont need to define a function becuse we can use lambda function for that


name = ['shajid rayhan', 'ahad', 'ab' ,'shaid rayhan talokdar']
print(max(name,key = lambda item : len(item)))    #--------------> with the help of lambda function :)

                        # and now we are going to use our min and max function in a data structure

# we going to find who got the most score in exam from a list

student = [

        {'name':'shajid','score':20,'age':23},
        {'name':'ahad','score':24,'age':54},
        {'name':'miraj','score':31,'age':26},
        {'name':'fahad','score':17,'age':99}
]
print(max(student,key = lambda item:item.get('score')))  # ---> this will give us a dictionary who get the most number
print(min(student,key = lambda item:item.get('score'))) # ----> min function

# but what if we need to print only the name form this dictionary who get the most number lets make it :)

print(max(student,key = lambda item:item.get('score'))['name']) # -->just added name out side with max function :)

print(min(student,key = lambda item:item.get('score'))['name']) # --> min function

                                            
                                    # another complex practice with min and max function


student2 = {

    'Shajid':{'score':66,'age':24},
    'Rayhan':{'score':25,'age':28},
    'ahad':{'score':34,'age':44},
    'fahad':{'score':38,'age':88}
}

print(max(student2,key = lambda item:student2[item].get('score'))) # ---> using max function

print(min(student2,key = lambda item:student2[item].get('score'))) # ---> min function