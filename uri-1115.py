x , y = [int(x) for x in input().split()]
if x > 0 and y > 0:
    print("primeiro")
elif x < 0 and y > 0:
    print("segundo")
elif x < 0 and y < 0:
    print("terceiro")
elif x > 0 and y < 0:
    print("quarto")
while x != 0 and y != 0:
    x , y = [int(x) for x in input().split()]
    if x > 0 and y > 0:
        print("primeiro")
    elif x < 0 and y > 0:
        print("segundo")
    elif x < 0 and y < 0:
        print("terceiro")
    elif x > 0 and y < 0:
        print("quarto")
