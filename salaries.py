from db import db
class salaries(db):
    def create_table(self):
        self.cur.execute("""
                         create table if not exists salaries(
                             id varchar(10) primary key,
                             name varchar(50),
                             salary int,
                             department varchar(20)
                         );
                         """)
        self.commit()
    def insert(self,id,name,salary,department):
        self.cur.execute(
            "insert into salaries(id,name,salary,department) values(%s,%s,%s,%s);",(id,name,salary,department)
        )
        self.commit()
    def read(self):
        self.cur.execute("select*from salaries;")
        return self.cur.fetchall()
    def update(self,id,salary):
        self.cur.execute(
            "update salaries set salary=%s where id=%s;",(salary,id)
        )
        self.commit()
    def delete(self,id):
        self.cur.execute(
            "delete from salaries where id=%s;",(id,)
        )
        self.commit()
    def drop(self):
        self.cur.execute(
            "drop table if exists salaries;"
        )
        self.commit()