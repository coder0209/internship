import psycopg2
class db:
    def __init__(self):
        self.con=psycopg2.connect(dbname="artha",
                                  user="postgres",
                                  password="saiamruth@123",
                                  host="localhost"
                     )
        self.cur=self.con.cursor()
    def commit(self):
        self.con.commit()#used to save the changes made
    def close(self):
        self.cur.close()
        self.con.close()