sequence = ""

n = int(input())

for i in range(n * 4 + 1):
    if i % 4 != 0:
        sequence += f"{i}" + " "
    elif i % 4 == 0 and i != 0:
        sequence += "PUM\n"

print(sequence.strip())