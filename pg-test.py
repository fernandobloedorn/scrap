import os
from dotenv import load_dotenv
from services.produto_service import saveOrUpdate
from services.connection_service import getConnectin
from models.product import Product

load_dotenv()

conn = getConnectin()
cur = conn.cursor()
cur.execute( "SELECT id, name FROM cliente" )

for id, name in cur.fetchall() :
    print( id, name )

conn.close()