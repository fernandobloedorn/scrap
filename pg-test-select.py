import os
from dotenv import load_dotenv
from services.product_service import saveOrUpdate
from services.connection_service import getConnection
from models.product import Product

load_dotenv()

conn = getConnection()
cur = conn.cursor()

cur.execute("SELECT id FROM produto WHERE codigo = %s", ("12",))

result = cur.fetchone()

if result is not None:
    id = result[0]
    print("ID:", id, "Type:", type(id))
# cur.close()

print("-----------------")

# cur = conn.cursor()
cur.execute("INSERT INTO produto (codigo, nome_tecnico) VALUES( %s, %s) RETURNING id;", ("13", "Teste 13"))
conn.commit()
id = cur.fetchone()[0]
print("ID insert:", id, "Type:", type(id))


# for id in cur.fetchall() :
#     print(type(id))
#     print("ID:", id )

cur.close()
conn.close()

