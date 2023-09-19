from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Ekinshi okno")
root.geometry("250x200")

master = Tk()
master.geometry('300x200')
master['bg'] = 'white'
master.title("Birinshi okno")

#Birinshi okno

def show_values():
    print (w1.get())

w1 = Scale(master, from_=0, length=750, to=100, tickinterval=10, orient=HORIZONTAL, bg="green", bd=10,)
w1.set(100)
w1.pack()
Button(master, text='Show',bg="green", bd=5, command=show_values).pack()

#okno

fra1 = Frame(master, width=300, height=200, bg="green", bd=20)
fra1.pack()

ent1 = Entry(fra1,width=20)
ent1.pack()


#Ekinshi okno


  
languages = ["Python", "JavaScript", "C#", "Java", "C++", "Rust", "Kotlin", "Swift",
             "PHP", "Visual Basic.NET", "F#", "Ruby", "R", "Go", "C", 
             "T-SQL", "PL-SQL", "Typescript", "Assembly", "Fortran"]
  

root.title("Ekinshi okno")
root.geometry("250x200")
 
 
languages_var = StringVar(value=languages)
listbox = Listbox(listvariable=languages_var)
listbox.pack(side=LEFT, fill=BOTH, expand=1)
  
scrollbar = ttk.Scrollbar(orient="vertical", command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
  
listbox["yscrollcommand"]=scrollbar.set
  
mainloop()
