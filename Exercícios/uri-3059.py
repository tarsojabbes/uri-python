n, i, f = list(map(int, input().split(' ')))
vetor = list(map(int, input().split(' ')))

x = 0

for num1 in range(n):
    y = num1 + 1
    while y != n:
        if i <= vetor[num1] + vetor[y] <= f:
            x += 1
        y += 1

print(x)
