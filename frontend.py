from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from backend import readFile, writeFile
from security import hillCipher

class application():
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Assign#1.3")
        self.root.geometry('400x300')
        self.root.eval("tk::PlaceWindow . center")

        self.PasswordScreen()
           
    def PasswordScreen(self):
        self.PasswordScreen = Frame(self.root)
        self.PasswordScreen.grid()
        
        Label(self.root, text='password').place(relx=0.5, rely=0.1, anchor=CENTER)
        self.password = Text(self.root, height=2, width=50)
        self.password.place(rely=0.12)

        self.selectTxtButton = Button(self.root,text='Origin file', command=self.select_fileTxt)
        self.selectTxtButton.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.selectOooButton = Button(self.root,text='Hash File', command=self.select_fileOOO)
        self.selectOooButton.place(relx=0.6, rely=0.3, anchor=CENTER)
        self.encrypButton = Button(self.root,text='Encry', command=lambda: self.encrypt()).place(relx=0.4, rely=0.4, anchor=CENTER)
        self.decrypButton = Button(self.root,text='Decry', command=lambda: self.decrypt()).place(relx=0.6, rely=0.4, anchor=CENTER)
        self.root.mainloop()

    @property
    def get_pass(self):
        print(self.password.get("1.0","end-1c"))
        return self.password.get("1.0","end-1c")
    
    def select_fileTxt(self):
        filetypes = (('text files', '*.txt'),('All files', '*.*'))
        self.OriginFile = fd.askopenfilename(title='Open a file',initialdir="Securitypass",filetypes=filetypes)
        print(self.OriginFile)
        self.data = readFile(self.OriginFile)
        self.selectTxtButton.configure(bg='powder blue')


    def select_fileOOO(self):
        filetypes = (('text files', '*.ooo'),('All files', '*.*'))
        self.HashFile = fd.askopenfilename(title='Open a file',initialdir="Securitypass",filetypes=filetypes)
        print(self.HashFile)
        self.data_encry = readFile(self.HashFile)
        self.selectOooButton.configure(bg='powder blue')

    def encrypt(self):
        try:
            self.hill = hillCipher(self.get_pass)
            cipher = []
            for m in self.data:
                cipher.append(self.hill.encrypt(m))
            newName = self.OriginFile.replace('.txt', '.ooo')
            writeFile(newName,cipher)
        except:
            messagebox.showerror("Error", "No file selected or password error")
    
    def decrypt(self):
        try:
            plaint = []
            for m in self.data_encry:
                plaint.append(self.hill.decrypt(m))
            newName = self.HashFile.replace('.ooo', 'new.txt')
            writeFile(newName,plaint)
        except:
            messagebox.showerror("Error", "No file selected or password error")
    
a = application()