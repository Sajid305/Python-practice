

                                
                                
                                        # Quantifiers


import re 



 
# pattern = re.finditer( 'a','ab4cd7 @*&5oaifds43aa21') # <----- a Exactly one word
# for match in pattern:
#     print(f'{match.start()}........{match.group()}')



# pattern = re.finditer( 'a+','b4cda7 @*&5oifdasa4a321') # <----- a+ atlast one word else none
# for match in pattern:
#     print(f'{match.start()}........{match.group()}')



# pattern = re.finditer( 'a*','ab4cd7 @*&5oaifds43aa21') # <----- a* to find any number of a 
# for match in pattern:
#     print(f'{match.start()}........{match.group()}')



# pattern = re.finditer( 'a?','b4cd7 @*&5oifdas4321') # <----- a? atmost one a or zero number of a 
# for match in pattern:
#     print(f'{match.start()}......{match.group()}')


# pattern = re.finditer( 'a{5}','b4cd7 @*&5oifaaaaad as4321') # <----- Exactly {n} number of a's 
# for match in pattern:
#     print(f'{match.start()}......{match.group()}')



# pattern = re.finditer( 'a{3,5}','b4cd7 @*&5oifdas4321') # a {m,n} Minimum m number of a's and maximum n number of a's
# for match in pattern:
#     print(f'{match.start()}......{match.group()}')



# pattern = re.finditer( 'a{3}a*','b4cd7 @*&5oifdas4321') # after take n number of a then any numebr of a 
# for match in pattern:
#     print(f'{match.start()}......{match.group()}')



# pattern = re.finditer( '^a','ab4cd7 @*&5oifdas4321') # ^a it will check whether the given target string start with a or not 
# for match in pattern:
#     print(f'{match.start()}......{match.group()}')



# pattern = re.finditer( 'a$','ab4cd7 @*&5oifdas4a321a') # a$ to check end with a or not 
# for match in pattern:
#     print(f'{match.start()}......{match.group()}')