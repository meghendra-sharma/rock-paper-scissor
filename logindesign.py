from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from database import *
from homewindow import *
class Loginwindow(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,*kwargs)
        self.title("Login")
        self.geometry("900x400")

        self.style = Style()
        self.style.configure("Header.TFrame",background = "blue")
        self.headerframe = Frame(self,style = "Header.TFrame")
        self.headerframe.pack(side = TOP,fill = X)


        self.style.configure("Header.TLabel",background = "blue",foreground = "white",font = (NONE,25))
        self.headerlabel = Label(self.headerframe,text = "WELCOME TO ROCK PAPER SCISSOR",style = "Header.TLabel")
        self.headerlabel.pack(pady = 10)

        self.style.configure("Content.TFrame",background = "white")
        self.contentframe = Frame(self,style = "Content.TFrame")
        self.contentframe.pack(side = TOP,fill = BOTH,expand = TRUE)

        self.style.configure("Create.TFrame",background = "white")
        self.createframe = Frame(self.contentframe,width = 450,style = "Create.TFrame")
        self.createframe.pack(side = LEFT,fill = Y)

        self.style.configure("Login.TFrame",background = "white")
        self.loginframe = Frame(self.contentframe,width = 450,style = "Login.TFrame")
        self.loginframe.pack(side = RIGHT,fill = Y)

        self.style.configure("sub.TFrame",background = "white")
        self.sub1frame = Frame(self.createframe,style = "sub.TFrame")
        self.sub1frame.place(relx = 0.5,rely = 0.5,anchor = CENTER)

        self.style.configure("sub.TFrame",background = "white")
        self.sub2frame = Frame(self.loginframe,style = "sub.TFrame")
        self.sub2frame.place(relx = 0.5,rely = 0.5,anchor = CENTER)


        self.style.configure("label1.TLabel",background = "white",font = (NONE,20))


        self.label1 = Label(self.sub1frame,text = "Create Account:",style ="label1.TLabel" )
        self.label1.grid(row = 0,column = 0,pady = 10)

        self.style.configure("label2.TLabel",background = "white",font = (NONE,20))

        self.label2 = Label(self.sub1frame,text = "Player ID",style ="label2.TLabel")
        self.label2.grid(row = 1,column = 0,pady = 10)

        self.style.configure("label3.TLabel",background = "white",font = (NONE,20))


        self.label3 = Label(self.sub1frame,text = "Name",style ="label3.TLabel")
        self.label3.grid(row = 2,column = 0,pady = 10)

        self.style.configure("label4.TLabel",background = "white",font = (NONE,20))




        self.label4 = Label(self.sub2frame,text = "Enter login details:",style = "label4.TLabel")
        self.label4.grid(row = 0,column = 0,pady = 10)

        self.style.configure("label5.TLabel",background = "white",font = (NONE,20))


        self.label5 = Label(self.sub2frame,text = "Enter your Player ID",style = "label5.TLabel")
        self.label5.grid(row = 1,column = 0,pady = 10,padx = 5)

        self.entry1 = Entry(self.sub1frame)
        self.entry1.grid(row = 1,column = 1,padx = 5)


        self.entry2 = Entry(self.sub1frame)
        self.entry2.grid(row = 2,column = 1,padx = 5)


        self.entry3 = Entry(self.sub2frame)
        self.entry3.grid(row = 1,column = 1,padx = 5)
        self.entry3.focus()

        self.button1 = Button(self.sub1frame,text = "Create",width = 20,command = self.button1click)
        self.button1.grid(row = 3,column = 1,pady = 10)

        self.button2 = Button(self.sub2frame,text = "Login",width = 20,command = self.button2click)
        self.button2.grid(row = 3,column = 1,pady = 10)


    def button1click(self):

        if self.entry1.get() == "" or self.entry2.get() == "":
            showwarning("Warning","INCOMPLETE DETAILS")
        else:
            info = searchscore(self.entry1.get())
            if info == None:
                insertscore(self.entry1.get(),self.entry2.get(),score = 0)
                showinfo("Message","CONGRATULATIONS YOU HAVE REGISTERED SUCCESSFULLY")
            else:
                showwarning("Warning","THIS PLAYER ID ALREADY EXIST")

    def button2click(self):
        if self.entry3.get() == "":
            showwarning("Warning","INCOMPLETE DETAILS")
        else:
            info = searchscore(self.entry3.get())
            if info == None:
                showwarning("Warning","INVALID ID")
            else:
                gamerid = self.entry3.get()
                self.destroy()
                homewindow = Homewindow()
                homewindow.playerid(gamerid)








if __name__ == "__main__":
    loginwindow = Loginwindow()
    loginwindow.mainloop()



