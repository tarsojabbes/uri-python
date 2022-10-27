x = 1
while x == 1:
    a = float(input())
    while a < 0 or a > 10:
        print('nota invalida')
        a = float(input())
    b = float(input())
    while b < 0 or b > 10:
        print('nota invalida')
        b = float(input())
    print("media = {:.2f}".format((a+b)/2))
    print("novo calculo (1-sim 2-nao)")
    x = int(input())
    while x != 1 and x != 2:
        print("novo calculo (1-sim 2-nao)")
        x = int(input())
