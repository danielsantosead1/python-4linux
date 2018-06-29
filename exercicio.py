#!/usr/bin/python3

with open ('nomes.txt', 'a') as arquivo:
    while True:
        nome = input('Digite um nome para inserir na lista ou sair para parar')
        if nome == 'sair':
            break
        arquivo.write(nome + '\n')        
            
   
