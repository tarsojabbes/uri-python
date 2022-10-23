nome = str(input())
fixo = float(input())
vendas = float(input())

salario = (vendas * 0.15) + fixo

print("TOTAL = R$ {:.2f}".format(salario))

# Neste comentario, mais outra maneira de resolver a questao, 
# mudando apenas a forma de imprimir o resultado. Por Maria
# Clara Rodrigues:

# nome = str(input())
# salarioFixo = float(input())
# numVendas = float(input())

# salarioTotal = salarioFixo + (numVendas * 0.15)

# print("TOTAL = R$ %0.2f" % salarioTotal)