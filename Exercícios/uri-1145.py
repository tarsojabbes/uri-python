entrada = input().split()
qtd_valores = int(entrada[0])
limite = int(entrada[1])

linha = ""
txt = []
contador = 0
for i in range(1 , limite + 1):
    linha += str(i)
    contador += 1
    if contador < qtd_valores and i < limite:
        linha += " "
    else:
        txt.append(linha)
        linha = ""
        contador = 0

for elemento in txt:
    print(elemento)