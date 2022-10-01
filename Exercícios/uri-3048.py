n = int(input())
numbers = []
x = 1

for number in range(n):
    v = int(input())
    if number != 0:
        if v != numbers[number-1]:
            x += 1
    numbers.append(v)
    
print(x)