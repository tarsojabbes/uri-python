n = int(input())

count = 0
a1 = 0
a2 = 1
sequence = "0 1 "
while count < n - 2:
    a3 = a1 + a2
    sequence += str(a3) + " "
    a1 = a2
    a2 = a3
    count += 1

print(sequence.strip())