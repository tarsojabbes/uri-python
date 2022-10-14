n = 0

cha = input()
resposta = input().split()
corretos = 0

for i in (resposta):
    if resposta[n] == cha:
        corretos += 1
    
    n += 1

print(corretos)
