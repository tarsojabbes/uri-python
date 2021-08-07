valor = int(input())

notasDe100 = 0
notasDe50 = 0
notasDe20 = 0
notasDe10 = 0
notasDe5 = 0
notasDe2 = 0
notasDe1 = 0
resto = 0

if 0 < valor < 1000000:
    if valor >= 100:
        notasDe100 = int(valor/100)
        resto = valor % 100
        if resto >= 50:
            notasDe50 = int(resto/50)
            resto = resto % 50
        if resto >= 20:
            notasDe20 = int(resto/20)
            resto = resto % 20
        if resto >= 10:
            notasDe10 = int(resto/10)
            resto = resto % 10
        if resto >= 5:
            notasDe5 = int(resto/5)
            resto = resto % 5
        if resto >= 2:
            notasDe2 = int(resto/2)
            resto = resto % 2
        if resto >= 1:
            notasDe1 = int(resto/1)
            resto = resto % 1

print(f'{valor}')
print(f'{notasDe100} nota(s) de R$ 100,00')
print(f'{notasDe50} nota(s) de R$ 50,00')
print(f'{notasDe20} nota(s) de R$ 20,00')
print(f'{notasDe10} nota(s) de R$ 10,00')
print(f'{notasDe5} nota(s) de R$ 5,00')
print(f'{notasDe2} nota(s) de R$ 2,00')
print(f'{notasDe1} nota(s) de R$ 1,00')
