L = int(input())
T = input()

M = []
vetor_auxiliar_para_a_matriz = []

for i in range(144):
	valor = float(input())
	vetor_auxiliar_para_a_matriz.append(valor)

	if len(vetor_auxiliar_para_a_matriz) == 12:
		M.append(vetor_auxiliar_para_a_matriz)
		vetor_auxiliar_para_a_matriz = []

if T == "S":
	soma_da_linha = 0
	for i in range(12):
		soma_da_linha += M[L][i]
		
	print("{:.1f}".format(soma_da_linha))

else:
	soma_da_linha = 0
	media_da_linha = 0
		
	for i in range(12):
		soma_da_linha += M[L][i]
	
	media_da_linha = soma_da_linha / 12	
	print("{:.1f}".format(media_da_linha))
	