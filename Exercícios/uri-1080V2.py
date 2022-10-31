#include <stdio.h>
max = 0

for i in range(0, 100):
    num = int(input())
    if num > max:
        max = num
        posicao = i + 1

print(f'{max}\n{posicao}')
