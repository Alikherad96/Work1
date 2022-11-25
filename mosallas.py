print("plz intr 3 zele of mosalas")
print("baraye kharej shodan : exit ")
while 2 > 1:
    aa = input("1st : ")
    if aa == "exit":
        print("hope u enjoy")
        break
    else:

        a = float(aa)
        b = float(input("2nd : "))
        c = float(input("3rd : "))

        if a < b+c and b < a+c and c < a+b:
            print("in mosalas ghabele rasm ast")
        else:
            print("in mosalas niiiiiiiiiiist")