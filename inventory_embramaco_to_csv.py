from services.product_service import findAll

from dotenv import load_dotenv

load_dotenv()

producst = findAll()

print("Produtos " + str(producst.__len__()))
