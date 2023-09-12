from tkinter import *
from tkinter import ttk


def show_message():
    label["text"] = entry.get()    
root = Tk()
root.title("Lab-2")
root.geometry("250x200")
root.configure(bg='beige')
entry = ttk.Entry()
entry.pack(anchor=NW, padx=70, pady=10)
btn = ttk.Button(text=" Нажми", command=show_message)
btn.pack(anchor=NW, padx=80, pady=10)
label = ttk.Label()
label.pack(anchor=NW, padx=95, pady=6)


check_var1 = BooleanVar()
check = Checkbutton(root, text='Текст 1', variable=check_var1)
check.pack(anchor=NW, padx=80, pady=1)

check_var2 = BooleanVar()
check = Checkbutton(root, text='Текст 2', variable=check_var2)
check.pack(anchor=NW, padx=80, pady=3)

check_var3 = BooleanVar()
check = Checkbutton(root, text='Текст 3', variable=check_var3)
check.pack(anchor=NW, padx=80, pady=3)


root.mainloop()
