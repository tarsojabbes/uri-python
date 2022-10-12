i = 0
media = 0
while (i < 2):
    nota = float(input())
    if (nota >= 0 and nota <= 10):
        i = i + 1
        media = media + nota
    if (nota < 0 or nota > 10):
        print("nota invalida")
media = media / 2
print("media = {:.2f}".format(media))