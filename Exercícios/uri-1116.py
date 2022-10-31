#include <stdio.h>

vezes = int(input())

for vez in range(vezes):
    x, y = input().split()
    x = int(x)
    y = int(y)
    
    if y == 0:
        saida = 'divisao impossivel'
    else:
        media = x / y
        saida = f'{media:.1f}'
        
    print(saida)
