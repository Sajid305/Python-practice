# in keyword in sets and for loop
 
s = {'a', 'b', 'c','d'}
 
# in keyword to check if item is present or not in set
if 'a && d' in s:
    print("present those letter")
else:
    print("not present yet")
 
# for loop 
for item in s:
    print(item)
 
s1 = {1,2,3,4}
s2 = {3,4,5,6}
 
# union 
# intersection
 
# {1,2,3,4,5,6}
# | <--- pipe
# union_set = s1 | s2
# print(union_set)
# &
print(s1 & s2)
