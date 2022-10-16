inter = 0
gremio = 0
empates = 0
grenais = 0
while True:
    gols_inter, gols_gremio = [int(i) for i in input().split()]
    grenais += 1
    if gols_inter > gols_gremio:
        inter += 1
    elif gols_inter < gols_gremio:
        gremio += 1
    else:
        empates += 1
    repeticao = int(input("Novo grenal (1-sim 2-nao)\n"))
    if repeticao == 2:
        break
print(f'''{grenais} grenais
Inter:{inter}
Gremio:{gremio}
Empates:{empates}''')
if inter > gremio:
    print("Inter venceu mais")
elif inter < gremio:
    print("Inter venceu mais")
else:
    print("Nao houve vencedor")
