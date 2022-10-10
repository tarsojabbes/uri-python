Q = int(input())
for C1 in range(Q):
  X = int(input())
  soma=0;

  for C2 in range(1,X):
    if (X%C2==0):
      soma=soma+C2
  if(soma==X):
    print("%i eh perfeito" %X)
    
  else:
    print("%i nao eh perfeito" %X)
     
