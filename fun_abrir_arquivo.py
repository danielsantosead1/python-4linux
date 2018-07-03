#!/usr/bin/python3

frutas  =  [
    {'fruta': 'banana', 'preco':2.0, 'qtd':10},
    {'fruta': 'laranja', 'preco':5, 'qtd':20},
    {'fruta': 'pera', 'preco':4.5, 'qtd':2}
]
##metodo 1
# def abrir(nome_arquivo):
#     try:    
#         with open (nome_arquivo, 'a+') as arquivo:
#             for itens in frutas:
#                 arquivo.write('{}\n'.format(itens))
#             return True 

#     except Exception as e:
#         return "erro: {}".format(e)
    
# a = abrir('frutas.txt')
# print(a)

##metodo 2
def abrir(nome_arquivo, lista):
    try:    
        with open (nome_arquivo, 'a+') as arquivo:
            for itens in lista:
                arquivo.write('{}\n'.format(itens))
            return True 

    except Exception as e:
        return "erro: {}".format(e)
    
a = abrir('frutas.txt', frutas)
print(a)



exit()
def abrir(nome_arquivo):
    try:    
        with open (nome_arquivo, 'r') as arquivo:
            return arquivo.readlines()        
    except Exception as e:
        return "erro: {}".format(e)
    
a = abrir('frutas.txt')

print(a)