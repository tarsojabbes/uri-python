value = float(input())

if 0 <= value <= 25:
    print('Intervalo [0,25]')
if 25 < value <= 50:
    print('Intervalo (25,50]')
if 50 < value <= 75:
    print('Intervalo (50,75]')
if 75 < value <= 100:
    print('Intervalo (75,100]')
if value < 0 or value > 100:
    print('Fora de intervalo')
