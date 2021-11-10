import math

test_cases = int(input())

while test_cases > 0:
	qtd = input().split()
	qtd_1 = int(qtd[0])
	qtd_2 = int(qtd[1])
	result = math.gcd(qtd_1, qtd_2)
	print(result)
	test_cases-=1
