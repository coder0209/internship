from db import db
#from employee import Employee
from address import address
from salaries import salaries
from performance_ranking import performance_ranking_table
from designation import designation_table

def main():
    print("welcome to database management system")
    while True:
        print("1.employee\n2.address\n3.salaries\n4.performance_ranking\n5.designation\n6.exit")
        choice=input("Enter your choice:")
        # if choice=="1":
        #     emp=Employee()
        #     emp.create_table()
        #     while True:
        #         print("1.insert\n2.read\n3.update\n4.delete\n5.drop\n6.exit")
        #         choice=input("Enter choice:")
        #         if choice=="1":
        #             id=input("Enter id:")
        #             name=input("Enter name:")
        #             ph=input("Enter phone:")
        #             emp.insert(id,name,ph)
        #         elif choice=="2":
        #             print(emp.read())
        #         elif choice=="3":
        #             id=input("Enter id:")
        #             name=input("Enter name:")
        #             emp.update(id,name)
        #         elif choice=="4":
        #             id=input("Enter id:")
        #             emp.delete(id)
        #         elif choice=="5":
        #             emp.drop()
        #         elif choice=="6":
        #             break
        #         else:
        #             print("Invalid choice")
        if choice=="2":
            addr=address()
            addr.create_table()
            while True:
                print("1.insert\n2.read\n3.update\n4.delete\n5.drop\n6.exit")
                choice=input("Enter choice:")
                if choice=="1":
                    id=input("Enter id")
                    addre=input("Enter address")
                    city=input("Enter city")
                    addr.insert(id,addre,city)
                elif choice=="2":
                    print(addr.read())
                elif choice=="3":
                    id=input("Enter id:")
                    addre=input("Enter address to update:")
                    addr.update(id,addre)
                elif choice=="4":
                    id=input("Enter the id:")
                    addr.delete(id)
                elif choice=="5":
                    addr.drop()
                elif choice=="6":
                    break
                else:
                    print("Invalid choice")
        elif choice=="3":
            sal=salaries()
            sal.create_table()
            while True:
                print("1.insert\n2.read\n3.update\n4.delete\n5.drop\n6.exit")
                choice=input("enter choice:")
                if choice=="1":
                    id=input("Enter id")
                    name=input("Enter name")
                    salary=int(input("Enter salary"))
                    dep=input("Enter department")
                    sal.insert(id,name,salary,dep)
                elif choice=="2":
                    print(sal.read())
                elif choice=="3":
                    id=input("Enter id")
                    salary=input("Enter salary")
                    sal.update(id,salary)
                elif choice=="4":
                    id=input("Enter id:")
                    sal.delete(id)
                elif choice=="5":
                    sal.drop()
                elif choice=="6":
                    break
                else:
                    print("invalid input")
        elif choice=="4":
            per=performance_ranking_table()
            per.create_table()
            while True:
                print("1.insert\n2.read\n3.update\n4.delete\n5.drop\n6.exit")
                choice=input("enter choice:")
                if choice=="1":
                    id=input("Enter id")
                    name=input("Enter name")
                    rank=int(input("enter rank(1-5)"))
                    per.insert(id,name,rank)
                elif choice=="2":
                    print(per.read())
                elif choice=="3":
                    id=input("Enter id")
                    rank=int(input("Enter rank:"))
                    per.update(id,rank)
                elif choice=="4":
                    id=input("Enter id:")
                    per.delete(id)
                elif choice=="5":
                    per.drop()
                elif choice=="6":
                    break
                else:
                    print("invalid input")
        elif choice=="5":
            des=designation_table()
            des.create_table()
            while True:
                print("1.insert\n2.read\n3.update\n4.delete\n5.drop\n6.exit")
                choice=input("enter choice:")
                if choice=="1":
                    id=input("Enter id:")
                    name=input("Enter name:")
                    deg=input("Enter designation:")
                    dep=input("Enter department:")
                    des.insert(id,name,deg,dep)
                elif choice=="2":
                    print(des.read())
                elif choice=="3":
                    id=input("Enter id:")
                    desg=input("Enter designation:")
                    des.update(id,desg)
                elif choice=="4":
                    id=input("Enter id:")                    
                    des.delete(id)
                elif choice=="5":
                    des.drop()
                elif choice=="6":
                    break
                else:
                    print("invalid input")
if __name__=="__main__":
    main()            
                
                             
                                    