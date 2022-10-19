N = int(input())
cobaia = { 'C' : 0,
           'R' : 0,
           'S' : 0   
                    }
total = 0
for i in range(N):
    Quantia, Tipo = [x for x in input().split()]
    Quantia = int(Quantia)
    cobaia[Tipo] = cobaia[Tipo] + Quantia
    total = total + Quantia
    
print("Total: {} cobaias".format(total))
print("Total de coelhos:", cobaia['C'])
print("Total de ratos:", cobaia['R'])
print("Total de sapos:", cobaia['S'])
percc = (cobaia['C']/total)*100
percr = (cobaia['R']/total)*100
percs = (cobaia['S']/total)*100
print("Percentual de coelhos: {:.2f} %".format(percc))
print("Percentual de ratos: {:.2f} %".format(percr))
print("Percentual de sapos: {:.2f} %".format(percs))