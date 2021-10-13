n = int(input())
for i in range(n):
    # [0] - num1 / [1] - operador / [2] - num2 / [4] - resultado
    entrada = input().split()
    if (entrada[1] == 'x'):
        r_correto = int(entrada[0]) * int(entrada[2])
    elif (entrada[1] == '+'):
        r_correto =  int(entrada[0]) + int(entrada[2])
    else:
        r_correto =  abs(int(entrada[0]) - int(entrada[2]))

    final = abs(r_correto - int(entrada[4]))

    print('E{}ou!'.format('r' * final))
