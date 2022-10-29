testes = int(input())

for i in range(testes):
    teste = input().split()
    qt = 0
    for i in range(int(teste[0])):
        qt += int(teste[i + 1])

    total_aparelhos = qt - (int(teste[0]) - 1)
    print(total_aparelhos)

