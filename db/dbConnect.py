import sqlite3
import pandas as pd

class Backend:

    def __init__(self):
        self.conn = sqlite3.connect('db/dadosESP8266.db')
        self.checkDB()

    def checkDB(self):
        tables = pd.read_sql_query("SELECT name FROM sqlite_schema WHERE type ='table' AND name = 'monitor'", self.conn)
        if(len(tables)==0):
            sqlCreateMonitor = '''
                CREATE TABLE monitor
                        (id char(32) PRIMARY KEY NOT NULL,
                        fonte CHAR(20),
                        data_status_atual   char(20),
                        temperatura NUMERIC,
                        umidade NUMERIC,
                        situacao CHAR(1));
                '''
            self.conn.execute(sqlCreateMonitor)
