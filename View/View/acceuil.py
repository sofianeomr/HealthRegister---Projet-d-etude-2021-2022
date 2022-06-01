#Les Bibliotheque a importer
from cProfile import label
from collections import UserList
from logging import root
from tkinter import ttk, Tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
import mysql.connector
import tkinter as tk
import UserClass as user
import SQLConnection as monsql
from tkinter import messagebox


class Patientaccueil:
   
    def __init__(self,root):
        self.root=root
        self.root.title("Patient Management System")
        self.root.geometry("1520x1900+0+0")
        self.mydb = monsql.SQLConnection.getSQLConnection()

        def information(ev):
            cursors_row=table.focus()
            contents = table.item(cursors_row)
            row = contents["values"]
            self.idpat=row[0]
            self.txtCQ.insert(1,row[1])
            self.txtnom.insert(2,row[2])
            self.txtdate.insert(3,row[3])
            self.txtprenom.insert(4,row[4])
            self.txtadresse.insert(5,row[5])
            self.txtTelephone.insert(6,row[6])
            self.txtSexeMasculin.insert(7,row[7])            
            return self.idpat 

        def modifier():
            myCursor = self.mydb.cursor()
            myCursor.execute("update patient set nom_patient=%s, prenom_patient=%s, date_de_naissance=%s, adresse=%s, sexe=%s, telephone=%s,numeroSecu=%s,id_medecin=%s where id_patient=%s", (self.txtnom.get(),self.txtprenom.get(), self.txtdate.get(), self.txtadresse.get(), self.txtSexeMasculin.get(), self.txtTelephone.get(),self.txtCQ.get(),x,self.idpat))
            self.mydb.commit()
            messagebox.showinfo("information",  "ajouté")            
            re=refresh()

        def calendaropen():
            import calendarController

        def refresh():
            self.__init__(root)
            
        def getval3():
            cq =self.txtCQ.get()
            nom = self.txtnom.get()
            prenom = self.txtprenom.get()
            date = self.txtdate.get()
            sexe =self.txtSexeMasculin.get() 
            adresse = self.txtadresse.get()
            telephone = self.txtTelephone.get()
            id_medecin=x
            recup=user.ManagePatient.AjouterPatient(self,nom,prenom,date,adresse,sexe,telephone,cq,id_medecin) 
            re=refresh()
        
        x=user.ManageUser.getid()
        y=user.ManageUser.getNom()
        z=user.ManageUser.getPrenom()
        self.idpat=0

        #titre
        lbltitre = Label(root, text= y+' '+z, borderwidth = 3, relief = SUNKEN, font = ("Sans Serif", 25,'bold'), background = "#2F4F4F", fg="#FFFAFA")
        lbltitre.place(x = 0, y = 0, width = 1850, height=100)
   
        lblCQ = Label(root, text="NUMERO DE SECURITE SOCIAL", font=("Arial", 8), bg="#091821", fg="white")
        lblCQ.place(x=180, y=150, width=150, height=30)
        self.txtCQ = Entry(root,bd=4, font=("Arial", 14))
        self.txtCQ.place(x=350,y=150,width=300)

        #Nom
        lblnom = Label(root, text="NOM", font=("Arial", 18), bg="#091821", fg="white")
        lblnom.place(x=180, y=200, width=150)
        self.txtnom = Entry(root,bd=4, font=("Arial", 14))
        self.txtnom.place(x=350,y=200,width=300)

        #Prenom
        lblprenom = Label(root, text="PRENOM", font=("Arial", 18), bg="#091821", fg="white")
        lblprenom.place(x=180, y=250, width=150, )
        self.txtprenom = Entry(root,bd=4, font=("Arial", 14))
        self.txtprenom.place(x=350,y=250,width=300)

        #DateDeNaissance
        lbldate = Label(root, text="DATE DE NAISSANCE", font=("Arial", 8), bg="#091821", fg="white")
        lbldate.place(x=180, y=300, width=150, height=30)
        self.txtdate = Entry(root,bd=4, font=("Arial", 14))
        self.txtdate.place(x=350,y=300,width=300)

        #sexe
        lblsexe = Label(root, text="SEXE", font=("Arial", 18), bg="#091821", fg="white")
        lblsexe.place(x=180, y=350, width=150, )
        
        self.txtSexeMasculin = Entry(root,bd=4, font=("Arial", 14))
        self.txtSexeMasculin.place(x=350, y=350, width=130)

        #Adresse
        lblAdresse = Label(root, text="ADRESSE", font=("Arial", 18), bg="#091821", fg="white")
        lblAdresse.place(x=180, y=400, width=150)
        self.txtadresse = Entry(root,bd=4, font=("Arial", 14))
        self.txtadresse.place(x=350, y=400, width=300)

        #Telephone
        lblTelephone = Label(root, text="TELEPHONE", font=("Arial", 18), bg="#091821", fg="white")
        lblTelephone.place(x=180, y=450, width=150, )
        self.txtTelephone = Entry(root,bd=4, font=("Arial", 14))
        self.txtTelephone.place(x=350,y=450,width=300)


        #Enregistrer
        btnenregistrer = Button(root, text = "Enregistrer", font = ("Arial", 16),bg = "#D2691E", fg = "white", command=getval3)
        btnenregistrer.place(x=400, y= 550, width=200)

        btnCalendar = Button(root, text = "Rendez vous", font = ("Arial", 16),bg = "#D2691E", fg = "white", command=calendaropen)
        btnCalendar.place(x=400, y= 600, width=200)

        #modifier
        btnmodofier = Button(root, text = "Modifier", font = ("Arial", 16),bg = "#D2691E", fg = "white", command=modifier )
        btnmodofier.place(x=400, y= 650, width=200)

      #Table
        table = ttk.Treeview(root, columns = (1, 2, 3, 4, 5, 6, 7,10), height = 5, show = "headings")
        table.place(x = 750,y = 150, width = 700, height = 450)

        #Entete
        table.heading(1 , text = "ID")
        table.heading(2 , text = "NOM")
        table.heading(3 , text = "PRENOM")
        table.heading(4 , text = "DATE DE NAISSANCE")
        table.heading(5 , text = "ADRESSE")
        table.heading(6 , text = "SEXE")
        table.heading(7 , text = "TELEPHONE")
        table.heading(10, text = "NUMERO SECU")

        #definir les dimentions des colonnes
        table.column(1,width = 5)
        table.column(2,width = 10)
        table.column(3,width = 15)
        table.column(4,width = 20)
        table.column(5,width = 25)
        table.column(6,width = 30)
        table.column(7,width = 35)
        table.column(10,width = 40)

        table.bind("<ButtonRelease-1>",information)

        #Execution
        myCursor = self.mydb.cursor()
        sql="select * from patient where id_medecin="+str(x)
        myCursor.execute(sql)
        myresult= myCursor.fetchall()
        for row in myresult:
            table.insert('', END, value = row,)
        root.mainloop() 

   
root=Tk()
obj=Patientaccueil(root)
root.mainloop()
