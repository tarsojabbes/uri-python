X = 0
Y = 0
N = int(input())
while (N >= 0):
  Y = N / 2
  X = X + 1
  print("Experiment " + str(X) + ": " + str(int(Y)) + " full cycle(s)")
  N = int(input())
