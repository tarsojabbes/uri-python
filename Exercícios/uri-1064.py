numbers = []
times = 0

while times < 6:
    value = float(input())
    numbers.append(value)
    times += 1

positiveNumbers = []

for number in numbers:
    if number > 0:
        positiveNumbers.append(number)

total = 0

for number in positiveNumbers:
    total = total + number

average = total/(len(positiveNumbers))

print(f'{len(positiveNumbers)} valores positivos')
print(f'{average:.1f}')
