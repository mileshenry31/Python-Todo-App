from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

root = Tk()
root.geometry('750x500')
root.title('To Do App')
frm = ttk.Frame(root, padding=10)
frm.grid()



def add_clicked():
    showinfo(
        title='Information',
        message='Button clicked'
    )




ttk.Button(frm, text='Add a todo', command=add_clicked).grid(column=0, row=0)

root.mainloop()