#!/usr/bin/python3
import pdb

pergunta = int(input("digite um numero: "))

def verifica(pergunta):
    if (pergunta % 2 == 0):
        return 'o numero digitado eh PAR'
    else:
        return 'o numero digitado eh IMPAR'

a = verifica(pergunta)
print(a)


