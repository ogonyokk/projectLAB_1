from tkinter import *
root = Tk()
root.title("Lab-1")

but = Button(root)
but["text"] = "Печать" 
def printer(event):
    print ("Как всегда очередной 'Hello World!'")
but.bind("<Button-1>",printer)
but.pack(padx=80, pady=3)
root.mainloop()

