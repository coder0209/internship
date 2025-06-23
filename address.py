from db import db
class address(db):
    def create_table(self):
        self.cur.execute("""
                         create table if not exists address(
                             id varchar(10) primary key,
                             address varchar(100),
                             city varchar(30)
                         );
                         """)
        self.commit()
    def insert(self,id,address,city):
        self.cur.execute(
            "insert into address(id,address,city) values(%s,%s,%s);",(id,address,city)
        )
        self.commit()
    def read(self):
        self.cur.execute("select*from address;")
        return self.cur.fetchall()
    def update(self,id,address):
        self.cur.execute(
            "update address set address=%s where id=%s;",(address,id)
            )
        self.commit()
    def delete(self,id):
        self.cur.execute(
            "delete from address where id=%s;",(id,)
        )
        self.commit()
    def drop(self):
        self.cur.execute(
            "drop table if exists address;"
        )
        self.commit()