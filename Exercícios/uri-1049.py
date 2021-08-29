inp1 = input()
inp2 = input()
inp3 = input()

if inp1 == 'vertebrado':
    if inp2 == 'ave':
        if inp3 == 'carnivoro':
            print('aguia')
        elif inp3 == 'onivoro':
            print('pomba')
    elif inp2 == 'mamifero':
        if inp3 == 'onivoro':
            print('homem')
        elif inp3 == 'herbivoro':
            print('vaca')
elif inp1 == 'invertebrado':
    if inp2 == 'anelideo':
        if inp3 == 'hematofago':
            print('sanguessuga')
        elif inp3 == 'onivoro':
            print('minhoca')
    elif inp2 == 'inseto':
        if inp3 == 'hematofago':
            print('pulga')
        elif inp3 == 'herbivoro':
            print('lagarta')
