#include <stdio.h>
h1, m1, h2, m2 = [int(x) for x in input().split()]

minfinal = 0
hrsmenos = 0
if m1 > m2:
    minfinal = (m2 + 60) - m1
    hrsmenos = 1
elif m1 < m2:
    minfinal = m2 - m1
else:
    pass

if h1 > h2:
    print(f'O JOGO DUROU {((h2 + 24) - h1) - hrsmenos} HORA(S) E {minfinal} MINUTO(S)')
elif h1 < h2:
    print(f'O JOGO DUROU {(h2 - h1) - hrsmenos} HORA(S) E {minfinal} MINUTO(S)')
elif h1 == h2 and m1 > m2:
    print(f'O JOGO DUROU 23 HORA(S) E {minfinal} MINUTO(S)')
elif h1 == h2 and m1 < m2:
    print(F'O JOGO DUROU 0 HORA(S) E {minfinal} MINUTO(S)')
else:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
    
