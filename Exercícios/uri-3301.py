def median_patinho(p):
    a = int(p[0])
    b = int(p[1])
    c = int(p[2])

    if a > b:
        if a < c: return 'huguinho'
        elif b > c: return 'zezinho'
        else: return 'luisinho'
    else:
        if a > c: return 'huguinho'
        elif b < c: return 'zezinho'
        else: return 'luisinho'


sobrinhos = input().split()
print(median_patinho(sobrinhos))
