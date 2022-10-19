a, b, c = map(float, input().split())
pi = 3.14159
#área do triangulo retangulo de base 'a' e altura 'c'
a_triangulo = (a * c)/2
#área do cículo de raio 'c'
a_circulo = pi * c ** 2
#área do trapézio de base 'a' e 'b' e altura 'c'
a_trapezio = (a + b)/2 * c
#área do quadrado de lado 'b'
a_quadrado = b ** 2
#área do retangulo de lado 'a' e 'b'
a_retangulo = a * b

print(f"TRIANGULO: {a_triangulo:.3f}")
print(f"CIRCULO: {a_circulo:.3f}")
print(f"TRAPEZIO: {a_trapezio:.3f}")
print(f"QUADRADO: {a_quadrado:.3f}")
print(f"RETANGULO: {a_retangulo:.3f}")
