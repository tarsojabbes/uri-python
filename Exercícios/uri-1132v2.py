X = int(input())
Y = int(input())
menor, maior = 0,0
if X > Y:
   maior = X
   menor = Y
else:
   maior = Y
   menor = X
soma = 0
for i in range(menor,maior+1,1):
    if i%13 != 0:
        soma = soma+i
print(soma)
