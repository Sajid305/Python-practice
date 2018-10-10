import random
sic = random.randint(1,20)
for number in range(1,7):
    guse = int(input())
    if guse > sic:
        print("your number is to high")
    elif guse < sic:
        print("your numbe ris to low")                  # number gusesing game  :)
    else:
        break
if guse == sic:
    print("you win")
else:
    print("you loss to much guses i was thinking about " + str(sic) + "you took " + str(guse))