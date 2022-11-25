import random
print("game is rock scissor paper    , for break program : press exit ")
b1 = a1 = 0
while 2 > 1:
    a = input("inter your choice  ( rock or scissor or paper or exit ) ")
    if a == "exit":
        print("hope you enjoy it")
        break
    elif a != "rock" and a != "scissor" and a != "paper":
        print(" please inter correct words")
    else:
        b = random.randint(1, 3)
        if a == "rock":
            if b == 1:
                a1 = a1 + 1
                b1 = b1 + 1
                print("equal")
            elif b == 2:
                a1 = a1 + 1
                print(" you win")
            else:
                b1 = b1 + 1
                print("ha ha computer wins")
        if a == "scissor":
            if b == 2:
                a1 = a1 + 1
                b1 = b1 + 1
                print("equal")
            elif b == 3:
                a1 = a1 + 1
                print(" you win")
            else:
                b1 = b1 + 1
                print("ha ha computer wins")
        if a == "paper":
            if b == 3:
                a1 = a1 + 1
                b1 = b1 + 1
                print("equal")
            elif b == 1:
                a1 = a1 + 1
                print(" you win")
            else:
                b1 = b1 + 1
                print("ha ha computer wins")
        print("computer score is :", b1)
        print("your score is :", a1)
