from tkinter import *
import webbrowser
from MLCipher import MixCipher

class Application(Frame):

    def __init__(self, master):
        """ Initialize the Frame """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        # Title label
        self.instruction = Label(self, text = "Triple Layered Caesar Cipher", font=("arial",17,"bold"))
        self.instruction.grid(row = 1, column = 0, columnspan = 2, padx = 5, sticky = W)

        # Method label
        self.method = Label(self, text = "Choose method:")
        self.method.grid(row = 2, column = 0, columnspan = 2, padx = 5, sticky = W)

        # Method options
        self.var1 = IntVar()

        self.option = Radiobutton(self, text="Encrypt", pady = 5, variable=self.var1, value=1)
        self.option.grid(row = 3, column = 0, columnspan = 1, padx = 5, sticky = W)

        self.option = Radiobutton(self, text="Decrypt", pady = 5, variable=self.var1, value=2)
        self.option.grid(row = 3, column = 1, columnspan = 1, padx = 5, sticky = W)

        # Message label
        self.instruction = Label(self, text = "Enter message: ")
        self.instruction.grid(row = 4, column = 0, columnspan = 150, padx = 5, sticky = W)

        # Message entry
        self.message= Entry(self)
        self.message.grid(row = 5, column = 0, padx = 5, sticky = W)

        # Key label
        self.instruction = Label(self, text = "Enter key : ")
        self.instruction.grid(row = 6, column = 0, columnspan = 2, padx = 5, sticky = W)

        # Key entry
        self.key= Entry(self)
        self.key.grid(row = 7, column = 0, padx = 5, sticky = W)

        # Submit 
        self.submit_button = Button(self, text = "Submit", command = self.mixCip)
        self.submit_button.grid(row = 8, column = 0, padx = 5, sticky = W)

        # Result label
        self.instruction = Label(self, text = "Result", font=("arial",14,"bold"))
        self.instruction.grid(row = 9, column = 0, columnspan = 2, padx = 5, sticky = W)

        # Result 
        self.result = Text(self, width = 45, height = 6, wrap = WORD)
        self.result.grid(row = 10, column = 0, columnspan = 3, padx = 5, sticky = W)

        #Github label
        self.github = Label(self, text = "Visit http://github.com/shubhgaur37", cursor="hand2")
        self.github.bind("<Button-1>", self.githubLink)
        self.github.grid(row = 11, column = 0, columnspan = 3, padx = 5, sticky = W)
    def githubLink(self, event):
        webbrowser.open_new(r"http://github.com/shubhgaur37")
    
    def mixCip(self):
        m = self.message.get()
        k = self.key.get()
        obj=MixCipher(k)
        ch=self.var1.get()
        if (ch)==1:#encrypt
            ciphertext=obj.encrypt(m)
            self.result.delete(0.0, END)
            self.option['set']=None
            self.result.insert(0.0, ciphertext )
            return ciphertext 
        
        else:
            ciphertext=obj.decrypt(m)
            self.result.delete(0.0, END)
            self.option['set']=None
            self.result.insert(0.0, ciphertext )
            return ciphertext 


root = Tk()
root.title("3LFibCaesar")
root.geometry("350x350")
app = Application(root)
root.mainloop()
