from db import db
class designation_table(db):
    def create_table(self):
        self.cur.execute("""
                         create table if not exists designation_table(
                             id varchar(10) primary key,
                             name varchar(20) not null,
                             designation varchar(50) not null,
                             department varchar(20)
                             );
                         """)
        self.commit()
    
    def insert(self,id,name,designation,department):
        self.cur.execute(
            "insert into designation_table(id,name,designation,department) values(%s,%s,%s,%s);",(id,name,designation,department)
        )
        self.commit()
        
    def read(self):
        self.cur.execute("select*from designation_table;")
        return self.cur.fetchall()
    def delete(self,id):
        self.cur.execute(
            "delete from designation_table where id=%s;",(id,)
        )
        self.commit()
    def drop(self):
        self.cur.execute(
            "drop table if exists designation_table;"
        )
        self.commit()
    