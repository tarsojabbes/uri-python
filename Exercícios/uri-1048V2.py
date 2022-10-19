a = float(input())
newval = 0
ajuste = 0
percentual = 0
if a <= 400:
    percentual = 15
    newval = a+((a*percentual)/100)
    ajuste = newval - a
    print("Novo salario: {:.2f}".format(newval))
    print("Reajuste ganho: {:.2f}".format(ajuste))
    print("Em percentual: {} %".format(percentual))
elif a <= 800:
    percentual = 12
    newval = a+((a*percentual)/100)
    ajuste = newval - a
    print("Novo salario: {:.2f}".format(newval))
    print("Reajuste ganho: {:.2f}".format(ajuste))
    print("Em percentual: {} %".format(percentual))
elif a <= 1200:
    percentual = 10
    newval = a+((a*percentual)/100)
    ajuste = newval - a
    print("Novo salario: {:.2f}".format(newval))
    print("Reajuste ganho: {:.2f}".format(ajuste))
    print("Em percentual: {} %".format(percentual))
elif a <= 2000:
    percentual = 7
    newval = a+((a*percentual)/100)
    ajuste = newval - a
    print("Novo salario: {:.2f}".format(newval))
    print("Reajuste ganho: {:.2f}".format(ajuste))
    print("Em percentual: {} %".format(percentual))
elif a > 2000:
    percentual = 4
    newval = a+((a*percentual)/100)
    ajuste = newval - a
    print("Novo salario: {:.2f}".format(newval))
    print("Reajuste ganho: {:.2f}".format(ajuste))
    print("Em percentual: {} %".format(percentual))
