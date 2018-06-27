#!/usr/bin/python3
nome = input("aluno, digite seu nome:")
nota1 = float(input("digite sua primeira nota:"))
nota2 = float(input("digite sua segunda nota: "))
resultado = (nota1 + nota2) / 2

nome = nome.replace('a', '@')
print(nome, "sua media eh: ", resultado)

if resultado >= 6:
    result = "Aprovado"
elif resultado < 5 and resultado >= 4:
    result = "Recuperação"
else:
    result = "Reprovado"

print("""
        nome:{}
        resultado:{}
        result:{}
        """.format(nome. media, result))