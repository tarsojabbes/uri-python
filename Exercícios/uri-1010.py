firstProduct = str(input())
secondProduct = str(input())

firstList = firstProduct.split()
secondList = secondProduct.split()

valorTotal = (int(firstList[1])*float(firstList[2]) +
              int(secondList[1]) * float(secondList[2]))
print(f'VALOR A PAGAR: R$ {valorTotal:.2f}')
