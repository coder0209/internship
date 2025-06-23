import psycopg2
from flask import Flask,jsonify
from psycopg2.extras import execute_values
import time
from db import Db
from error_handling import ErrorHandling
app=Flask(__name__)

class CreateTable(Db):
    def create(self):
        try:
            self.cur.execute("""create table if not exists users(
                            id serial primary key, 
                         name varchar(30) not  null,
                         email varchar(50) not null,
                password varchar(50) not null,
                ph varchar(10) not null) 
                         """)
            self.conn.commit()
            self.cur.close()
            self.conn.close()
        except Exception as e:
            print("Error creating table!!",e)
class Test(Db):
    def insert(self):
        values = []
        for i in range(100000):
            values.append((f'user{i}', f'user{i}@gmail.com'))

        insert_fun = "INSERT INTO users (name, email) VALUES %s"
        try:
            start = time.time()
            execute_values(self.cur, insert_fun, values)
            self.conn.commit()
            end = time.time()

            time_taken = end - start
            data={
                "Success": len(values),
                "in time": time_taken
            }
            return ErrorHandling.success("Success inserting data.",200,data)

        except Exception as e:
            return ErrorHandling.failure("Error inserting data.",500,e)

        self.cur.close()
        self.conn.close()


@app.route('/test',methods=['GET','POST']) #decorators

def test():
    test=Test()
    response,status=test.insert()
    return jsonify(response),status
    
if __name__ == "__main__":
    create=CreateTable()
    create.create()
    app.run(debug=True)
    