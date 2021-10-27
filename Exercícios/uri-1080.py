maior = 0

for x in range(0, 100):
  n = int(input())
  if n > maior:
    maior = n
    p = x + 1

print(maior)
print(p)
