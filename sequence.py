import random
simon = []

def add_to_sequence(nice):
    nice.append(random.randint(0 , 3))

def display_sequence(nice):
    me = " "
    for x in nice:
        if x == 0:
            me = "red"
            print(me)
        elif x == 1:
            me = "green"
            print(me)
        elif x == 2:
            me = "Yellow"
            print(me)
        else:
            me = "Blue"
            print(me)
while True:
    choice = input(" 1 : Add to Sequence "
                "2 : Display Sequence "
                "3 : Exit Program ")
    print("")
    if choice.lower() == "1":
        add_to_sequence(simon)
    elif choice.lower() == "2":
        display_sequence(simon)
    elif choice.lower() == "3":
        print("Bye")
        break
    else:
        print("Invalid Input")
