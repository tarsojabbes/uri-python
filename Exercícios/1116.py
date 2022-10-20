quantidade = int(input())
resultados = []

for x in range(quantidade):
    dividendo,divisor = input().split(" ")
    dividendo = float(dividendo)
    divisor = float(divisor)
    if (divisor == 0):
        resultados.append("divisao impossivel")
    else:
        divisao = dividendo / divisor
        resultados.append(divisao)

for w in resultados:
    print(w)
