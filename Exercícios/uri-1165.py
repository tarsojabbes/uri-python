n = int(input())
for x in range(n):
    num = int(input())
    t = 0
    for i in range(1, num+1):
        if num % i == 0:
            t += 1
    if t == 2:
        print(f'{num} eh primo')
    else:
        print(f'{num} nao eh primo')
