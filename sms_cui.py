from sqlite3 import *
DB_NAME = "manaswarke.db"

def db_setup():
    con = None
    try:
        con = connect(DB_NAME)
        sql = "create table if not exists student(rno int primary key, name text, marks int)"
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print("db and tb done")
    except Exception as e:
        print("db tb issue ", e)
        if con is not None:
            con.rollback()
    finally:
        if con is not None:
            con.close()  # Fixed: changed smpycon to con

db_setup()

while True:
    op = int(input(" 1 new, 2 read, 3 delete and 4 exit "))
   
    if op == 1:
        rno = int(input("enter rno "))
        name = input("enter name ")
        marks = int(input("enter marks "))
        con = None
        try:
            con = connect(DB_NAME)
            sql = "insert into student(rno, name, marks) values (?,?,?)"
            cursor = con.cursor()
            # Fixed: passing query parameters correctly as a tuple
            cursor.execute(sql, (rno, name, marks))
            con.commit()
            print("record created")
        except Exception as e:
            print("create issue ", e)
            if con is not None:
                con.rollback()
        finally:
            if con is not None:
                con.close()


    elif op == 2:
        con = None
        try:
            con = connect(DB_NAME)
            sql = "select rno, name, marks from student"
            cursor = con.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            for d in data:
                print(d)
        except Exception as e:
            print("read issue ", e)
        finally:
            if con is not None:
                con.close()

    elif op == 3:
        # Fixed: Added input request so the program knows which record to delete
        rno = int(input("enter rno to delete "))
        con = None
        try:
            con = connect(DB_NAME)
            sql = "delete from student where rno = ?"
            cursor = con.cursor()
            # Fixed: passing the criteria parameter correctly as a tuple
            cursor.execute(sql, (rno,))
            con.commit()
            print(cursor.rowcount, "record deleted")
        except Exception as e:
            print("create issue ", e)
            if con is not None:
                con.rollback()
        finally:
            if con is not None:
                con.close()

    elif op == 4:
        break


    else:
        print("invalid option")