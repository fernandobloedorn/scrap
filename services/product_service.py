from .connection_service import getConnection
import util.date_util as dateUtil

SELECT_PRODUCT = "SELECT id FROM produto WHERE codigo = %s;"
INSERT_PRODUCT = "INSERT INTO produto (codigo, nome_tecnico, referencia, linha, dt_cadastro, dt_alteracao) VALUES( %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP) RETURNING id;"
UPDATE_PRODUCT = "UPDATE produto SET nome_tecnico = %s, referencia = %s, linha = %s, dt_alteracao = CURRENT_TIMESTAMP WHERE id = %s;"

SELECT_LOT = "SELECT id FROM produto_lote WHERE produto_id = %s AND lote = %s;"
INSERT_LOT = "INSERT INTO produto_lote (produto_id, lote, saldo_cdi, saldo_embramaco, dt_programacao, dt_cadastro, dt_alteracao) VALUES( %s, %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP) RETURNING id;"
UPDATE_LOT = "UPDATE produto_lote SET saldo_cdi = %s, saldo_embramaco = %s, dt_programacao = %s, dt_alteracao = CURRENT_TIMESTAMP WHERE id = %s;"

SELECT_LOT_INVENTORY = "SELECT id FROM produto_lote_saldo WHERE produto_lote_id = %s AND dt_estoque = %s;"
INSERT_LOT_INVENTORY = "INSERT INTO produto_lote_saldo (produto_lote_id, saldo_cdi, saldo_embramaco, dt_estoque) VALUES( %s, %s, %s, %s) RETURNING id;"
UPDATE_LOT_INVENTORY = "UPDATE produto_lote_saldo SET saldo_cdi = %s, saldo_embramaco = %s WHERE id = %s;"

SELECT_PRODUCT_JOIN_LOT = """SELECT produto.codigo, produto.nome_tecnico nome,  produto.linha, produto.referencia, 
                          produto_lote.lote, produto_lote.saldo_cdi, produto_lote.saldo_embramaco, produto_lote.dt_programacao 
                          FROM produto JOIN produto_lote on produto.id = produto_lote.produto_id 
                          WHERE produto_lote.dt_alteracao >= %s
                          ORDER BY produto.codigo, produto_lote.lote LIMIT 10;"""

def saveOrUpdate(products):
    
    insertProduct = 0
    updateProduct = 0
    insertLot = 0
    updateLot = 0
    insertLotInventory = 0
    updateLotInventory = 0

    idProduct = None 
    
    conn = getConnection()
    cur = conn.cursor()

    for product in products:

        cur.execute(SELECT_PRODUCT, (product.code,))
        result = cur.fetchone()

        if result is not None:
            idProduct = result[0]
            cur.execute(UPDATE_PRODUCT, (product.name, product.reference, product.line, idProduct))
            conn.commit()
            updateProduct += 1

        else:
            cur.execute(INSERT_PRODUCT, (product.code, product.name, product.reference, product.line))
            conn.commit()
            idProduct = cur.fetchone()[0]
            insertProduct += 1

        if idProduct is not None:
            cur.execute(SELECT_LOT, (idProduct, product.lot))
            result = cur.fetchone()

            idLot = None 

            if result is not None:
                idLot = result[0]
                cur.execute(UPDATE_LOT, (product.inventory_cdi, product.inventory_embraco, product.programation, idLot))
                conn.commit()
                updateLot += 1

            else:
                cur.execute(INSERT_LOT, (idProduct, product.lot, product.inventory_cdi, product.inventory_embraco, product.programation))
                conn.commit()
                idLot = cur.fetchone()[0]
                insertLot += 1

            if idLot is not None:

                date = dateUtil.today()

                cur.execute(SELECT_LOT_INVENTORY, (idLot, date))
                result = cur.fetchone()

                if result is not None:
                    idLotInventory = result[0]
                    cur.execute(UPDATE_LOT_INVENTORY, (product.inventory_cdi, product.inventory_embraco, idLotInventory))
                    conn.commit()
                    updateLotInventory += 1

                else:
                    cur.execute(INSERT_LOT_INVENTORY, (idLot, product.inventory_cdi, product.inventory_embraco, date))
                    conn.commit()
                    insertLotInventory += 1



            # print(p.codigo, "-", p.produto)
        
        # sql = "SELECT cadastra_produto('" + p.codigo + "', '" + p.produto + "', '', '" + p.ref + "', 0.0, '', '');"
        # print(sql)
        # cur.execute(sql)
        # conn.commit()

    cur.close()
    conn.close()

    print("Produtos -> Novos:", insertProduct, "- Atualizados:", updateProduct)
    print("Lotes -> Novos:", insertLot, "- Atualizados:", updateLot)
    print("Data estoque -> Novos:", insertLotInventory, "- Atualizados:", updateLotInventory)

def findAll():
    products = []
    conn = getConnection()
    cur = conn.cursor()

    cur.execute(SELECT_PRODUCT_JOIN_LOT, ("2021-11-02 00:00:00",))

    for row in cur.fetchall():
        print( "Codigo", row[0] )
        print( "Nome", row[1] )

    cur.close()
    conn.close()
    return products


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