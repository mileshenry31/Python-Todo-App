from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('750x500')
root.title('To Do App')


frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Button(frm, text='Add a todo')
if __name__ == '__main__':
    root.mainloop()