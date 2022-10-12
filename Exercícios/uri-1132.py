X = int(input())
Y = int(input())
less, great = 0, 0
if X > Y:
   great = X
   less = Y
else:
   great = Y
   less = X
sum = 0
for i in range(less, great + 1, 1):
    if i % 13 != 0:
        sum = sum + i
print(sum)
