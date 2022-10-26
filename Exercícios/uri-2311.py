n = int(input())
listNomes = list()
listNotas = list()
for i in range(n):
    listNomes.append(input())
    dific = float(input())
    notas = list(map(float,input().split()))
    notas.sort()
    notas = notas[1:6]
    listNotas.append(sum(notas)*dific)
for i in range(n):
    print("%s %.2f"%(listNomes[i],listNotas[i]))
