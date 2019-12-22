# SQLite_prospector
The SQLite_prospector is just a code snippet allowing developers to read a database.

## class
importdb - requires a database name while creating an object.

## methods
list_all_tables - To get the list of all the tables in the db
get_schema - requires a table name as an argument, prints the schema of a table.
get_data - requires a table name and query as an argument, prints the data in the table by executing the given query.
           By default prints all the row in the table

## How to use:

1. Download the code.
2. Place the sqlite_prospector.py file in the same folder as the database
   or give the full path of the database while creating the object of importdb as shown below.

'''python
import sqlite_prospector
db_name = 'chinook.db'
imp = importdb(db_name)
imp.list_all_tables()
imp.get_schema('albums')
imp.get_data('albums')
#Can send custom query for data retrieval.
imp.get_data('albums',"select * from %s where ArtistId=50")
'''

'''Note:
A default database 'chinook.db' is also provided in the repo.
The main method is written based on that db for demonstration purposes.
'''
