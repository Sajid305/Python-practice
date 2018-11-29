



from faker import Faker
from random import *
fake = Faker()
def phonenumbergen():
    d1=randint(0,9)
    d2=str(d1)
    for i in range(9):
        d2=d2+str(randint(0,9))
    return int(d2)


# fake name phone address 
print(fake.phone_number())
print(fake.name())
print(fake.address())
print(fake.email())
