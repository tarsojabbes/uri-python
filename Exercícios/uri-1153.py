n = int(input())

fatorial = n
for i in range(1, n):
  fatorial = fatorial * (n-i)

print(fatorial)