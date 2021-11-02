import csv
import util.file_util as fileUtil
from services.product_service import findAll
from dotenv import load_dotenv

load_dotenv()

products = findAll()

print("Produtos " + str(products.__len__()))

if products.__len__() > 0:
    fileUtil.productsToCsv("embramaco.csv", products)