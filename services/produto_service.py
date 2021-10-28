from connection_service import getConnectin

def saveOrUpdate(produtos):
    conn = getConnectin()
    cur = conn.cursor()
    cur.execute( "SELECT cadastra_produto('3', 'nome alterado', 'nome 2', 'ref', 1.0, '', '');" )
    conn.close()
    print("Salvou")
    # createOrReplaceFunction()
    # for p in produtos:
    #     print(p.codigo, p.produto)

# def createOrReplaceFunction():
#     print("create function")
#     conn = getConnectin()
#     cur = conn.cursor()
#     cur.execute( "SELECT id, name FROM cliente" )
#     conn.close()
