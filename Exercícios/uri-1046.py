input = input().split()

inicioH, fimH, inicioM, fimM = input
inicioH = int(inicioH)
fimH = int(fimH)
inicioM = int(inicioM)
fimM = int(fimM)
total = 0


if inicioH == fimH:
    total += 24
    print(f'O JOGO DUROU {total} HORA(S)')
else:
    if inicioH >= 12:
        ate24 = abs(24 - inicioH)
        if fimH <= 12:
            total = abs(ate24 + fimH)
            print(f'O JOGO DUROU {total} HORA(S)')
        if fimH > 12:
            ate24F = abs(24 - fimH)
            total = abs(ate24 - ate24F)
            print(f'O JOGO DUROU {total} HORA(S)')
    if inicioH < 12:
        if fimH >= 12:
            total = abs(fimH - inicioH)
            print(f'O JOGO DUROU {total} HORA(S)')
        if fimH < 12:
            if fimH < inicioH:
                dif = 24 - (abs(fimH - inicioH))
                print(f'O JOGO DUROU {dif} HORA(S)')
            else:
                total = abs(inicioH - fimH)
                print(f'O JOGO DUROU {total} HORA(S)')
