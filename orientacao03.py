#!/usr/bin/python3

class Carro():
    def __init__(self, marca, modelo):
        self.rodas = 4
        self.portas = 5
        self.cor = 'preta'
        self.gasolina = 100
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        if self.gasolina == 0:
            print('acabou a gasolina')
        else:
            while self.gasolina > 0:
                contador = int(input('continuar acelerando? presione 1 para sim'))
                if contador == 1:
                    print('acelerando...')
                    self.gasolina -= 10
                    print('tanque...{}%'.format(self.gasolina))
                    if self.gasolina == 0:
                        print('acabou a gasolina')
                        recarregar = input('abastecer? digite sim ou nao: ')
                        if recarregar == 'sim':
                            self.gasolina = 100
                        else:
                            print('adeus')
                else:
                    exit()
            
    def frear(self):
        print('freando...')
    
objetoCarro = Carro('toyota', 'prius')

print('marca do carro: {}'.format(objetoCarro.marca))
print('cor do carro: {}'.format(objetoCarro.cor))
print('Quantidade de rodas: {}'.format(objetoCarro.rodas))
print('Quantidade de portas: {}'.format(objetoCarro.portas))
   
objetoCarro.acelerar()
   

    