from models.product import Product
import util.float_util as floatUtil
import util.date_util as dateUtil

product = Product()

codigo = "TN00661RZA"
produto = "60,00 61034 TELHA"
linha = "Acetinado"
ref = "A"
lote = "0669A-32-1104-21-2A"
saldoCdi = "1.651,20"
saldoEmbramaco = "0,00"
programacao = ""

# print("Saldo:", floatUtil.parse(saldoCdi))

a = dateUtil.parse(programacao)
a = dateUtil.dateToString(a)
# a = dateUtil.today()

print ("The type of the date is now",  type(a))
print ("The date is", a)