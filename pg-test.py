import os
from dotenv import load_dotenv
from services.product_service import saveOrUpdate
from models.product import Product
import util.float_util as floatUtil
import util.date_util as dateUtil

load_dotenv()

# conn = getConnectin()
# cur = conn.cursor()
# cur.execute( "SELECT id, name FROM cliente" )

# for id, name in cur.fetchall() :
#     print( id, name )

# conn.close()

products = []

product = Product()

product.code = "TN00661RZA"
product.name = "60,00 61034 TELHA"
product.line = "Acetinado"
product.reference = "A"
product.lot = "0669A-32-1104-21-2A"
product.inventory_cdi = floatUtil.parse("1.651,20")
product.inventory_embraco = floatUtil.parse("0,00")
product.programation = dateUtil.parse("03/11/2021")

products.append(product)

saveOrUpdate(products)