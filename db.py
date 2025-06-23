import psycopg2

class Db:
    def __init__(self):
        self.conn=psycopg2.connect(
                dbname="artha",
                user="postgres",
                password="saiamruth@123",
                host="localhost")
        self.cur=self.conn.cursor()
        
        
        



