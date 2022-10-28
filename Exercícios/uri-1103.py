arr = input().split()
h1, m1, h2, m2 = [int(x) for x in arr]

while h1 != 0 or m1 != 0 or h2 != 0 or m2 != 0:

  mi = 60*h1+m1
  mf = 60*h2+m2
  if mi < mf:
    print(mf-mi)

  if mi > mf:
    print(24*60-mi+mf)

  arr = input().split()
  h1, m1, h2, m2 = [int(x) for x in arr]
  
