nome = input()
idade = int(input())

if idade < 5:
    print(f'{nome}, {idade} anos, Não pode competir.')
else:
    pass
if 5 <= idade <= 7:
    print(f'{nome}, {idade} anos, Infantil A.')
else:
    pass

if 8 <=idade <= 10:
    print(f'{nome}, {idade} anos, Infantil B.')
else:
    pass

if 11 <= idade <= 13:
    print(f'{nome}, {idade} anos, Juvenil A.')
else:
    pass

if 14 <= idade <= 17:
    print(f'{nome}, {idade} anos, Juvenil B.')
else:
    pass

if idade > 17:
    print(f'{nome}, {idade} anos, Senior.')