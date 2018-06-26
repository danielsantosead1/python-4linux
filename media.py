#!/usr/bin/python3
nome = input("aluno, digite seu nome:")
nota1 = int(input("digite sua primeira nota:"))
nota2 = int(input("digite sua segunda nota"))
resultado = (nota1 + nota2) / 2
nome = nome.replace('a', '@')
print(nome, "sua media eh:", resultado)

