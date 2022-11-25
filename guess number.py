import random
print("game : guess my number ( between 1-100 ) /// less than 10 times ha ha ha ")
print("if you press   (exit)  the program will be break out")

a = random.randint(1, 100)
print(a)
b = 2000
i = 0
while b != a and i < 10:
    b = int(input("plz guss a number : "))
    if b > a:
        print("guess a lower number")
    elif b < a:
        print("guess a higher number")
    i = i + 1
print("good job - you guess after", i, "times the number is : ", b)
