# -*- coding: utf-8 -*-

N = int(input())
X = []
contIn = 0
contOut = 0

for i in range(0, N):
    X.append(int(input()))
    if 10 <= X[i] <= 20:
        contIn = contIn + 1
    else:
        contOut = contOut + 1

print(contIn, 'in')
print(contOut,'out')
