bolinhas = int(input())
galhos = int(input())
if galhos % 2 == 1:
  galhos -= 1
if galhos / 2 > bolinhas:
  print("Faltam " + str(int(galhos / 2 - bolinhas)) + " bolinha(s)")
else:
  print("Amelia tem todas bolinhas!")
