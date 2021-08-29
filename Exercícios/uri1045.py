numbers = input().split()

a, b, c = numbers
a = float(a)
b = float(b)
c = float(c)

list = []
list.append(a)
list.append(b)
list.append(c)
list.sort(reverse=True)

if list[0] >= (list[1] + list[2]):
    print('NAO FORMA TRIANGULO')
# or b**2 == (c**2 + a**2) or c**2 == (b**2 * a**2)
if list[0]**2 == (list[1]**2 + list[2]**2) or list[1]**2 == (list[2]**2 + list[0]**2) or list[2]**2 == (list[1]**2 * list[0]**2):
    print('TRIANGULO RETANGULO')
# or b**2 > (c**2 + a**2) or c**2 > (b**2 * a**2)
if list[0]**2 > (list[1]**2 + list[2]**2) or list[1]**2 > (list[2]**2 + list[0]**2) or list[2]**2 > (list[1]**2 * list[0]**2):
    print('TRIANGULO OBTUSANGULO')
# or b**2 < (c**2 + a**2) or c**2 < (b**2 * a**2)
if list[0]**2 < (list[1]**2 + list[2]**2) and list[1]**2 < (list[2]**2 + list[0]**2) and list[2]**2 < (list[1]**2 * list[0]**2):
    print('TRIANGULO ACUTANGULO')
if list[0] == list[1] and list[1] == list[2]:
    print('TRIANGULO EQUILATERO')

# Triangulo Isósceles
if list[0] == list[1] and list[1] != list[2]:
    print('TRIANGULO ISOSCELES')
if list[0] == list[2] and list[2] != list[1]:
    print('TRIANGULO ISOSCELES')
if list[1] == list[2] and list[2] != list[0]:
    print('TRIANGULO ISOSCELES')
