#!/usr/bin/python3

class Dog():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.energia = 10
    
    def latir(self):
        print('Au au !')

    def andar(self):
        if self.energia == 0:
            print('nao da! estou cansado')
        else:
            print('andando...')
        self.energia = self.energia -1
        print(self.energia)

    def dormir(self):
        self.energia = 10
        print('domindo e recarregando')

##fim da classe#


dog1 = Dog('bilu', 2) #objeto

cont = 9
if cont > 0:
    contador = int(input('digite 1 para andar: '))
    dog1.andar()
    cont = cont-1

if contador == 1:
    dog1.andar()
else:
    exit()
    




    
    
