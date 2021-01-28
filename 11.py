from tkinter import *
import mysql.connector

root=Tk()
root.geometry('410x450')
root.title("DATABASE USING MYSQL AND TKINTER")
root.config(background="greenyellow")

def Database():
    global connection, cursor
    connection = mysql.connector.connect(
                                         host='localhost',
                                         database='lab1',
                                         user='root',
                                         password='1379'
                                         )
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `people`(name TEXT, usn TEXT)")
    connection.commit()

textin=StringVar() # data_type variable_name --> C; variable_name=datatype -->Python
textinn=StringVar()

def insert():
    Database()
    cursor.execute("INSERT INTO `people`(name, usn) VALUES(%s,%s)",(str(textin.get()),str(textinn.get())))
    connection.commit()
    #INSERT INTO TABLE_NAME VALUES (name 'priya',)
    

def show():
    Database()
    cursor.execute("SELECT * FROM people")
    for row in cursor.fetchall():
        print(row)
        
lab=Label(root,text="Name")
lab.place(x=0,y=0)
entname=Entry(root,width=20,textvar=textin)
entname.place(x=80,y=0)
labl=Label(root,text="usn")
labl.place(x=0,y=40)
entusn=Entry(root,width=20,textvar=textinn)
entusn.place(x=80,y=40)
but=Button(root,padx=2,pady=2,text="Submit",command=insert)
but.place(x=60,y=100)
res=Button(root,padx=2,pady=2,text="Show",command=show)
res.place(x=160,y=100)

#UPDATE
name=StringVar()
usn=StringVar()
Database()
def updateusn():
    cursor.execute("UPDATE people SET name = %s WHERE usn = %s",(str(name.get()),str(usn.get())))
    connection.commit()
labuname=Label(root, text="Update Name:")
labuname.place(x=0,y=200)
enttupdatename=Entry(root,width=20,textvar=name)
enttupdatename.place(x=160,y=200)
labusn=Label(root,text="Provide usn Number:")
labusn.place(x=0,y=240)
entupdateusn=Entry(root,width=20,textvar=usn)
entupdateusn.place(x=210,y=240)
buttupdate=Button(root, padx=2, pady=2, text="Update",command=updateusn)
buttupdate.place(x=80,y=280)

#DELETE
del1=StringVar()
def det():
    dee=del1.get()
    Database()
    cursor.execute("DELETE FROM `people` WHERE name = %s",(dee,))
    connection.commit()
labdelete=Label(root,text="Delete")
labdelete.place(x=0,y=340)
endelete=Entry(root,width=20,textvar=del1)
endelete.place(x=90,y=340)
butdel=Button(root,padx=2,pady=2,text="Delete",command=det)
butdel.place(x=90,y=380)

#DROP TABLE
def drop():
    Database()
    cursor.execute("DROP table people")
    connection.commit()
buttdrop=Button(root, padx=2, pady=2, text="Drop Table",command=drop)
buttdrop.place(x=180,y=380)


root.mainloop()