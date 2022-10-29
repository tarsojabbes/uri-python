qt_elfos = int(input())

musicos = 0
desenhistas = 0
arquitetos = 0
bonecos = 0

presentes = 0
for i in range(qt_elfos):
    elfo = input().split()
    if elfo[1] == "bonecos": bonecos += int(elfo[2])
    elif elfo[1] == "arquitetos": arquitetos += int(elfo[2])
    elif elfo[1] == "musicos": musicos += int(elfo[2])
    elif elfo[1] == "desenhistas": desenhistas += int(elfo[2])

presentes = (musicos // 6) + (desenhistas // 12) + (arquitetos // 4) + (bonecos // 8)

print(presentes)
