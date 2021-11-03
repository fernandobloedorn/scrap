import csv
import util.file_util as fileUtil
from services.product_service import findAll
from api.google_drive.upload_file import fileUpload
from dotenv import load_dotenv

load_dotenv()

products = findAll()

print("Produtos " + str(products.__len__()))

# if products.__len__() > 0:
#     fileUtil.productsToCsv("estoque_embramaco.csv", products)
fileUpload("estoque_embramaco.csv", "csv/embramaco.csv")
