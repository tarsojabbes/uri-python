#include <stdio.h>
J = 8
I = 1
comparacao = 5

while I < 10:
    J -= 1
    print(f'I={I} J={J}')
    if J == comparacao:
        J += 5
        I += 2
        comparacao += 2
