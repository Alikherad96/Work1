print("inter ur score exam")
print("kharej shodan : exit ra type konid")
s = 0
ii = 0

while 2 > 1:
    score = input("plz inter ur score : ")
    if score == "exit":
        break
    elif float(score) > 20:
        print("plz inter lower than 20")
    else:
        s = float(score)+s
        ii = ii + 1
if ii > 0:
    ave = s/ii
    print("ur ave is :", ave)