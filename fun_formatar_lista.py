#!/usr/bin/python3
minhalista = ['daniel', 'santos', 'guedes', 'sampaio']
novalista = []

def formatar_lista(lista):
    for itens in minhalista:
        novalista.append('{}\n'.format(itens))
    return novalista

a = formatar_lista('minhalista')
print(a)

