import sqlite3
import os

filepath = "./"
filename = "users"

class DatabaseHandler:

    def __init__(self):
        global connection
        connection= sqlite3.connect(filepath + filename + ".db")

    def __del__(self):
        if connection:
            connection.commit()
            connection.close()


    def check_db_file(self):
        if not os.path.isfile(filepath):
               os.makedirs(filepath,exist_ok=True)
        connection = sqlite3.connect(filepath + filename + ".db")
        connection.execute("CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, username TEXT, warnings INTEGER)")


    def get_single_row_db(self,query):
        try:
            db = sqlite3.connect(filepath + filename + ".db")
            executed =db.cursor().execute( query )
            row = executed.fetchone()
            return row[0]
        except sqlite3.Error as e:
            print("select error: {}".format(e))


    def get_all_rows_db(self,query):
        try:
            db = sqlite3.connect(filepath + filename + ".db")
            executed =db.cursor().execute( query )
            rows = executed.fetchall()
            return rows
        except sqlite3.Error as e:
            print("select error: {}".format(e))


    def insert_into_db(self,query,data):
        try:
            db = sqlite3.connect(filepath + filename + ".db")
            cr = db.cursor()
            row = cr.execute(query,data)
            db.commit()
            new_row = row.fetchone()
            return new_row
        except sqlite3.Error as e:
            print( "insert into error: {}".format(e))

    def update_db(self, query, arg):
        try:
            db = sqlite3.connect( filepath + filename + ".db" )
            cr = db.cursor()
            row = cr.execute( query, arg )
            db.commit()
            new_row = row.fetchone()
            return new_row
        except sqlite3.Error as e:
            print( "update error: {}".format( e ) )

    def update_db_no_args(self,query):
        try:
            db = sqlite3.connect(filepath + filename + ".db")
            cr = db.cursor()
            cr.execute(query)
            db.commit()
        except sqlite3.Error as e:
            print("delete error: {}".format(e))







