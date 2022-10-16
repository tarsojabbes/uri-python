x = ''
tabela = {'1': 0,
          '2': 0,
          '3': 0
          }

while x != '4':
    x = input()
    if x in tabela:
        tabela[x] = tabela[x]+1
print("MUITO OBRIGADO")
print("Alcool:", tabela['1'])
print("Gasolina:", tabela['2'])
print("Diesel:", tabela['3'])
