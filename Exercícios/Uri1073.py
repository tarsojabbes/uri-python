N = int(input())

#Começar no 2 para ser o primeiro par. é adicionado o +1 para chegar até o número digitado, pois sem ele não iria printar o próprio.
for c in range (2, N+1, 2):
    print(f'{c}^2 = {c ** 2}')
    