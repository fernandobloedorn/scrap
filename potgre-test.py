hostname = 'localhost'
username = 'python'
password = 'c0d4@2021!'
database = 'mais_trading'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT id, name FROM cliente" )

    for id, name in cur.fetchall() :
        print( id, name )


print( "Using psycopg:" )
import psycopg
myConnection = psycopg.connect( host=hostname, user=username, password=password, dbname=database )
doQuery( myConnection )
myConnection.close()
