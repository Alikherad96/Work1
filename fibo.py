print("kharej shodan : exit ra type konid")

while 2 > 1:
    nn = input("plz inter ur int number we calc fibo(ur number): ")
    a = str(1)
    if nn == "exit":
        break
    elif float(nn) <= 0:
        print("plz inter upper than 0")
    elif int(nn) == 1:
        print("1")

    else:
        n = int(nn)
        fib = 1
        fib1 = 1
        fib2 = 1
        for i in range(n-2):

            a = a +"," + str(fib2+fib1)
            fib = fib1 + fib2
            fib2 = fib1
            fib1 = fib
        print("1", a)