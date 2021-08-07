numeros = input().split()

novoArray = []
for numero in numeros:
    novoArray.append(int(numero))

novoArray.sort(reverse=True)

print(f'{novoArray[0]} eh o maior')
