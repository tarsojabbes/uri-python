n = int(input())

for i in range(n):
  [x, y] = input().split()
  x = int(x)
  y = int(y)

  maior = 0
  menor = 0
  
  if(x >= y):
    maior = x
    menor = y
  else:
    maior = y
    menor = x

  soma = 0

  for k in range(menor + 1, maior):
    if(k % 2 != 0):
      soma += k

  print(soma)
  soma = 0