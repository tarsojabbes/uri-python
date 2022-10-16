entrada = input().split()

C = int(entrada[0]) #Distânca percorrida (m)
N = int(entrada[1]) #Comprimento da pista (m)

resultado = C % N   #Ponto de término

print(resultado)
