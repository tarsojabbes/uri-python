total = 0
cont = 0

while True:
    age = int(input())

    if(age <= 0): break

    total += age
    cont += 1

print(f'{total / cont:.2f}')