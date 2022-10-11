alcool = gasolina = diesel = 0
while True:
    combustivel = int(input())
    if combustivel == 1:
        alcool += 1
    elif combustivel == 2:
        gasolina += 1
    elif combustivel == 3:
        diesel += 1
    elif combustivel == 4:
        break
        
print("MUITO OBRIGADO")
print("Alcool: %i\nGasolina: %i\nDiesel: %i" % (alcool, gasolina, diesel))
