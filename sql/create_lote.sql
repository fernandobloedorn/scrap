CREATE TABLE produto_lote
(
  id serial NOT NULL,
  produto_id NUMERIC(11),
  lote character varying,
  saldo_cdi NUMERIC(15,3),
  saldo_embramaco NUMERIC(15,3),
  dt_cadastro timestamp without time zone,
  dt_alteracao timestamp without time zone
)

CREATE TABLE produto_lote_saldo
(
  id serial NOT NULL,
  produto_lote_id NUMERIC(11),
  saldo_cdi NUMERIC(15,3),
  saldo_embramaco NUMERIC(15,3),
  dt_estoque date
)

SELECT produto.codigo, produto.nome_tecnico nome,  produto.linha, produto.referencia, 
produto_lote.lote, produto_lote.saldo_cdi, produto_lote.saldo_embramaco, produto_lote.dt_programacao
FROM produto 
JOIN produto_lote on produto.id = produto_lote.produto_id 
WHERE produto_lote.dt_alteracao >= '2021-11-02 00:00:00'
ORDER BY produto.codigo, produto_lote.lote 
LIMIT 1;