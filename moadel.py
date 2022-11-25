name = input("plz inter ur name :")
print("baraye kharej shodan : exit ")
while 2 > 1:
    if name == "exit":
        break
    else:
        a = float(input("plz inter ur 1st number : "))
        b = float(input("plz inter ur 2nd number : "))
        c = float(input("plz inter ur 3rd number : "))
    if a > 20 or b > 20 or c > 20:
        print("plz inter correct scores")
    else:
        av = (a+b+c)/3
        if av >= 17:
            print(name, " u r a great std and ur ave scores is : ", av)
        elif av >= 12:
            print(name, " : u r a normal std and ur ave scores is :", av)
        else:
            print(name, " : sorry u r failed becuse ur ave scores is :", av)
