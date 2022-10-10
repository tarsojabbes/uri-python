Y = 1
x = int(input())
print("N[0] = 0")
for W in range(1, 1000):
  if x > Y:
    print("N[" + str(W) + "] = " + str(Y))
    Y += 1
  else:
    Y = 1
    print("N[" + str(W) + "] = 0")
