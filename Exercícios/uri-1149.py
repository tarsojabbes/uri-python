entrada = input().split()
A, N = int(entrada[0]), int(entrada[-1])
soma = 0
for i in range(N):
    soma += A + i
print(soma)
