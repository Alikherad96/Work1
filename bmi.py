print("this pro calc ur BMI , hope u enjoy")
print("baraye kharej shodam : exit")

while 2 > 1:
    ww = input("plz enter ur weight in KG : ")
    if ww == "exit":
        print("az hamrayiye shoma motshakeram")
        break
    else:
        w = float(ww)
        h = float(input("plz enter ur height in CM : "))
        bmi = 10000 * w / h ** 2

        if bmi < 18.5:
            print("because ur bmi is lower than 18.5 ! : ur body is underweight : plz eat more fast food")
        elif 25 >= bmi >= 18.5:
            print("because ur bmi is between 18.5 , 25   : ur body is normal : excellent")
        elif 30 > bmi > 25:
            print("because ur bmi is between 25 , 30  () : ur have overweight : eat less bread or potato")
        elif 35 > bmi >= 30:
            print("because ur bmi is between 30 , 35  (()) : u have obesity : eat less bread or potato and fast food")
        else:
            print("because ur bmi is greater than 35   (((((()))))) : u have extreme obesity : eat nothing")
        print("ur bmi is : ", bmi)