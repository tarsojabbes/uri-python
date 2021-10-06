while True:
    pairValues = input().split()
    m = int(pairValues[0])
    n = int(pairValues[1])
    if m <= 0 or n <= 0:
        break
    else:
        if m > n:
            m, n = n, m
        aux = m - n - 1
        sum_values = int(((m + n) * abs(aux))/2)
        for i in range(m, n + 1):
            print(f'{i}', end=" ")
        print(f'Sum={sum_values}')
