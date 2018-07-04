#!/usr/bin/python3

fruta = {
    'nome' : 'laranja',
    'valor': 4,
    'qtd'  : 25
}
var = lambda x, y: x*y

print(var(fruta['valor'], fruta['qtd']))
