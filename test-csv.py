
# import csv
import util.file_util as fileUtil
from models.product import Product
  
products = []
product = Product()
product.code = "1"
product.name = "Nome 1"
product.line = "1"
product.reference = "2"
product.lot = "2"
product.inventory_cdi = 0.0
product.inventory_embraco = 0.0
product.programation = "2021-11-02"
products.append(product)

product = Product()
product.code = "2"
product.name = "Nome 2"
product.line = "1"
product.reference = "2"
product.lot = "2"
product.inventory_cdi = 0.0
product.inventory_embraco = 0.0
product.programation = "2021-11-02"
products.append(product)

# field names 
fields = ['Codigo', 'Nome', 'Linha', 'Referencia', 'Lote', 'Saldo_CDI', 'Saldo_embramaco', 'Programacao']   
  
fileUtil.productsToCsv("embramaco.csv", products)

# with open('csv/embramaco.csv', 'w') as f:
      
#     # using csv.writer method from CSV package
#     write = csv.writer(f)
      
#     write.writerow(fields)
#     write.writerows(rows)