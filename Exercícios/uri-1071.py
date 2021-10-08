n1 = int(input())
n2 = int(input())

lista = []

if (n1 >= 0 or n2 >= 0):
    if (n1 >= n2):
        for i in range(n1+1,n2):
            if (i % 2 != 0):
                lista.append(i)
    else:
        for i in range(n2+1,n1):
            if (i % 2 != 0):
                lista.append(i)
else:
    for i in range(0,n1,-1):
        if (i % 2 != 0):
            lista.append(i)
    for j in range(0,n2,-1):
        if (j % 2 != 0):
            lista.append(j)


print(sum(lista))
