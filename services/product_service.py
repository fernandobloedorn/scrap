from .connection_service import getConnectin

def saveOrUpdate(produtos):
    
    # conn = getConnectin()
    # cur = conn.cursor()
    # sql = "SELECT cadastra_produto('12', 'teste', '', 'A', 0.0, '', '');"
    # # sql = "Insert into produto (codigo, nome_tecnico) values ('45', 'teste');"
    # print(sql)
    # cur.execute(sql)
    # conn.commit() # <- We MUST commit to reflect the inserted data
    # cur.close()
    # conn.close()

    for p in produtos:
        print(p.codigo, "-", p.produto)
        conn = getConnectin()
        cur = conn.cursor()
        sql = "SELECT cadastra_produto('" + p.codigo + "', '" + p.produto + "', '', '" + p.ref + "', 0.0, '', '');"
        print(sql)
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        print("Salvou 1")
        

# def createOrReplaceFunction():
#     print("create function")
#     conn = getConnectin()
#     cur = conn.cursor()
#     cur.execute( "SELECT id, name FROM cliente" )
#     conn.close()
