N = int(input())

for N in range(0,N):
    N = int(input())
    if N % 2 == 0 and N > 0: 
        print('EVEN POSITIVE')
    elif N % 2 != 0 and N > 0:
        print('ODD POSITIVE')
    elif N == 0 :
        print('NULL')
    elif N % 2 == 0 and N < 0:
        print('EVEN NEGATIVE')
    elif N % 2 != 0 and N < 0:
        print('ODD NEGATIVE')

