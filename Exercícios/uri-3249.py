def venceu(batalha):
    if 'CD' in batalha: return False
    return True


n_entradas = int(input())
vitorias = 0

for i in range(n_entradas):
    if venceu(input()): vitorias += 1

print(vitorias)
