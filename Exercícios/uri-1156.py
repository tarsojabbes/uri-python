S = 1
denominador = 2
for numerador in range(3, 40, 2):
    S += numerador / denominador
    denominador *= 2
print(f"{S:.2f}")
