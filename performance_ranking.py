from db import db
class performance_ranking_table(db):
    def create_table(self):
        self.cur.execute("""
                         create table if not exists performance_ranking_table(
                           id varchar(10) primary key,
                           name varchar(20) not null,
                           rank int 
                         );
                         """)
    
        self.commit()
    def insert(self,id,name,rank):
        self.cur.execute(
            "insert into performance_ranking_table(id,name,rank) values(%s,%s,%s);",(id,name,rank)
            # f"insert into performance_ranking_table(id,name,rank) values({id},{name},{rank});"
            #"insert into performance_ranking_table(id,name,rank) values({id},{name},{rank});".format(id=id,name=name,rank=rank)
            )
        self.commit()
        
    def read(self):
        self.cur.execute("select*from performance_ranking_table")
        return self.cur.fetchall()
    def update(self,id,rank):
        self.cur.execute(
        "update performance_ranking_table set rank=%s where id=%s;",(rank,id)
        )
        self.commit()
    def delete(self,id):
        self.cur.execute(
            "delete from performance_ranking_table where id=%s;",(id,)
        )
        self.commit()
    def drop(self):
        self.cur.execute("drop table if exists performance_ranking_table")
        self.commit()