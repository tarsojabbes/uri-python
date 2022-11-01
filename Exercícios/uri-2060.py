n = int(input())
numeros = [int(x) for x in input().split()]
multiplos = {2:0, 3:0, 4:0, 5:0}

for num in numeros:
    for key,value in multiplos.items():
        if num % key == 0:
            multiplos[key] = value + 1
for key,value in multiplos.items():
    print(f"{value} Multiplo(s) de {key}")
