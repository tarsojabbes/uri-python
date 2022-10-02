n = int(input())
position = input()

for move in range(n):
    type_of_move = input()
    if type_of_move == '1':
        if position == 'A':
            position = 'B'
        elif position == 'B':
            position = 'A'
    elif type_of_move == '2':
        if position == 'C':
            position = 'B'
        elif position == 'B':
            position = 'C'
    else:
        if position == 'A':
            position = 'C'
        elif position == 'C':
            position = 'A'

print(position)