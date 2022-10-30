# Universidade Federal de Campina Grande
# Ciência da Computação - Programação 1
# Vitória Maria do Nascimento - 2021.2
# vitoria.nascimento.ccc.edu.ufcg
# Questão: "Menores das Triplas" - Unidade: 4

def calcula_menor(triplas):
    triplas = triplas.split()
    menor = 0
    lista = []
    for i in range(len(triplas)):
        if int(triplas[i]) <= int(triplas[menor]):
            menor = i
        lista.append(triplas[menor])
    return lista


def calcula_media_menores(lista):
    media = 0
    for ele in lista:
        media += int(ele)

    media = media / len(lista)
    menor_de_todos = menor
    return media


def analisa_se_iguais(triplas):
    for num in triplas:
        if num == triplas[0]:
            return True
        else:
            return False


def main():

    while True:
        triplas = input()
        if triplas == 'fim': break
        else:
            lista = calcula_menor(triplas)
        if analisa_se_iguais(triplas) == True:
            media = 'nada'
            menor_entre_menores = 'nada'
            maior_entre_menores = 'nada'
            break

    media = calcula_media_menores(lista)

    print(f'Média dos menores: {media:.2f}')
    print(f'Menor entre os menores: {menor_entre_menores}')
    print(f'Maior entre os menores: {maior_entre_menores}')

if __name__ == '__main__':
    main()