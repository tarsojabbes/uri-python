numbers = []
times = 0

while times < 5:
    value = int(input())
    numbers.append(value)
    times += 1

evenNumbers = []
oddNumbers = []
positiveNumbers = []
negativeNumbers = []

for number in numbers:
    if number % 2 == 0:
        evenNumbers.append(number)
    if number % 2 != 0:
        oddNumbers.append(number)
    if number > 0:
        positiveNumbers.append(number)
    if number < 0:
        negativeNumbers.append(number)

print(f'{len(evenNumbers)} valor(es) par(es)')
print(f'{len(oddNumbers)} valor(es) ímpar(es)')
print(f'{len(positiveNumbers)} valor(es) positivo(s)')
print(f'{len(negativeNumbers)} valor(es) negativo(s)')
