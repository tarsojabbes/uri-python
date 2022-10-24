def getNumber(blink):
    bin = blink.replace("*", "1").replace("-", "0")
    return int(bin, 2)
    
for i in range(3):
    sum = 0
    crow = input()
    while(crow != "caw caw"):
        sum += getNumber(crow)
        crow = input()
    
    print(sum)