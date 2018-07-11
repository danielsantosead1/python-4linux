#!/usr/bin/python3
from pymongo import MongoClient

try:
    client = MongoClient()
    db = client['4linux']
except Exception as e:
    print('erro {}'.format(e))

dados = db.pessoas.find_one({'id':2})

db.pessoas.update({"id":2}, {"nome":"daniel santos guedes"})

print(dados)