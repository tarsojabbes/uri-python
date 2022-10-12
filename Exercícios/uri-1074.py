N = int(input())
x = 0
even_odd =''
sign = ''
for i in range(N):
    x = int(input())
    if x > 0:
        sign = "POSITIVE"
    elif x < 0:
        sign = "NEGATIVE"
    else:
        sinal = "NULL"
        print(sign)
    if x != 0:
        if x%2==0:
            even_odd = "EVEN"
        else:
            even_odd = "ODD"
        print(even_odd, sign)
