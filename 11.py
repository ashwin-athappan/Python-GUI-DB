from tkinter import *
import mysql.connector

root=Tk()

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
        
lab=Label(root,text="Name :")
lab.pack()
entname=Entry(root,width=20,textvar=textin)
entname.pack()
labl=Label(root,text="usn :")
labl.pack()
entusn=Entry(root,width=20,textvar=textinn)
entusn.pack()
but=Button(root,text="Submit",command=insert)
but.pack()
res=Button(root,text="Show",command=show)
res.pack()

#UPDATE
name=StringVar()
usn=StringVar()
Database()
def updateusn():
    cursor.execute("UPDATE people SET name = %s WHERE usn = %s",(str(name.get()),str(usn.get())))
    connection.commit()
labuname=Label(root, text="Update Name:")
labuname.pack()
enttupdatename=Entry(root,width=20,textvar=name)
enttupdatename.pack()
labusn=Label(root,text="Provide usn Number:")
labusn.pack()
entupdateusn=Entry(root,width=20,textvar=usn)
entupdateusn.pack()
buttupdate=Button(root, text="Update",command=updateusn)
buttupdate.pack()

#DELETE
del1=StringVar()
def det():
    dee=del1.get()
    Database()
    cursor.execute("DELETE FROM `people` WHERE name = %s",(dee,))
    connection.commit()
labdelete=Label(root,text="Delete")
labdelete.pack()
endelete=Entry(root,width=20,textvar=del1)
endelete.pack()
butdel=Button(root,text="Delete",command=det)
butdel.pack()

#DROP TABLE
def drop():
    Database()
    cursor.execute("DROP table people")
    connection.commit()
buttdrop=Button(root, text="Drop Table",command=drop)
buttdrop.pack()


root.mainloop()