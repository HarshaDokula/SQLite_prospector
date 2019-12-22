import sqlite3
from pprint import pprint



class importdb():
    def __init__(self,db):
        self.db = db
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()

    def list_all_tables(self):
        #To get the list of all the tables in the db
        print("List of all the tables in {}:".format(self.db))
        tables = self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        count = 0
        print("**"*35)
        for table in tables:
            print(table[0])
            count += 1
        print("==>>No of tables in db {}:{}<<==".format(self.db,count))
        print("**"*35)


    def get_schema(self,table_name):
        #Print the schema of a table.
        print("Schema of table {}:".format(table_name))
        print("+="*35)
        self.cur.execute('pragma table_info(%s)'%table_name)
        for col in self.cur.fetchall():
            print(col)
        print("+="*35)


    def get_data(self,table_name,query="SELECT * FROM %s;"):
        #print the full table,by default.
        print("Data from table: {}".format(table_name))
        self.cur.execute(query%(table_name))
        print("##"*35)
        for row in self.cur.fetchall():
            print(row)
            print("--"*25)
        print("##"*35)


def main():
    db_name = 'chinook.db'
    imp = importdb(db_name)
    imp.list_all_tables()
    imp.get_schema('albums')
    imp.get_data('albums')
    #Can send custom query for data retrieval.
    imp.get_data('albums',"select * from %s where ArtistId=50")

if __name__ == '__main__':
    main()
