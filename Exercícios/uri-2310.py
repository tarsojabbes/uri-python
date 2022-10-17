vezes = int(input())
total_saque = 0
total_bloqueio = 0
total_ataque = 0

saque_certo1 = 0
bloqueio_certo1 = 0
ataque_certo1 = 0

for x in range(0,vezes):
  nome = input()
  saque,bloqueio,ataque = map(int, input().split())
  saque_certo,bloqueio_certo,ataque_certo = map(int, input().split())
  total_saque += saque
  total_bloqueio += bloqueio
  total_ataque += ataque
 
  saque_certo1 += saque_certo
  bloqueio_certo1 += bloqueio_certo
  ataque_certo1 += ataque_certo
 
print("Pontos de Saque: %.2f"%(saque_certo1/total_saque  * 100),"%.")
print("Pontos de Bloqueio: %.2f"%(bloqueio_certo1/total_bloqueio * 100),"%.")
print("Pontos de Ataque: %.2f"%(ataque_certo1/total_ataque * 100),"%.")
