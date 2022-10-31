#include <stdio.h>
J = 8
I = 1

while I < 10:
    J -= 1
    print(f'I={I} J={J}')
    if J == 5:
        J = 8
        I += 2
