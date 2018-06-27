#!/usr/bin/python3


nomes = []
    
while True:
    nome = input('Digite um nome para inserir na lista ou sair para parar')
    if nome == 'sair':
        print("os nomes digitados foram:", nomes)
        break
        
    else:
        nomes.append(nome)



    
