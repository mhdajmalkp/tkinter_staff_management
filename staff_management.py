import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *


#REFREHSIG LIST start
def connection():
    conn = mysql.connector.connect(host="localhost", user="root", password="ajkp", database="payroll")

    return conn


def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registation")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results



def refreshTable():


    for data in listBox.get_children():
        listBox.delete(data)

    for array in read():
        listBox.insert(parent='', index='end', iid=array, text="", values=(array))

#REFRESHING LIST END HERE




#getting values to entry
def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['ID'])
    e2.insert(0, select['NAME'])
    e3.insert(0, select['MOBILE NO'])
    e4.insert(0, select['SALARY'])


#add function
def Add():
    studid = e1.get()

    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ajkp", database="payroll")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO  registation (id,empname,mobile,salary) VALUES (%s, %s, %s, %s)"
        val = (studid, studname, coursename, feee)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Employee inserted successfully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()
    refreshTable()

#Update function


def update():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ajkp", database="payroll")
    mycursor = mysqldb.cursor()

    try:
        sql = "Update  registation set empname= %s,mobile= %s,salary= %s where id= %s"
        val = (studname, coursename, feee, studid)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Updateddddd successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()

    refreshTable()


#search function


def search():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()


    conn = connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Registation WHERE id='" + studid +"'or empname='" + studname + "'or mobile='" + coursename + "'or salary='"+feee+"'")

    try:
        result = cursor.fetchall()
        for x in result:
            print(x)
        e1.delete(0, END)
        e1.insert(END, x[0])
        e2.delete(0, END)
        e2.insert(END, x[1])
        e3.delete(0, END)
        e3.insert(END, x[2])
        e4.delete(0, END)
        e4.insert(END, x[3])


    except:
        messagebox.showinfo("Error", "No data found")



#delete function



def delete():
    studid = e1.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ajkp", database="payroll")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from registation where id = %s"
        val = (studid,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Deleteeeee successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()
    refreshTable()



# adding item to list
def show():

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="ajkp", database="payroll")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id,empname,mobile,salary FROM registation")
    records = mycursor.fetchall()
    print(records)

    for i, (id, stname, course, fee) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id, stname, course, fee))
        mysqldb.close()


#main
root = Tk()
root.geometry("975x550")
root.configure(bg="cornflowerblue")
root.title("Staff Management")
root.resizable(False,False)
global e1
global e2
global e3
global e4

img=PhotoImage(file='D:\\py tkinter\\calculator\\log.png')
root.iconphoto(False,img)


tk.Label(root, text="Employee ID",background="cornflowerblue",font='poppins 12 bold').place(x=100, y=350)
Label(root, text="Employee Name",background="cornflowerblue",font='poppins 12 bold').place(x=500, y=350)
Label(root, text="Mobile",background="cornflowerblue",font='poppins 12 bold').place(x=100, y=400)
Label(root, text="Salary",background="cornflowerblue",font='poppins 12 bold').place(x=500, y=400)

e1 = Entry(root,font='poppins 12 ')
e1.place(x=260, y=350,width=200,height=30)

e2 = Entry(root,font='poppins 12 ')
e2.place(x=670, y=350,width=200,height=30)

e3 = Entry(root,font='poppins 12 ')
e3.place(x=260, y=400,width=200,height=30)

e4 = Entry(root,font='poppins 12 ')
e4.place(x=670, y=400,width=200,height=30)
fonts=("popins-bold",10)
Button(root, text="ADD",command=Add, height=1, width=10,font='poppins 13 bold').place(x=120, y=475)
Button(root, text="UPDATE",command=update,height=1, width=10,font='poppins 13 bold').place(x=320, y=475)
Button(root, text="SEARCH",command=search ,height=1, width=10,font='poppins 13 bold').place(x=520, y=475)
Button(root, text="DELETE",command=delete, height=1, width=10,font='poppins 13 bold').place(x=720, y=475)

style= ttk.Style()
style.theme_use("clam")
style.configure("Treeview",background = "#E8E8E8",foreground="black",rowheight=25,fieldbackground="white")
style.configure('Treeview.Heading', background="#8FBC8F",font=('poppins',10),)



style.map('Treeview',background=[('selected','blue')])


# creating tree view means cols
cols = ('ID', 'NAME', 'MOBILE NO', 'SALARY')
listBox = ttk.Treeview(root, columns=cols, show='headings')



for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=3,rowspan=3)
    listBox.place(x=80, y=40)
    listBox.tag_configure('orow', background='silver', font=('popins', 12))









show()
listBox.bind('<Double-Button-1>', GetValue)
"""
menus = Menu(root)
root.config(menu=menus)

option_menu = Menu(menus)
menus.add_cascade(label="File", menu=option_menu)

option_menu.add_separator()
option_menu.add_command(label="Exit",command=root.quit)
"""
root.mainloop()

