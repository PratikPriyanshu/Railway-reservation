import pymysql,random
db=pymysql.Connect(host="localhost",database='irctc',user='pratik',passwd='12345')
cur=db.cursor()
def res():
    while True :
        print("WELCOME TO IRCTC ONLINE")
        print()
        print("1. Ticket Reservation",'\n',"2. Check Details",'\n')
        i=input("Enter Your Choices : ")
        if i=="1":
            print("ENTER DETAILS OF PASSENGER:")
            print()
            a=input("Enter the Name ==> ")
            b=int(input("Enter Age ==> "))
            c=input("Enter Sex ==> ")
            d=input("Enter Starting Destination ==> ")
            e=input("Enter your Final Detination ==> ")
            f=input("Enter your Reservation Class ==> ")
            sql="insert into ticket(NAME,AGE,SEX,FR0M,T0,CLASS) values('%s','%s','%s','%s','%s','%s')" %(a,b,c,d,e,f)
            cur.execute(sql)
            db.commit()
            print()
            print(cur.rowcount,'records inserted')
            print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -    --  -  -  -  -  -  -  -  -  -")
            print()
        elif i=="2":
            n=cur.execute("select * from ticket")
            d=cur.fetchall()
            for i in d:
                  print(i,end="\n")
            print()
            print("DETAILS OF",cur.rowcount,"PASSENGERS")
            print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -    --  -  -  -  -  -  -  -  -  -")
        else:
            break
try: 
    n=cur.execute("create table ticket(NAME varchar(25),AGE int,SEX char(1),FR0M varchar(7),T0 varchar(7),CLASS varchar(5))")
    db.commit()
    r=random.random()
    print("Table Created in",r,"sec")
    print()
    res()

except pymysql.err.OperationalError:
    print("Table already exist...")
    print()
    res()