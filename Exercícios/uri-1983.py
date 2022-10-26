qt_alunos = int(input())

maior = 0
melhor_aluno = 0
for i in range(qt_alunos):
    aluno = input().split()
    if float(aluno[1]) > maior:
        maior = float(aluno[1])
        melhor_aluno = aluno[0]

if maior >= 8:
    print(melhor_aluno)
else:
    print("Minimum note not reached")

