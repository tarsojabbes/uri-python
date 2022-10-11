#lê a entrada e separa os elementos em uma lista
lista_regua = input().split(' ')

#converte os elementos da lista de string para int
lista_regua = [int(i) for i in lista_regua]

#imprime o número de tomadas disponíveis ao final 
print(sum(lista_regua) - 3)
