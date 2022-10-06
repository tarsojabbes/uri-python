v = int(input())
p = int(input())
parcelas = [0]*p
rest = v%p

for value in range(len(parcelas)):
    if v%p == 0:
        print(int(v/p))
    else:
        if rest != 0:
            print(int(((v-v%p)/p) + 1))
            rest -= 1
        else:
            print(int((v-v%p)/p))