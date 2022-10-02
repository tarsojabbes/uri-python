n = int(input())

x = 1000000

for supermercado in range(n):
    p, g = list(map(float, input().split(' ')))
    y = 1000*p/g
    if y < x:
        x = y

print("{:.2f}".format(x))
