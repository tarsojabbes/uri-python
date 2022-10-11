N = int(input())
for i in range(N):
    valor1, valor2, valor3 = [float(i) for i in input().split()]
    media = (valor1 * 2 + valor2 * 3 + valor3 * 5) / 10
    print(f"{media:.1f}")
