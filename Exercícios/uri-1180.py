tamanho = int(input())
lista = list(map(int, input().split()))

guardar = lista.index(min(lista))


print("Menor valor: " + str(min(lista)) + "\nPosicao: " + str(guardar))
