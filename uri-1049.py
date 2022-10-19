# -*- coding: utf-8 -*-

animal1 = input()
animal2 = input()
animal3 = input()

if animal1 == 'vertebrado':
    if animal2 == 'ave' and animal3 == 'carnivoro':
        print('aguia')
    elif animal2 == 'ave' and animal3 == 'onivoro':
        print('pomba')
    elif animal2 == 'mamifero' and animal3 == 'onivoro':
        print('homem')
    elif animal2 == 'mamifero' and animal3 == 'herbivoro':
        print('vaca')
        
elif animal1 == 'invertebrado':
    if animal2 == 'inseto' and animal3 == 'hematofago':
        print('pulga')
    elif animal2 == 'inseto' and animal3 == 'herbivoro':
        print('lagarta')
    elif animal2 == 'anelideo' and animal3 == 'hematofago':
        print('sanguessuga')
    elif animal2 == 'anelideo' and animal3 == 'onivoro':
        print('minhoca')
