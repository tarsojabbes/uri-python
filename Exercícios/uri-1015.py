firstLine = input().split()
secondLine = input().split()

distance = ((float(secondLine[0]) - float(firstLine[0])) **
            2 + (float(secondLine[1]) - float(firstLine[1]))**2)**0.5

print(f'{distance:.4f}')