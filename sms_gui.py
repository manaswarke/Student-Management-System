from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *

f = ("Arial", 30, "bold")
DB_NAME = "manaswarke.db"

def mw_to_aw():
       mw.withdraw()
       aw.deiconify()

def aw_to_mw():
       mw.withdraw()
       vw.deiconify()
       read()

def mw_to_vw():
       mw.withdraw()
       vw.deiconify()
       read()

def vw_to_mw():
       vw.withdraw()
       mw.deiconify()

def mw_to_dw():
       mw.withdraw()
       dw.deiconify()

def dw_to_mw():
       dw.withdraw()
       mw.deiconify()

def save():
       rno = int(aw_ent_rno.get())
       name = aw_ent_name.get()
       marks = int(aw_ent_marks.get())
       con = None
       try:
                con = connect(DB_NAME)
                sql = "insert into student (rno, name, marks) values (?,?,?)"
                cursor = con.cursor()
                cursor.execute(sql, (rno, name, marks))
                con.commit()
                print("record created")
                showinfo("success","record created")
                aw_ent_rno.delete(0, END)
                aw_ent_name.delete(0, END)
                aw_ent_marks.delete(0, END)
                aw_ent_rno.focus()
       except Exception as e:
                print("create issue ", e)
                con.rollback()
                showerror("issue ", e)
       finally:
                if con !=None:
                        con.close()
def read():
       vw_st_data.delete("0.0", END)
       con = None
       try:
              con = connect(DB_NAME)
              sql = "select rno, name, marks from student"
              cursor = con.cursor()
              cursor.execute(sql)
              data = cursor.fetchall()
              info = ""
              for d in data:
                      info = info + "\nrno =" +str(d[0]) + "\name = " + str(d[1]) + "\nmarks = " + str(d[2]) + "\n-----"
              vw_st_data.insert(INSERT, info)
       except Exception as e:
              print("read issue ",e)
       finally:
              if con !=None:
                      con.close()

def delete():
    rno = int(dw_ent_rno.get())
    con = None
    try:
        con = connect(DB_NAME)
        sql = "delete from student where rno = ?"
        cursor = con.cursor()
        cursor.execute(sql, (rno,)) 
        con.commit()
        msg = str(cursor.rowcount) + " records deleted"
        showinfo("success", msg)
        dw_ent_rno.delete(0, END)
        dw_ent_rno.focus()
    except Exception as e:
        print("delete issue ", e)
        con.rollback()
        showerror("delete issue ", e)
    finally:
        if con != None:
                con.close()

#main window
mw = Tk()
mw.title("Student Managment System by Manas Warke")
mw.geometry("700x700+300+30")

mw_btn_add = Button(mw, text="Add Student", font=f, width=13, command=mw_to_aw)
mw_btn_view = Button(mw, text="View students", font=f, width=13, command=mw_to_vw)
mw_btn_delete = Button(mw, text="Delete Student", font=f, width=13,
command=mw_to_dw)

mw_btn_add.pack(pady=20)
mw_btn_view.pack(pady=20)
mw_btn_delete.pack(pady=20)


#add window
aw = Toplevel()
aw.title("Create Student ")
aw.geometry("700x700+300+30")

aw_lab_rno = Label(aw, text="Enter Rno", font=f)
aw_ent_rno = Entry(aw, font=f)
aw_lab_name = Label(aw, text="Enter name", font=f)
aw_ent_name = Entry(aw, font=f)
aw_lab_marks = Label(aw, text="Enter marks", font=f)
aw_ent_marks = Entry(aw, font=f)
aw_btn_save = Button(aw, text="Save student", font=f, command=save)
aw_btn_back = Button(aw, text="Back to main", font=f, command=aw_to_mw)

aw_lab_rno.pack(pady=10)
aw_ent_rno.pack(pady=10)
aw_lab_name.pack(pady=10)
aw_ent_name.pack(pady=10)
aw_lab_marks.pack(pady=10)
aw_ent_marks.pack(pady=10)
aw_btn_save.pack(pady=10)
aw_btn_back.pack(pady=10)
aw.withdraw()

#view window
vw = Toplevel()
vw.title("View Student")
vw.geometry("700x700+300+30")

vw_st_data = ScrolledText(vw, font=f, width=26, height=12)
vw_btn_back = Button(vw, text="Back to Main", font=f,command=vw_to_mw)
vw_st_data.pack(pady=10)
vw_btn_back.pack(pady=10)
vw.withdraw()

#delete window
dw = Toplevel()
dw.title("Delete Student")
dw.geometry("700x700+300+30")

dw_lab_rno = Label(dw, text="Enter Rno", font=f)
dw_ent_rno = Entry(dw, font=f)
dw_btn_delete = Button(dw, text="Delete Student", font=f, command=delete)
dw_btn_back = Button(dw, text="Back to Main", font=f, command=dw_to_mw)
dw_lab_rno.pack(pady=10)
dw_ent_rno.pack(pady=10)
dw_btn_delete.pack(pady=10)
dw_btn_back.pack(pady=10)
dw.withdraw()

mw.mainloop()