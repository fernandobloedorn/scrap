
def saveOrUpdate(produtos):
    createOrReplaceFunction()
    for p in produtos:
        print(p.codigo, p.produto)

def createOrReplaceFunction():
    print('Create 2')
