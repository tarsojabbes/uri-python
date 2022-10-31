N = int(input())

def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    
    return True

for num in [int(input()) for i in range(N)]:
    if isPrime(num):
        print("Prime")
    else:
        print("Not Prime")