n = int(input())
for i in range(n):
    m = int(input())
    produtos = dict()
    for j in range(m):
        produto,preco = input().split()
        produtos[produto] = float(preco)

    p = int(input())
    soma = 0
    for k in range(p):
        produto,quantidade = input().split()
        soma += produtos[produto] * int(quantidade)
    print(f"R$ {soma:.2f}")

