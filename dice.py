print("kharej shodan : exit ra type konid")
print("throw dice : space")
import random
while 2 > 1:
    a = input("press space to throw dice : ")
    if a == "exit":
        break
    elif a == " ":
        b = random.randint(1, 6)
        while b == 6:
            print(b)
            b = random.randint(1, 6)
        print(b)

