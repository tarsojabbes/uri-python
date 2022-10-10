salario = float(input())

if (salario >= 0 and salario <= 400.00):
    reajuste = float(salario * 0.15)
    novo = salario + reajuste
    percentual = 15
elif (salario >= 400.01 and salario <= 800.00):
    reajuste = float(salario * 0.12)
    novo = salario + reajuste
    percentual = 12
elif (salario >= 800.01 and salario <= 1200.00):
    reajuste = float(salario * 0.10)
    novo = salario + reajuste
    percentual = 10
elif (salario >= 1200.01 and salario <= 2000.00):
    reajuste = float(salario * 0.07)
    novo = salario + reajuste
    percentual = 7
elif (salario >= 2000.01):
    reajuste = float(salario * 0.04)
    novo = salario + reajuste
    percentual = 4
print("Novo salario: {:.2f}".format(novo))
print("Reajuste ganho: {:.2f}".format(reajuste))
print("Em percentual: {} %".format(percentual))