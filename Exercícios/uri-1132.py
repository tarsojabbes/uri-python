x = int(input())
y = int(input())

total = 0

if y > x:
    y, x = y, x

for i in range(x, y + 1):
    if i % 13 != 0:
        total += i

print(total)