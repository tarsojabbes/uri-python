tempo = float(input())

horas = 0
minutos = 0
segundos = 0
resto = 0

if tempo >= 3600:
    horas = horas + int(tempo/3600)
    resto = tempo % 3600
    if resto < 3600:
        minutos = minutos + int(resto/60)
        resto = resto % 60
    if resto <= 60:
        segundos = int(segundos + resto)
else:
    minutos = minutos + int(tempo/60)
    resto = tempo % 60
    if resto <= 60:
        segundos = int(segundos + resto)

print(f'{horas}:{minutos}:{segundos}')
