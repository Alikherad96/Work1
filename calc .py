
print("welcome to my clculator")

import math

pi = (math.pi)
print(" + : sum ")
print(" - : sub ")
print(" * : mul ")
print(" / : div ")
print("s : sin")
print("l : log")
print("sq : sqrt")
print("c : cos")
print("t : tan")
print("cot : cot")
print("f : factorial")

while 2 > 1:
    op = input("select ur op : ")
    if op == "exit":
        print("az hamrayiye shoma motshakeram")
        break
    else:
        if op == "+" or op == "-" or op == "*" or op == "/" or op == "s" or op == "l" or op == "sq" or op == "c" or op == "t" or op == "cot" or op == "f":

            a = float(input(" first num :"))
            if op == "+" or op == "-" or op == "*" or op == "/":
               b = float(input("second num :"))

            if op == "+":
                r = a+b
            elif op == "-":
                r = a-b
            elif op == "*":
                r = a*b
            elif op == "/":
                if b == 0:
                    r = ("can't div by 0")
                else:
                    r = a/b
            elif op == "s":
                a1 = (a*pi) / 180
                r = math.sin(a1)
            elif op == "l":
                if a > 0:
                    r = math.log(a,10)
                else:
                    r = ("can't do this")
            elif op == "sq":
                if a >= 0:
                    r = math.sqrt(a)
                else:
                    r = ("can't do this")
            elif op == "c":
                r = math.cos((a*pi) / 180)
            elif op == "t":
                r = math.tan((a*pi) / 180)
            elif op == "cot":
                if a != 0:
                    r = 1 / (math.tan((a * pi) / 180))
                else:
                    r = ("can't do this")
            elif op == "f":
                r = math.factorial(int(a))
            print(r)
        else:
            print("Oh NO")