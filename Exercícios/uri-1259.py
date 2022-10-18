n = int(input())
v = [int(input()) for x in range(n)]
pares = [x for x in v if x%2 == 0]
impares = [x for x in v if x%2!=0]
for par in sorted(pares):
    print(par)
for impar in sorted(impares, reverse=True):
    print(impar)
