numbers = input().split()
n1, n2, n3 = numbers

list = []
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
list.append(n1)
list.append(n2)
list.append(n3)
list.sort()

for item in list:
    print(item)
print('')
for number in numbers:
    print(number)
