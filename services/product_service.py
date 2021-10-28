from .connection_service import getConnectin

def saveOrUpdate(produtos):
    conn = getConnectin()
    cur = conn.cursor()
    
    for p in produtos:
        print(p.codigo, p.produto)
        cur.execute( "SELECT cadastra_produto('" + p.codigo + "', '" + p.produto + "', '', '" + p.ref + "', 0.0, '', '');" )
        print("Salvou")
    conn.close()

# def createOrReplaceFunction():
#     print("create function")
#     conn = getConnectin()
#     cur = conn.cursor()
#     cur.execute( "SELECT id, name FROM cliente" )
#     conn.close()
