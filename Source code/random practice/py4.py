age = int(input("input your age"))
if age==0 or age<=3:
    print("you can't watch this movi")
elif age<10:
    print("free")                               # Different ticket price by age
elif 10<=age<=50:
    print("Tecket price : 150tk")
elif 50<=age:
    print("Ticket price : 250tk")