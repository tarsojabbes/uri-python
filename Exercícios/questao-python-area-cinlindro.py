import math

print('Cálculo da Superfície de um Cilindro')
print('---')
diametro = float(input('Medida do diâmetro? '))
altura = float(input('Medida da altura? '))

base = math.pi * (diametro / 2) ** 2
lateral = altura * (math.pi * 2 * (diametro / 2))
area = 2 * base + lateral
print('---')
print(f'Área calculada: {area:.2f}')
