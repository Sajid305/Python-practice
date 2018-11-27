



                                            # make a mobile number validation regex 

                                            
import re
 
s=input('enter your mobile number : ')
find = re.fullmatch('[0-9]\d{10}',s)
if find != None:
    print(s,'valid mobile number')
else:
    print('Invalid mobile number')

