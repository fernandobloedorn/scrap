import os
from dotenv import load_dotenv
from services.product_service import saveOrUpdate
from services.connection_service import getConnection
from models.product import Product

load_dotenv()

conn = getConnection()
cur = conn.cursor()
cur.execute("SELECT id FROM produto WHERE codigo = '%s'", ("12"))

for id in cur.fetchall() :
    print("ID:", id )

conn.close()

