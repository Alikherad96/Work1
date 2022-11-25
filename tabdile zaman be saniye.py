print ("tabdile zaman ba format 00:00:00  be saniye ")
print ("baraye kharej shodan exit benvisid ")


while 3>2 :

    a=input("intr ur time")
    if a=="exit" :
        print("az hamrayiye shoma motshakerim")
        break
    else :
        print (a[0:2])
        print (a[3:5])
        print (a[6:8])
        h=int(a[0:2])
        m=int(a[3:5])
        s=int(a[6:8])

    print ("zamane shoma besaniye barabr ast ba:" , (h*3600+m*60+s))



