X = []
for i in range(10):
	valores = int(input())
	X.append(valores)
	
for i in range(len(X)):
	if X[i] <= 0:
		X[i] = 1
	
	print("X[{0}] = {1}".format(i, X[i]))
	