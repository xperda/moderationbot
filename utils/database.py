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


    def get_single_row_db(self,user_id):
        try:
            db = sqlite3.connect(filepath + filename + ".db")
            cr = db.cursor()
            executed =cr.execute(f'SELECT warnings FROM users WHERE id = {user_id}')
            row = executed.fetchone()
            return row[0]
        except sqlite3.Error as e:
            print("select error: {}".format(e))


    def get_all_rows_db(self):
        query = 'SELECT warnings FROM users'
        try:
            db = sqlite3.connect(filepath + filename + ".db")
            executed =db.cursor().execute( query )
            rows = executed.fetchall()
            return rows
        except sqlite3.Error as e:
            print("select all error: {}".format(e))


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


    def update_db(self,arg,user_id):
        query = f'UPDATE users SET warnings = {arg} WHERE id = {user_id}'
        try:
            db = sqlite3.connect(filepath + filename + ".db")
            cr = db.cursor()
            cr.execute(query)
            db.commit()
        except sqlite3.Error as e:
            print("delete error: {}".format(e))

    def delete_row_db(self,user_id):
        query = f"DELETE FROM users where id = {user_id}"
        try:
            db = sqlite3.connect( filepath + filename + ".db" )
            cr = db.cursor()
            cr.execute( query )
            db.commit()
        except sqlite3.Error as e:
            print( "delete error: {}".format( e ) )







