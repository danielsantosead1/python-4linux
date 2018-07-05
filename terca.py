#!/usr/bin/python3

# def boas_vindas(*nomes):
#     for item in nomes:
#         print("ola seja bem vindo {}".format(item))
    
# boas_vindas('daniel', 'rayna', 'paulo')

# def boas_vindas(**kargs):
#     print('seja bem vindo {} {}'.format(kargs['nome'], kargs['sobrenome']))

# boas_vindas(nome='daniel', sobrenome='santos')

########################################################
def boas_vindas(**kargs):
    a = kargs['preco']
    b = kargs['qtd']
    c = a * b
    print('o valor total eh {}'.format(c))

boas_vindas(fruta='laranja', preco=2, qtd=5)
########################################################

