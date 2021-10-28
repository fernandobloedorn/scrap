
def getConnectin():
    connection = psycopg.connect( host=os.environ['PG_HOST'], user=os.environ['PG_USER'], password=os.environ['PG_PASS'], dbname=os.environ['PG_DB'] )
    return connection