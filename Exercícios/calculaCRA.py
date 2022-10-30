periodos = int(input())

disciplinas_cursadas = 0
CRA = 0
i = 1

while i <= periodos:

    media_semestre = 0

    j = 1

    disciplinas = int(input())

    disciplinas_cursadas += disciplinas

    while j <= disciplinas:
        notas = float(input())
        media_semestre += notas

        j += 1

    print(f'Minha média no {i}º período é: {media_semestre/disciplinas:.2f}')

    CRA += media_semestre

    i += 1

print(f'\nMeu CRA é: {CRA/disciplinas_cursadas:.2f}')