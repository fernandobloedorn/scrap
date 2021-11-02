import csv
  
def productsToCsv(file, products): 
    with open('csv/' + file, 'w',) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Codigo', 'Nome', 'Linha', 'Referencia', 'Lote', 'Saldo_CDI', 'Saldo_embramaco', 'Programacao'])
        for product in products:
            writer.writerow([product.code, product.name, product.line, product.reference, product.lot, product.inventory_cdi, product.inventory_embraco, product.programation])
    print("Arquivo gerado com sucesso em csv/" + file)