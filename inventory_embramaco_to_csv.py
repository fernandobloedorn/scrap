import csv
import util.file_util as fileUtil
from services.product_service import findAll
from api.google_drive.upload_file import upload_file
from dotenv import load_dotenv

load_dotenv()

products = findAll()

print("Produtos " + str(products.__len__()))

# if products.__len__() > 0:
#     fileUtil.productsToCsv("estoque_embramaco.csv", products)
upload_file("estoque_embramaco.csv")