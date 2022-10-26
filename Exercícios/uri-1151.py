n = int(input())

valor1 = [0]*n

for i in range(0, n):
    if i <= 1:
        valor1[i] = i
    else:
        valor1[i] = valor1[i -1] + valor1[i - 2]

    if i == n -1:
        print('%d'%(valor1[i]), end = ' ')
    else:
        print('%d'%(valor1[i]), end = ' ')

print()   # Contribuicao de Maria Clara Rodrigues em 10/10/2022