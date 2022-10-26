# -*- coding: utf-8 -*-

from math import sqrt

def fib(n):
    raiz_5 = sqrt(5)
    return (((1 + raiz_5) / 2) ** n - ((1 - raiz_5) / 2) ** n) / sqrt(5)

n = int(input())
print("%.1f" % fib(n))
