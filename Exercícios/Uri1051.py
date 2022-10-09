salario = float(input())
conta = 0

if salario <= 2000.00:
    print('Isento')
elif salario > 2000.00 and salario <= 3000.00:
    conta = (salario - 2000.0) * 0.08
    print(f'R$ {conta:.2f}')
elif salario > 3000.00 and salario <= 4500.00:
    conta = (salario - 3000.0) * 0.18 + (1000*0.08)
    print(f'R$ {conta:.2f}')
else:
    conta = (salario - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08)
    print(f'R$ {conta:.2f}')
