print("tabdile saniye be format hh:mm:ss ")
print("baraye kharej shodan exit benvisid ")


while 3 > 2:

    a = input("inter ur time in second")
    if a == "exit":
        print("az hamrayiye shoma motshakerim")
        break
    else:
        t = int(a)
        h = t // 3600
        m = (t-h*3600)//60
        s = (t-h*3600-m*60)
        print("ur time is",h,":",m,":",s)