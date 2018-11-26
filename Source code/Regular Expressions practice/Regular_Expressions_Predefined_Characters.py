


                               # :::Predefined Character Classes:::


import re



# matcher = re.finditer('\s','ab4cd7 @*&5oifd4321') #   <----------space character

# for match in matcher:
#     print(f'{match.start()}-----{match.group()}')




# <--------------\S-------------> Except space character


# matcher = re.finditer('\S','b4cd7 @*&5oifd4321')

# for match in matcher:
#     print(f'{match.start()}-----{match.group()}')


#<----------------\d-------------> [0-9] any digit


# matcher = re.finditer('\d','b4cd7 @*&5oifd4321')

# for match in matcher:
#     print(f'{match.start()}-----{match.group()}')


#<----------------\D-------------> Except digit


# matcher = re.finditer('\D','b4cd7 @*&5oifd4321')

# for match in matcher:
#     print(f'{match.start()}-----{match.group()}')

#<----------------\w-------------> Any word character(alpha numerick)

# matcher = re.finditer('\w','b4cd7 @*&5oifd4321')

# for match in matcher:
#     print(f'{match.start()}-----{match.group()}')


#<----------------\W-------------> Any character Except word(specialchar) 

# matcher = re.finditer('\W','b4cd7 @*&5oifd4321')

# for match in matcher:
#     print(f'{match.start()}-----{match.group()}')

#<----------------([ . ])-------------> Every character 


# matcher = re.finditer('.','b4cd7 @*&5oifd4321')

# for match in matcher:
#     print(f'{match.start()}-----{match.group()}')