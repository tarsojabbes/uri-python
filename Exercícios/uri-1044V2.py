A, B = [int(x) for x in input().split()]
v = (A % B == 0) + (B % A == 0)
if v > 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")