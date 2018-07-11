#!/usr/bin/python3

import psycopg2

try:
    con = psycopg2.connect('host=localhost dbname=projeto user=admin password=4linux')
    print('conectou com sucesso')

    cur = con.cursor()
    
    #cur.execute("insert into pessoas (nome, idade, telefone) values('chuck noris', 28, '111111111')")
    #con.commit()
    
    cur.execute("select * from pessoas")
    conteudo = cur.fetchall()
    
    print(conteudo)
    

except Exception as e:
    print('erro conexao: {}'.format(e))
    


