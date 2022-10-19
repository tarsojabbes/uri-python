hora1, minuto1, hora2, minuto2 = [int(x) for x in input().split()]
if hora1 == hora2 and minuto1 == minuto2:
    horaf = 24
    minutof = 0
else:
    if minuto1 > minuto2:
        minuto2 += 60
        hora2 = hora2 - 1
    if hora1 > hora2:
        hora2 += 24
    horaf = hora2 - hora1
    minutof = minuto2 - minuto1

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horaf,minutof))