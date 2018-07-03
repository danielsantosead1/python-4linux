#!/usr/bin/python3
try:
    with open('nomes.txt', 'r') as arquivo:
        var = arquivo.readlines()
    alterado = []
    cont = 1

    for linha in var:
        linha = linha.replace('\n', '-{}\n'.format(cont))
        alterado.append(linha)
        cont += 1 
    print(alterado)
    with open('novo.txt', 'w') as arquivo:
            for linha in alterado:
                arquivo.write(linha)
except FileNotFoundError as e:
    print("arquivo nao existe")