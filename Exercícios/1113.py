while True:
    valores = [int(i) for i in input().split()]
    x, y = valores
    if x == y:
        break
    elif x > y:
        print('Decrescente')
    else:
        print('Crescente')