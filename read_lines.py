#!/usr/bin/python3

with open('nomes.txt', 'r') as arquivo:
    var = arquivo.readlines()
alterado = []
cont = 1
for linha in var:
    alterado.append('{}-{}'.format(cont, linha))
    cont = cont+1
print(alterado)

with open ('nomes.txt', 'a+') as arquivo:
    for x in alterado:
        arquivo.write(x)   