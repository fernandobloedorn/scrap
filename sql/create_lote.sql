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