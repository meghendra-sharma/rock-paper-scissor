from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import random
from database import *
#from logindesign import *
#option = IntVar()
#option.set(1)
class Homewindow(Tk):
    def __init__(self,*args,**kawrgs):
        Tk.__init__(self,*args,**kawrgs)
        self.title("Home")
        self.state("zoomed")

        self.score = 0


        self.style = Style()
        self.style.configure("Header.TFrame",background = "purple")

        self.headerframe = Frame(self,style = "Header.TFrame")
        self.headerframe.pack(fill = X)

        self.style.configure("Header.TLabel",background = "purple",font = (NONE,70),foreground = "white")
        self.headerlabel = Label(self.headerframe,text = "Let's Play",style = "Header.TLabel")
        self.headerlabel.pack()

        self.style.configure("Rules.TFrame",background = "pink")
        self.rulesframe = Frame(self,style = "Rules.TFrame",width = 400)
        self.rulesframe.pack(side = LEFT,fill = Y)

        self.style.configure("Content.TFrame",background = "pink")
        self.contentframe = Frame(self,style = "Content.TFrame")
        self.contentframe.pack(fill = BOTH,expand = TRUE)

        """self.style.configure("Title.TFrame",background = "black")
        self.titleframe = Frame(self,height = 10,style = "Title.TFrame")
        self.titleframe.pack(side = BOTTOM ,fill = X)"""


        self.style.configure("Rules.TLabel",background = "pink",foreground = "black",font = (NONE,15))
        self.ruleslabel = Label(self.rulesframe,text = """RULES:
        
        1. ROCK VS PAPER -> PAPER WINS
        2. ROCK VS SCISSOR -> ROCK WINS
        3. PAPER VS SCISSOR -> SCISSOR WINS
        
        $-EACH TIME YOU WIN
          YOU WILL BE
          AWARDED 2000 POINTS
        
        $-NOTHING WILL BE
          AWARDED
          IF DRAWN
          OR COMPUTER WINS""",style = "Rules.TLabel")
        self.ruleslabel.pack()

        self.style.configure("Main.TLabel",background = "pink",font = (NONE,37),foreground = "black")
        self.label1 = Label(self.contentframe,text = "Choose one between Rock Paper Scissor",style = "Main.TLabel")
        self.label1.pack(pady = 20)
        #self.label1.place(relx = 0.5,rely = 0.5,anchor = CENTER)

        self.option = IntVar()
        self.option.set(0)

        self.style.configure("TRadiobutton",background = "pink",font = (NONE,30))

        self.rockbutton = Radiobutton(self.contentframe,text = "ROCK",value = 1,variable = self.option,style = "TRadiobutton")
        self.rockbutton.pack(pady = 10)

        self.paperbutton = Radiobutton(self.contentframe,text = "PAPER",value = 2,variable = self.option,style = "TRadiobutton")
        self.paperbutton.pack(pady = 10)

        self.scissorbutton = Radiobutton(self.contentframe,text = "SCISSOR",value = 3,variable = self.option,style = "TRadiobutton")
        self.scissorbutton.pack(pady = 10)

        self.style.configure("TButton",font = (NONE,25))
        self.submitbutton = Button(self.contentframe,text = "Submit",command = self.submitbuttonclick,style = "TButton")
        self.submitbutton.pack(pady = 10)

    def submitbuttonclick(self):
        self.compchoice = random.randint(1,3)
        if self.option.get() == 1 and self.compchoice == 1:
            ans = askquestion("Result","""You and Computer both have chosen Rock.
            Its a draw,Do you want to play again?""")
            if ans == "yes":
                self.option.set(0)
            else:
                info = searchscore(self.playerid)
                if self.score <= info[2]:
                    showinfo("Message","You have scored"+" "+ str(self.score))
                else:
                    showinfo("Message","Congratulations you have made a new highscore"+" "+ str(self.score))
                    updatescore(self.playerid,self.score)


        elif self.option.get() == 2 and self.compchoice == 2:
            ans = askquestion("Result","""You and Computer both have chosen Paper.
            Its a draw,Do you want to play again?""")
            if ans == "yes":
                self.option.set(0)
            else:
                info = searchscore(self.playerid)
                if self.score <= info[2]:
                    showinfo("Message","You have scored"+" "+ str(self.score))
                else:
                    showinfo("Message","Congratulations you have made a new highscore"+" "+ str(self.score))
                    updatescore(self.playerid,self.score)


        elif self.option.get() == 3 and self.compchoice == 3:
            ans = askquestion("Result","""You and Computer both have chosen Scissor.
            Its a draw,Do you want to play again?""")
            if ans == "yes":
                self.option.set(0)
            else:
                info = searchscore(self.playerid)
                if self.score <= info[2]:
                    showinfo("Message","You have scored"+" "+ str(self.score))
                else:
                    showinfo("Message","Congratulations you have made a new highscore"+" "+ str(self.score))
                    updatescore(self.playerid,self.score)


        elif self.option.get() == 1 and self.compchoice == 3:
            self.score = self.score + 2000
            ans = askquestion("Result","""You have chosen Rock
            Computer has chosen scissor.
            You win,Do you want to play again?""")
            if ans == "yes":
                self.option.set(0)
            else:
                info = searchscore(self.playerid)
                if self.score <= info[2]:
                    showinfo("Message","You have scored"+" "+ str(self.score))
                else:
                    showinfo("Message","Congratulations you have made a new highscore"+" "+ str(self.score))
                    updatescore(self.playerid,self.score)

        elif self.option.get() == 2 and self.compchoice == 1:
            self.score = self.score + 2000
            ans = askquestion("Result","""You have chosen Paper
            Computer has chosen Rock.
            You win,Do you want to play again?""")
            if ans == "yes":
                self.option.set(0)
            else:
                info = searchscore(self.playerid)
                if self.score <= info[2]:
                    showinfo("Message","You have scored"+" "+ str(self.score))
                else:
                    showinfo("Message","Congratulations you have made a new highscore"+" "+ str(self.score))
                    updatescore(self.playerid,self.score)


        elif self.option.get() == 3 and self.compchoice == 2:
            self.score = self.score + 2000
            ans = askquestion("Result","""You have chosen Scissor
            Computer has chosen Paper.
            You win,Do you want to play again?""")
            if ans == "yes":
                self.option.set(0)
            else:
                info = searchscore(self.playerid)
                if self.score <= info[2]:
                    showinfo("Message","You have scored"+" "+ str(self.score))
                else:
                    showinfo("Message","Congratulations you have made a new highscore"+" "+ str(self.score))
                    updatescore(self.playerid,self.score)

        elif self.option.get() == 1 and self.compchoice == 2:
            self.ans = askquestion("Result","""You have chosen Rock
            Computer has chosen paper .
            Computer wins,Do you want to play again?""")
            if self.ans == "yes":
                self.option.set(0)
            else:
                info = searchscore(self.playerid)
                if self.score <= info[2]:
                    showinfo("Message","You have scored"+" "+ str(self.score))
                else:
                    showinfo("Message","Congratulations you have made a new highscore"+" "+ str(self.score))
                    updatescore(self.playerid,self.score)


        elif self.option.get() == 2 and self.compchoice == 3:
            ans = askquestion("Result","""You have chosen Paper
            Computer has chosen Scissor.
            Computer wins,Do you want to play again?""")
            if ans == "yes":
                self.option.set(0)
            else:
                info = searchscore(self.playerid)
                if self.score <= info[2]:
                    showinfo("Message","You have scored"+" "+ str(self.score))
                else:
                    showinfo("Message","Congratulations you have made a new highscore"+" "+ str(self.score))
                    updatescore(self.playerid,self.score)


        elif self.option.get() == 3 and self.compchoice == 1:
            ans = askquestion("Result","""You have chosen Scissor
            Computer has chosen Rock.
            Computer wins,Do you want to play again?""")
            if ans == "yes":
                self.option.set(0)
            else:
                info = searchscore(self.playerid)
                if self.score <= info[2]:
                    showinfo("Message","You have scored"+" "+ str(self.score))
                else:
                    showinfo("Message","Congratulations you have made a new highscore"+" "+ str(self.score))
                    updatescore(self.playerid,self.score)


        else:
            showwarning("Warning","You haven't chose any option")

    def playerid(self,playerid):
        self.playerid = playerid


#homewindow = Homewindow()
#homewindow.mainloop()
#homewindow.score = 0




