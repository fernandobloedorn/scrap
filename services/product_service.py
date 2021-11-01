from .connection_service import getConnection
import util.date_util as dateUtil

SELECT = "SELECT id FROM produto WHERE codigo = %s;"
INSERT = "INSERT INTO produto (codigo, nome_tecnico, referencia, linha) VALUES( %s, %s, %s, %s) RETURNING id;"
UPDATE = "UPDATE produto SET nome_tecnico = %s, referencia = %s, linha = %s WHERE id = %s;"

def saveOrUpdate(products):
    
    conn = getConnection()
    cur = conn.cursor()

    for product in products:

        cur.execute(SELECT, (product.code,))
        result = cur.fetchone()

        id = None 

        if result is not None:
            id = result[0]
            # print("ID update:", id, "Type:", type(id))

            cur.execute(UPDATE, (product.name, product.reference, product.line, id))
            conn.commit()

        else:
            cur.execute(INSERT, (product.code, product.name, product.reference, product.line))
            conn.commit()
            id = cur.fetchone()[0]
            # print("ID insert:", id, "Type:", type(id))

        # if id is not None:
        #     print("ID OK")
        # else:
        #     print("ID Nao OK: ", produto.codigo)

            # print(p.codigo, "-", p.produto)
        
        # sql = "SELECT cadastra_produto('" + p.codigo + "', '" + p.produto + "', '', '" + p.ref + "', 0.0, '', '');"
        # print(sql)
        # cur.execute(sql)
        # conn.commit()

    cur.close()
    conn.close()

# CREATE OR REPLACE FUNCTION cadastra_produto(character, character, character, character, numeric, character, character)
#   RETURNS void AS
# $BODY$ 
# DECLARE P_CODIGO ALIAS FOR $1;
# DECLARE P_NOME_TECNICO ALIAS FOR $2;
# DECLARE P_NOME_COMERCIAL ALIAS FOR $3;
# DECLARE P_REFERENCIA ALIAS FOR $4;
# DECLARE P_SALDO ALIAS FOR $5;
# DECLARE P_URL_FOTO ALIAS FOR $6;
# DECLARE P_URL_FICHA_TECNICA ALIAS FOR $7;
# BEGIN
#    IF((SELECT COUNT(*) FROM produto WHERE codigo = P_CODIGO) > 0) THEN
#       UPDATE produto SET nome_tecnico = P_NOME_TECNICO, nome_comercial = P_NOME_COMERCIAL, referencia = P_REFERENCIA, saldo = P_SALDO, url_foto = P_URL_FOTO, url_ficha_tecnica = P_URL_FICHA_TECNICA      
#       WHERE codigo = P_CODIGO;
#    ELSE
#       INSERT INTO produto (codigo, nome_tecnico, nome_comercial, referencia, saldo, url_foto, url_ficha_tecnica) 
#       VALUES (P_CODIGO, P_NOME_TECNICO, P_NOME_COMERCIAL, P_REFERENCIA, P_SALDO, P_URL_FOTO, P_URL_FICHA_TECNICA);
#    END IF;
# END;
# $BODY$
        

# def createOrReplaceFunction():
#     print("create function")
#     conn = getConnectin()
#     cur = conn.cursor()
#     cur.execute( "SELECT id, name FROM cliente" )
#     conn.close()

# def saveOrUpdateOld(produtos):
    
#     # conn = getConnectin()
#     # cur = conn.cursor()
#     # sql = "SELECT cadastra_produto('12', 'teste', '', 'A', 0.0, '', '');"
#     # # sql = "Insert into produto (codigo, nome_tecnico) values ('45', 'teste');"
#     # print(sql)
#     # cur.execute(sql)
#     # conn.commit() # <- We MUST commit to reflect the inserted data
#     # cur.close()
#     # conn.close()

#     for p in produtos:
#         print(p.codigo, "-", p.produto)
#         conn = getConnection()
#         cur = conn.cursor()
#         sql = "SELECT cadastra_produto('" + p.codigo + "', '" + p.produto + "', '', '" + p.ref + "', 0.0, '', '');"
#         print(sql)
#         cur.execute(sql)
#         conn.commit()
#         cur.close()
#         conn.close()
#         print("Salvou 1")