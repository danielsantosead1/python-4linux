#!/usr/bin/python3

while True:
    try:
        num = int(input("digite um numero: "))
        print(num)
        break
    except Exception as e:
        print("nao é um inteiro: {}".format(e))



