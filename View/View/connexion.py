from collections import UserDict
from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox
import UserClass as user
import SQLConnection as monsql


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("ddd")
        self.root.geometry("1520x1900+0+0")
        self.mydb = monsql.SQLConnection.getSQLConnection()

        def getval2(): 
            email = self.txt_email.get()
            mp = self.txt_pass_.get()
            recupy=user.ManageUser.Seconnecter(self,email,mp) 
            rec=user.ManageUser.getid()
            if rec == None:
                return 0
            else:
                self.root.destroy()                
                import acceuil                

        
        def returnregister():
            call(["python", "View/View/Register.py" ])

        left_lbl=Label(self.root,bg="#008B8B",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl=Label(self.root,bg="#2F4F4F",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)

        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)

        title=Label(login_frame, text="LOGIN HERE", font=("time new roman",30,"bold"),bg="white",fg="#008B8B").place(x=250,y=50)
             
        email=Label(login_frame, text="EMAIL ADDRESS", font=("time new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=150)
        self.txt_email=Entry(login_frame, font=("time new roman",15),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35)

        pass_=Label(login_frame, text="PASSWORD", font=("time new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=250)
        self.txt_pass_=Entry(login_frame, font=("time new roman",15),bg="lightgray")
        self.txt_pass_.place(x=250,y=280,width=350,height=35)

        btn_reg=Button(login_frame,cursor="hand2",text="Registe new Account",font=("times new roman",14),bg="white",fg="green",bd=0,command=returnregister).place(x=250,y=320)
        btn_login=Button(login_frame,text="Login",font=("times new roman",20,"bold"),fg="white",bg="#B00857", cursor="hand2",command=getval2).place(x=250,y=360,width=180,height=40)

#Partie Graphique
#Ma fenetre
root=Tk()
obj=Login(root)
root.mainloop()
