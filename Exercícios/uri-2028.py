case = 1
while True:
	try:
		n = int(input()) + 1
		iter = 0
		array = [0]
		while iter < n:
			iter += 1
			qtd = 0
			while qtd < (n - iter):
				array.append((n) - ((n) - ((n) - iter)))
				qtd += 1
		array.sort()

		newArray = " ".join([str(i) for i in array])
		if len(array) == 1:
			print(f'Caso {case}: {len(array)} numero')
		else:
			print(f'Caso {case}: {len(array)} numeros')
		print(newArray, end="")
		print('\n')
		case += 1

	except EOFError:
		break