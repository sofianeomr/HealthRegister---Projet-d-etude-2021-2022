import tkinter as tk
import csv
import sys
import os.path
from tkinter import END, Text, messagebox
from turtle import width
from Calendar import Calendar
import UserClass as user
from tkinter import *


from CalendarView import CalendarView

root = tk.Tk()
root.title("Prise de rendez vous")
#Tikinter Vars
nompatient = tk.StringVar()
name = tk.StringVar()
loggedInLabel = tk.StringVar()
hours = tk.IntVar()
minutes = tk.IntVar()
#Functions

def raiseFrame(frame):
	frame.tkraise()

def moveToBook():
	raiseFrame(bookAppointment)
	# Calendar

	
def makeAppointment():
	#Format date
	date = str(datePickercalendar.day_selected)+"/"+str(datePickercalendar.month_selected)+"/"+str(datePickercalendar.year_selected)
	#Format time
	minutesString=str(minutes.get())
	if minutes.get()==0:
		minutesString = "00"
	time = str(hours.get())+":"+minutesString
	with open ("appointments.txt",'a',newline="") as appFile:
		writer = csv.writer(appFile)
		writeList = [nompatient.get(),date,time]
		writer.writerow(writeList)
		appFile.close()
	messagebox.showinfo("Success!","Appointment made!")
	calendarViewFrame = tk.Frame(userFrame, borderwidth=5, bg="lightblue")
	calendarViewFrame.grid(row=1, column=3, columnspan=5)
	viewCalendar = CalendarView(calendarViewFrame, {name.get()})
	raiseFrame(userFrame)



userFrame = tk.Frame(root)
bookAppointment = tk.Frame(root)
frameList=[userFrame,bookAppointment]
#Configure all (main) Frames
for frame in frameList:
	frame.grid(row=0,column=0, sticky='news')
	frame.configure(bg='lightblue')

tk.Label(bookAppointment,text="Rendez vous",font=("Arial", 30),bg='lightblue').grid(row=1,column=1,columnspan=5)
tk.Label(bookAppointment,text="Date: ",font=("Arial", 20),bg='lightblue').grid(row=2,column=1)
tk.Label(bookAppointment,text="Heure: ",font=("Arial", 22),bg='lightblue').grid(row=3,column=1)
tk.Label(bookAppointment,text="Nom patient: ",font=("Arial", 22),bg='lightblue').grid(row=4,column=1)
tk.Entry(bookAppointment,textvariable=nompatient,font=("Arial", 22),bg='white').grid(row=4,column=2)

tk.Button(bookAppointment,font=("Arial", 15),bg='#D2691E',text="Programmer le RDV",command=lambda :makeAppointment()).grid(row=4,column=4)

#Time Selector
timeSelectFrame = tk.Frame(bookAppointment,borderwidth=5,bg="lightblue")
timeSelectFrame.grid(row=3,column=2)
tk.Spinbox(timeSelectFrame,from_=1, to=24,bg="white",width=2,textvariable=hours).grid(row=1,column=1)
tk.Label(timeSelectFrame,text=":",bg="lightblue").grid(row=1,column=2)
tk.Spinbox(timeSelectFrame,width=2,textvariable=minutes,values=(0,15,30,45),bg="white").grid(row=1,column=3)

def lister():
	text_file = open("appointments.txt", 'r')
	stuff= text_file.read()
	list.insert(END,stuff)
	text_file.close()

def save():
	text_file = open("appointments.txt", 'w')
	text_file.write(list.get(1.0, END))
	messagebox.showerror("", "Felecitation vous etes inscrit")


calendarFrame = tk.Frame(bookAppointment, borderwidth=5, bg="lightblue")
calendarFrame.grid(row=2, column=2, columnspan=5)
datePickercalendar = Calendar(calendarFrame, {})
list = tk.Text(userFrame,width=25, height=8,font=("Helvetica", 16))
list.grid(row=1, column=2)

tk.Button(userFrame,font=("Courier", 22),bg='#D2691E',text="Retour", command=moveToBook).grid(row=4, column=2)
tk.Button(userFrame,font=("Courier", 22),bg='#D2691E',text="Save", command=save).grid(row=4, column=3)
tk.Button(userFrame,font=("Courier", 22),bg='#D2691E',text="Liste patients", command=lister).grid(row=4, column=4)


raiseFrame(bookAppointment)
root.mainloop()