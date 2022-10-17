v = []
for a in range(0, 20):
    v.append(int(input()))

count = 0
reverse_count = len(v) - 1

while count < reverse_count:
    v[count], v[reverse_count] = v[reverse_count], v[count]
    count += 1
    reverse_count -= 1

for i in range(len(v)):
    print(f"N[{i}] = {v[i]}")