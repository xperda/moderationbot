import os
import sqlite3
from utils.config import ConfigLoader

#sqlite 3 database handler
#Reference from https://github.com/snoringninja/niftybot-discord/blob/master/resources/database.py
class DatabaseHandler:
    def __init__(self):
        self.path = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
            )
        )

        self.db = os.path.join(
            self.path,
            ConfigLoader().load_config_setting('Bot','database')
        )

    def connect_db(self):

        try:
            connection = sqlite3.connect(self.db)
        except sqlite3.Error as e:
            print("Connection to database: {0}".format(e))

        return
    #create a database
    def create_db(self,query):
        try:
            db = sqlite3.connect(self.db, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            csr=db.cursor()
            csr.execute(query)
            db.commit()
            db.close()
        except sqlite3.Error as e:
            print("Creating database error: {0}".format(e))

    #create tables
    def create_tables(self,query):
        try:
            db = sqlite3.connect(self.db,detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            csr = db.cursor()
            csr.execute(query)
            db.commit()
            db.close()
        except sqlite3.Error as e:
            print("Creating tables error: {0}".format(e))

    #get a single result from database
    def get_result(self,query):
        try:
            db = sqlite3.connect(self.db, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            csr = db.cursor()
            res = csr.execute(query)
            res.fetchone()
            db.commit()
            db.close()
        except sqlite3.Error as e:
            return print("Database get error:{0}".format(e))
        return res

    #get all result from database
    def get_all_results(self,query,parameters):
        try:
            db = sqlite3.connect(self.db, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            csr = db.cursor()
            res = csr.execute(query)
            res.fetchall()
            db.commit()
            db.close()
        except sqlite3.Error as e:
            return print("Database get error:{0}".format(e))
        return res

    #update database
    def update_database(self,query,parameters):
        try:
            db = sqlite3.connect(self.db, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            csr = db.cursor()
            res = csr.execute(query)
            db.commit()
            db.close()
        except sqlite3.Error as e:
            return print("Database update error:{0}".format(e))
        return res

    #insert into database
    def insert_into_database(self,query,parameters):
        try:
            db = sqlite3.connect(self.db,detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
            csr = db.cursor()
            res = csr.execute(query,parameters)
            row = res.fetchone()
            db.commit()
            db.close()
        except sqlite3.Error as e:
            return print("Database insert error:{0}".format(e))
        return row

