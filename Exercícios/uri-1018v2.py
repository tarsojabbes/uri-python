N = int(input())
print(N)
notas = {"nota(s) de R$ 100,00" : 100,
         "nota(s) de R$ 50,00": 50,
         "nota(s) de R$ 20,00": 20,
         "nota(s) de R$ 10,00": 10,
         "nota(s) de R$ 5,00": 5,
         "nota(s) de R$ 2,00": 2,
         "nota(s) de R$ 1,00":1}
resto= N
for key,value in notas.items():
    notas[key] = int(resto/value)
    resto = resto%value
    print(notas[key],key)