lines = input().split(' ')

horainicio, mininicio, horafim, minfim = lines

mininicio = int(mininicio)
minfim = int(minfim)
horafim = int(horafim)*60;
horainicio = int(horainicio)*60;

durac = (horafim + minfim) - (horainicio + mininicio)

if(durac <= 0):
    durac += 24*60;

hora = durac//60
minutos = durac - (60*hora)
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora, minutos))