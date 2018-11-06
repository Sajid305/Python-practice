
                                            # Advance sorted function

fruits = ['grapes', 'mango', 'apple']
fruits.sort()
print(fruits)

fruits = ('grapes', 'mango', 'apple')    #--->sorting tuples
print(sorted(fruits))

fruits = {'grapes', 'mango', 'apple'} # sorting set
print(sorted(fruits))

                       
                                        # using sort in a data structure

 
guitars = [
    {'model': 'yamaha f310', 'price':8400},
    {'model': 'faith naptune', 'price':50000 },
    {'model': 'faith apollo venus', 'price': 35000},
    {'model': 'taylor 814ce', 'price': 450000}
]
 
sorted_value = sorted(guitars,key = lambda item : item['price']) # sorting by price
print(sorted_value)

sorted_value2 = sorted(guitars,key = lambda dict:dict.get('price')) # same just used get method on it
print(sorted_value2)

sorted_value3 = sorted(guitars,key = lambda d:d['price'],reverse = True) # same just used reverse method to reverse price
print(sorted_value3)