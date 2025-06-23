import psycopg2
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from psycopg2.extras import execute_values
import time
from db import Db
from error_handling import ErrorHandling
app=FastAPI()
class CreateTable(Db):
    def create(self):
        try:
            self.cur.execute("""
                    CREATE TABLE IF NOT EXISTS users(
                        id serial primary key, 
                        name varchar(30) not null,
                        email varchar(50) not null) 
                  """)
            self.conn.commit()
        except Exception as e:
            print("Error creating table",e)
        self.cur.close()
        self.conn.close()

class Test(Db):
    def insert(self):
        values=[]
        for i in range(100000):
            values.append((f'user{i}',f'user{i}@gmail.com'))

        insert_fun="INSERT INTO users (name,email) VALUES %s"
        try:
            start=time.time()
            execute_values(self.cur,insert_fun,values)
            self.conn.commit()
            end=time.time()

            time_taken = end - start
            data={
                "Success creating":len(values),
                "time taken":time_taken
            }
            return ErrorHandling.success("Successfully inserted data.",200,data)

        except Exception as e:
            return ErrorHandling.failure("Error inserting data.",500,e)

        self.cur.close()
        self.conn.close()

@app.post('/test1')

def test_():
    test=Test()

    response,statuscode=test.insert()
    return JSONResponse(content=response,status_code=statuscode)
@app.get("/test2")
def read_sample():
    db=Db()
    db.cur.execute("SELECT * FROM users LIMIT 10")
    data = db.cur.fetchall()
    db.cur.close()
    db.conn.close()
    return { "sample": data }



createtable=CreateTable()
createtable.create()

