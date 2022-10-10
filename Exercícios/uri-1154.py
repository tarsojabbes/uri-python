soma = 0
cont = 0
while True:
  atual = int(input())
  if atual > 0:
    soma += atual
    cont += 1
  else:
    break
media = soma / cont
print("%.2f" %media)
