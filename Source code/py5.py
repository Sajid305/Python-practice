import random
sicnumber = random.randint(1, 20)
for number in range(1,7):
    guse_number = int(input("inter your number"))
    if guse_number < sicnumber:
        print("your number is to low")
    elif guse_number > sicnumber:
        print("your number is to high")
    else:
        break
if guse_number == sicnumber:
    print("you win")
else:
    print(f"you loos you took {number}  guses i was thinking about {sicnumber}")
