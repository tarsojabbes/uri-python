interval = float(input())

if 0 <= interval <= 25:
    print(f'Intervalo [0,25]')
elif 25 < interval <= 50:
    print(f'Intervalo (25,50]')
elif 50 < interval <= 75:
    print(f'Intervalo (50,75]')
elif 75 < interval <= 100:
    print(f'Intervalo (75,100]')
else:
    print('Fora de intervalo')

