#lê o numero de testes que vão ser feitos
testes = int(input())

#faz o somatório quantas vezes foram pedidas  
for i in range(testes):
    while True:
        termos = int(input())
        if termos >= 1 and termos <= 1000:
            break
    soma = 0
    for j in range(termos):
        if (j % 2 == 0):
            soma += 1
        elif (j % 2 != 0):
            soma -= 1
    print(soma)
