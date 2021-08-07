numeros = input().split()

triangulo = (float(numeros[0]) * float(numeros[2]))/2

circulo = 3.14159 * (float(numeros[2])**2)

trapezio = ((float(numeros[0]) + float(numeros[1])) * float(numeros[2]))/2

quadrado = float(numeros[1])**2

retangulo = float(numeros[0]) * float(numeros[1])

print(f'TRIANGULO: {triangulo:.3f}\nCIRCULO: {circulo:.3f}\nTRAPEZIO: {trapezio:.3f}\nQUADRADO: {quadrado:.3f}\nRETANGULO: {retangulo:.3f}')
