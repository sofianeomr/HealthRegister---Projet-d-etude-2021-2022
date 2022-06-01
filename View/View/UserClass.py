from collections import UserList
import hashlib
import re
import SQLConnection as monsql
from tkinter import messagebox
from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox

global userList
userList = [] 
global patientList
patientList=[]

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  


class User :
    def __init__(self, idUser,name,prenom,telephone,email,mp) -> None:
        self.idUser = idUser
        self.name = name
        self.prenom = prenom
        self.telephone = telephone
        self.email = email
        self.mp = mp

class ManageUser :
   
    def __init__(self) -> None:
        self.mydb = monsql.SQLConnection.getSQLConnection()

    def check(email):   
        if(re.search(regex,email)):   
            return 1   
        else:   
            return 0

    def addUser(self,name,prenom,telephone,email,mp,confmp)->User:        
        if name=="" or prenom=="" or telephone=="" or mp=="" or confmp=="" :
            messagebox.showwarning("erreur", "veuillez remplir toute les données")

        elif mp != confmp  or len(mp)<8 :
            messagebox.showwarning("erreur", "Le mot de passe et la confirmation du mot de passe doivent etre identique")

        elif self.check(email) == 0:
            messagebox.showwarning("erreur", "L'email n'est pas conforme")

        elif self.verifyUser(name,prenom,telephone,email) != 0:
            messagebox.showwarning("erreur", "Erreur de connexion")

        else:
            encoded=mp.encode()
            pswdHashed = hashlib.sha256(encoded).hexdigest()
            
            myCursor = self.mydb.cursor()
            sql = "INSERT INTO medecin (nom_medecin, prenom_medecin,telephone_medecin,email_medecin,mp_medecin) VALUES (%s,%s,%s,%s,%s)"
            val = (name,prenom,telephone,email,pswdHashed)
            myCursor.execute(sql,(val))
            self.mydb.commit()
            id = myCursor.lastrowid
            user = User(id,name,prenom,telephone,email,pswdHashed)
            messagebox.showinfo("", "Felecitation vous etes inscrit")
            self.userList = user
            self.root.destroy()
            return user


    def verifyUser(self,name,prenom,telephone,email):

        mycursor = self.mydb.cursor(prepared=True)
        sqlQuery = "SELECT * FROM medecin where nom_medecin= %s and prenom_medecin = %s and telephone_medecin = %s and email_medecin = %s "
        val = (name,prenom,telephone,email)
        mycursor.execute(sqlQuery, val)
        myresult = mycursor.fetchall()
        if len(myresult) < 1 :
            return 0
        else:
            return 1

        
    def Seconnecter(self,email,mp):
        if (email == "" or mp == ""):
            messagebox.showerror("erreur", "il faut rentrer les données", parent=self.root)
        else:
            try:      
                encoded=mp.encode()
                pswdHashed = hashlib.sha256(encoded).hexdigest()
                myCursor = self.mydb.cursor()
                sql="SELECT * FROM medecin where email_medecin=%s and mp_medecin=%s"
                val = (email,pswdHashed)            
                myCursor.execute(sql,(val))
                myresult = myCursor.fetchall()

                if len(myresult) == 0:
                    messagebox.showerror("erreur","Cette utilisateur n'existe pas", parent=self.root)
                else:
                    messagebox.showinfo("", "Bienvenue !")
                    for x in myresult:
                        userList.append(User(x[0], x[1], x[2], x[3], x[4], x[5]))                    
                    return userList   

            except Exception as es:
                messagebox.showinfo("", "nn")

    def getid():
        for p in userList:
            return p.idUser

    def getNom():
        for p in userList:
            return p.name

    def getPrenom():
        for p in userList:
            return p.prenom


class Patient :
    def __init__(self, idUser,name,prenom,telephone,email,mp,confmp) -> None:
        self.idUser = idUser
        self.name = name
        self.prenom = prenom
        self.telephone = telephone
        self.email = email
        self.mp = mp
        self.confmp = confmp

class ManagePatient :

    def __init__(self) -> None:
        self.mydb = monsql.SQLConnection.getSQLConnection()
    
   # afficher les informations de la table
    def AjouterPatient(self,nom,prenom,date,adresse,sexe,telephone,cq,id_medecin):
        try:          
            myCursor = self.mydb.cursor()
            sql = "INSERT INTO patient (nom_patient, prenom_patient, date_de_naissance, adresse, sexe, telephone,numeroSecu,id_medecin) VALUES (%s, %s, %s, %s, %s,%s,%s,%s) "
            val = (nom, prenom, date, adresse, sexe, telephone,cq,id_medecin)
            myCursor.execute(sql, val)
            self.mydb.commit()
            messagebox.showinfo("information",  "ajouté")

        except Exception as e:
            print(e)
            #retour