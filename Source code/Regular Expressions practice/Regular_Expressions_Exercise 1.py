

                                       #   Problem and solution


# role to follow
# [1]---The allowed Character are : alphabets and digits
# [2]---First character should be lower case alphabet only [a to k]
# [3]---The second Character Should be any digit divisible by 3
# [4]---The length of identifire should be at lest 2


                                    #    Solution

import re
 
s=input('enter your strimg : ')

find = re.fullmatch('[a-k][0369][a-zA-Z0-9#]*',s)
if find != None:
    print(s,'your ans is correct')
else:
    print('your ans is wrong')