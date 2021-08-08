numbers = input().split()

a, b, c = numbers

delta = (float(b)**2) - 4 * float(a) * float(c)
r1 = 0
r2 = 0

if float(a) == 0 or delta <= 0:
    print('Impossivel calcular')
else:
    r1 = ((float(b) * (-1)) + (delta**0.5))/(2*(float(a)))
    r2 = ((float(b) * (-1)) - (delta**0.5))/(2*(float(a)))
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')
