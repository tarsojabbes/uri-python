B = int(input())
G = int(input())

resultado = "Amelia tem todas bolinhas!"

if(G/2 >= B):
  if  (G % 2 != 0):
    G = G - 1
  result = (G/2) - B
  resultado = "Faltam {:.0f} bolinha(s)".format(result)
  
print(resultado)
