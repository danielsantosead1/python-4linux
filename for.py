#!/usr/bin/python3
num = int(input("digite um numero"))

for x in range(num):
    if x % 2 == 0:
        print("{} par".format(x))
    else:
        print("{} impar".format(x))