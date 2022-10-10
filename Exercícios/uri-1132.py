menor = int(input())
maior = int(input())

if menor > maior:
  menor, maior = maior, menor

soma = 0
for i in range(menor, maior+1):
  if i%13 != 0:
    soma+=i

print(soma)