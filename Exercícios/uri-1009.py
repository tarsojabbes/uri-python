nome = str(input())
fixo = float(input())
vendas = float(input())

salario = (vendas * 0.15) + fixo

print("TOTAL = R$ {:.2f}".format(salario))