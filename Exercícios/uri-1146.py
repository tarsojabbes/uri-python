x = int(input())

while x != 0:
  sequencia = []
  for i in range(1, x+1):
    sequencia.append(i)

  print(' '.join(map(str, sequencia)))
  x = int(input())