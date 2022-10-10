idade = int(input())

ano = idade // 365
mes = (idade % 365) // 30
dia = ((idade % 365) % 30)

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')

