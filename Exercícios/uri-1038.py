input = input().split()
code, amount = input

hotdog = 4
xSalada = 4.5
xBacon = 5
torrada = 2
refrigerante = 1.5

dict = {'1': hotdog, '2': xSalada, '3': xBacon,
        '4': torrada, '5': refrigerante}

total = dict[code] * float(amount)

print(f'Total: R$ {total:.2f}')
