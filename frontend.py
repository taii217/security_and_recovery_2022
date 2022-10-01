from cProfile import label
from tkinter import *

class application():
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("TextBox Input")
        self.root.geometry('100x200')
        self.frm = Frame(self.root)
        
        self.frm.grid()
        Label(self.root, text='password').grid(row=0,column=0)
        self.password = Text(self.root)
        self.password.grid(row=0,column=1)

        Label(self.root, text='data').grid(row=1,column=0)
        self.data = Text(self.root)
        self.data.grid(row=1,column=1)

        
        self.button = Button(text='Show', command=lambda: self.get_pass()).grid(row=2,column=10)

        self.root.mainloop()
       
    
    def get_pass(self):
        print(self.password.get("1.0","end-1c"))
        return self.password.get("1.0","end-1c")

    def get_pass(self):
        print(self.data.get("1.0","end-1c"))
        return self.data.get("1.0","end-1c")
        

a = application()