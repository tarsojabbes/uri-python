import math

def main():
    r1, x1, y1, r2, x2, y2 = [int(x) for x in input().split()]
    dist = math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)))

    if((r1 - dist) >= r2):
        print("RICO")
    else:
      print("MORTO")

while True:
  try:
    main()
  except EOFError:
    break
