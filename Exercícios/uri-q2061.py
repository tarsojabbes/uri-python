contador = 0
entrada = input().split()

N = int(entrada[0]) #Nº de abas abertas
M = int(entrada[1]) #Nº de ações

while contador < M:
    acao = input()
    
    if acao == "fechou":
        N += 1
    elif acao == "clicou":
        N -= 1
    
    contador += 1

print(N)
