import pymysql
import pymysql.cursors
import os


class DatabaseConnection:
    def __init__(self,host,user,password,database):
        self.host = os.environ.get(host)
        self.user = os.environ.get(user)
        self.password = password
        self.database = database
        self.conn = None
    
    def get_conn(self):
        if self.conn is None:     
            self.conn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                cursorclass=pymysql.cursors.DictCursor
            )
            return self.conn
        else:
            raise Exception('Connection with the database has already been established')
    

    
 