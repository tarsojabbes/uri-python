s = input()
bits1 = 0
for i in range(len(s)):
    if s[i] == '1':
        bits1 += 1

if bits1 % 2 == 1:
    s += '1'
else:
    s += '0'

print(s)
