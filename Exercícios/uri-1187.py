O = input()

M = []
vetor_auxiliar_para_a_matriz = []
for i in range(144):
	valor = float(input())
	vetor_auxiliar_para_a_matriz.append(valor)

	if len(vetor_auxiliar_para_a_matriz) == 12:
		M.append(vetor_auxiliar_para_a_matriz)
		vetor_auxiliar_para_a_matriz = []

if O == "S":
	soma_area_superior = 0

	for i_linha in range((len(M) // 2) - 1):
		for i_coluna in range(i_linha + 1, len(M) - (i_linha + 1)):
			soma_area_superior += M[i_linha][i_coluna]				

	print("{:.1f}".format(soma_area_superior))

else:
	soma_area_superior = 0
	media = 0
	conta_elementos = 0

	for i_linha in range((len(M) // 2) - 1):
		for i_coluna in range(i_linha + 1, len(M) - (i_linha + 1)):
			soma_area_superior += M[i_linha][i_coluna]				
			conta_elementos += 1

	media = soma_area_superior / conta_elementos
	print("{:.1f}".format(media))

