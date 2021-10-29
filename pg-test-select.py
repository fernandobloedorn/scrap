import os
from dotenv import load_dotenv
from services.product_service import saveOrUpdate
from services.connection_service import getConnection
from models.product import Product

load_dotenv()

conn = getConnection()
cur = conn.cursor()
cur.execute("SELECT id FROM produto WHERE codigo = '12'")

if cur.fetchone() is not None:
    id = cur.fetchone()
    print(type(id))

# for id in cur.fetchall() :
#     print(type(id))
#     print("ID:", id )

cur.close()
conn.close()

