import re
from tkinter import*
import UserClass as user
import SQLConnection as monsql


regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  

class Inscription:

    def check(self,email):   
                if(re.search(regex,email)):   
                    return 1   
                else:   
                    return 0

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


    def __init__(self,root):
        self.root=root
        self.root.title("Fenetre Inscription")
        self.root.geometry("1350x700+80+0")
        self.mydb = monsql.SQLConnection.getSQLConnection()

        def getval():
            name = self.name.get()
            prenom =  self.prenom.get()
            telephone =  self.telephone.get()
            email =  self.email.get()
            mp =  self.mp.get()
            confmp =  self.confmp.get()

            recup=user.ManageUser.addUser(self,name,prenom,telephone,email,mp,confmp) 
        
        
        left_lbl=Label(self.root,bg="#008B8B",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl=Label(self.root,bg="#2F4F4F",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)

        #formulaire
        frame1=Frame(self.root,bg="white")
        frame1.place(x=350,y=100,width=700,height=450)

        title=Label(frame1,text="INSCRIPTION",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=50,y=30)

        self.name=StringVar()
        f_name=Label(frame1,text="NOM",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        txt_fname=Entry(frame1,font=("times new roman",15),textvariable=self.name,bg="lightgray").place(x=50,y=130,width=250)

        self.prenom=StringVar()
        l_name=Label(frame1,text="Prenom",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        txt_lname=Entry(frame1,font=("times new roman",15),textvariable=self.prenom,bg="lightgray").place(x=370,y=130,width=250)

        self.telephone=StringVar()
        telephone=Label(frame1,text="Numero Telephone",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        txt_telephone=Entry(frame1,font=("times new roman",15),textvariable=self.telephone,bg="lightgray").place(x=50,y=200,width=250)
 
        self.email=StringVar()
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        txt_email=Entry(frame1,font=("times new roman",15),textvariable=self.email,bg="lightgray").place(x=370,y=200,width=250)

        self.mp=StringVar()
        password=Label(frame1,text="Mot de passe",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        txt_password=Entry(frame1,font=("times new roman",15),textvariable=self.mp,bg="lightgray").place(x=50,y=340,width=250)

        self.confmp=StringVar()
        confPassword=Label(frame1,text="Confirmer mot de passe",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        txt_confPassword=Entry(frame1,font=("times new roman",15),textvariable=self.confmp,bg="lightgray").place(x=370,y=340,width=250)

    #checkbutton
        chk=Checkbutton(frame1,text="J'accepte les conditions",font=("times new roman",12),bg="white").place(x=50,y=380)
        
    #submit
        btn_login=Button(frame1,text="Enregistrer", font=("times new roman",15,"bold"),bd=0,cursor="hand2",bg="#B00857",command=getval).place(x=400,y=380)            

root=Tk()
obj=Inscription(root)
root.mainloop()
