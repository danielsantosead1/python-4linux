#!/usr/bin/python3

class Dog():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.energia = 10
    

    def latir(self):
        print('Au au !')

    def andar(self):
        self.energia = self.energia -1
        print('andando... energia {}'.format(self.energia))

    def dormir(self):
        self.energia = 10
        print('domindo e recarregando')

dog1 = Dog('bilu', 2)

print(dog1.idade)

dog1.latir()

dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()

dog1.dormir()

dog1.andar()
    

    
#!/usr/bin/python3
