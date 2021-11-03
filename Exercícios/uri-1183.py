arr = []

option = input()

for i in range(12):
    arr.append([])

for i in range(0, 12):
    for j in range(0, 12):
        value = input()
        arr[i].append(float(value))

soma = 0
iteracoes = 0
for i in range(0, 12):
    for j in range(i + 1, 12):
        soma = soma + float(arr[i][j])
        iteracoes += 1

media = soma/iteracoes
if option == 'S':
    print(f'{soma:.1f}')
if option == 'M':
    print(f'{media:.1f}')
