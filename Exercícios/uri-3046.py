#a soma das idades dos seus três filhos é igual à idade dela.
#dada a idade de dona Mônica e as idades de dois dos filhos, seu programa deve computar e imprimir a idade do filho mais velho.
m = int(input())
a = int(input())
b = int(input())
c = int(m-(a+b))
idades = [a,b,c]
idades.sort()

print(idades[-1])