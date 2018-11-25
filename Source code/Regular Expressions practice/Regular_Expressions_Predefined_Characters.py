
import re

# matcher = re.finditer('\s','ab4cd7 @*&5oifd4321')

# for match in matcher:
#     print(f'{match.start()}-----{match.group()}')


matcher = re.finditer('\W','b4cd7 @*&5oifd4321')

for match in matcher:
    print(f'{match.start()}-----{match.group()}')