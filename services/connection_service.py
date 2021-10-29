import psycopg
import os

def getConnectin():

    print(os.environ['PG_HOST'], os.environ['PG_USER'], os.environ['PG_PASS'], os.environ['PG_DB'])

    connection = psycopg.connect( host=os.environ['PG_HOST'], user=os.environ['PG_USER'], password=os.environ['PG_PASS'], dbname=os.environ['PG_DB'] )
    return connection