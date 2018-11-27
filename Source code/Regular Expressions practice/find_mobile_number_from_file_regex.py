

                            
                                #  find all valid mobile number from text file


import re

f1 = open('input.txt','r')
f2 = open('output.txt','w')

for line in f1:
    list = re.findall('[0-1]\d{10}',line)
    for number in list:
        f2.write(number+'\n')
print('Extracted all phone number')
f1.close()
f2.close()