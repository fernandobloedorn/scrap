from .connection_service import getConnection

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
        conn = getConnection()
        cur = conn.cursor()
        sql = "SELECT cadastra_produto('" + p.codigo + "', '" + p.produto + "', '', '" + p.ref + "', 0.0, '', '');"
        print(sql)
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        print("Salvou 1")


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
