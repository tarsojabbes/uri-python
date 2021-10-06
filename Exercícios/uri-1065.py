numbers = []
times = 0

while times < 5:
    value = int(input())
    numbers.append(value)
    times += 1

evenNumbers = []

for number in numbers:
    if number % 2 == 0:
        evenNumbers.append(number)

print(f'{len(evenNumbers)} valores pares')
