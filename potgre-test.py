# hostname = 'localhost'
# username = 'python'
# password = 'c0d4@2021!'
# database = 'mais_trading'

# PG_HOST=localhost
# PG_USER=python
# PG_PASS=c0d4@2021!
# PG_DB=mais_trading

import os
from dotenv import load_dotenv

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT id, name FROM cliente" )

    for id, name in cur.fetchall() :
        print( id, name )

load_dotenv()

print( "Using psycopg:" )
import psycopg
myConnection = psycopg.connect( host=os.environ['PG_HOST'], user=os.environ['PG_USER'], password=os.environ['PG_PASS'], dbname=os.environ['PG_DB'] )
doQuery( myConnection )
myConnection.close()
