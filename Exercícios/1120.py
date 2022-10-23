while(True):
    entrada, num = input().split()
    if(entrada == '0' and num == '0'):
        break
    num = '0' + num
    valor = int(num.replace(entrada,''))
    print(valor)
