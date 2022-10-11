lines = float(input())

if(0<lines<=2000):
    print("Isento")
elif(2000<lines<=3000):
    t= (lines-2000)
    tx= (t*8)/100
    print("R$ {:.2f}".format(tx))
elif(3000<lines<=4500):
    t= (lines-3000)
    tx1=(1000*8)/100
    tx2= (t*18)/100
    print("R$ {:.2f}".format((tx1+tx2)))
else:
    t= (lines-4500)
    tx1= (1000*8)/100
    tx2=(1500*18)/100
    tx= (t*28)/100
    print("R$ {:.2f}".format((tx+tx1+tx2)))
