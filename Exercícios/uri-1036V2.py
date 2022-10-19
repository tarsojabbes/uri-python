a, b, c = [float(x) for x in input().split()]
delta = (b**2)-(4*a*c)
if delta < 0 or a == 0:
    print("Impossivel calcular")
elif delta == 0:
    R1 = (-1*b)/(2*a)
    R2 = R1
    print("R1 = {:.5f}".format(R1))
    print("R2 = {:.5f}".format(R2))
else:
    R1 = ((-1*b)+(delta**(1/2)))/(2*a)
    R2 = ((-1*b)-(delta**(1/2)))/(2*a)
    print("R1 = {:.5f}".format(R1))
    print("R2 = {:.5f}".format(R2))