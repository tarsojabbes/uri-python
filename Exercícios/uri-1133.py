x = int(input())
y = int(input())

if y < x:
    a = x
    x = y
    y = a

for i in range(x+1, y):
    if(i % 5 == 2 or i % 5 == 3):
        print(i)