from tkinter import *
from AvailableQuestions import *
import shelve

class ViewEditQuestions(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createViewEditQuestions()
        self.availableQuestions()

    def createViewEditQuestions(self):
        ## Add C U Logo
        photo = PhotoImage(file="Images/logo.gif")
        labelLogo = Label(self,image = photo)
        labelLogo.image=photo
        labelLogo.grid(row=0, column=0 )


        ## create AdminOptions button

        butAdminOptions = Button(self, text = "Admin Options", font=("MS", 8, "bold"), height=1, width = 15)
        ##butAdminOptions["command"]=AdminOptions.load()  ## look
        butAdminOptions.grid(row=0, column=8, columnspan=2, sticky = NW, padx=10, pady=5)

        ##sets Category title
        lblCategory = Label(self, text = "Category  ", font=("MS", 12, "bold"))    ### Needs coding
        lblCategory.grid(row = 1, column = 0, columnspan = 6, sticky = W, padx=10, pady=5)

        ##sets title
        lblViewEditQuestions = Label(self, text = "View / Edit Questions  ", font=("MS", 14, "bold"))
        lblViewEditQuestions.grid(row = 2, column = 0, columnspan = 6, sticky = W, padx=10, pady=5)

        # sets currently available label
        lblCurrentlyAvailable = Label(self, text = "(Currently Available Questions)  ", font=("MS", 8, "bold"))
        lblCurrentlyAvailable.grid(row = 3, column = 0, columnspan = 3, sticky = W, padx=10, pady=5)

        #sets up questions listbox
        self.listQ = Listbox(self,height=6)
        scroll = Scrollbar(self, command= self.listQ.yview)
        self.listQ.configure(yscrollcommand=scroll.set)

        #Placed list box next to label and scroll bar after.  Listbox and scrollbar aligned
        #to be next to one another
        self.listQ.grid(row=4, column=0, columnspan=10, sticky=EW, padx=10, pady=5)
        scroll.grid(row=4,column=10,sticky=NS, rowspan=6)

        #inserts required values into listbox inc. empty string at end
        #Need to be added from file input
        ##for item in ["Q1", "Q2", "Q3", "Q4", "Q5", ""]:
            ##self.listQ.insert(END,item)

        #create a labelframe to group q and a

        lblFQandA = LabelFrame(self, bg = "light slate gray")
        lblFQandA.grid(row=10, column = 0, columnspan = 10, sticky = W, padx=10, pady=5)
        #create label for question text box

        lblViewEditQuestion = Label(lblFQandA, text = "Question  ", font=("MS", 8, "bold"), bg="light slate gray", fg = "white")
        lblViewEditQuestion.grid(row = 10, column = 0, columnspan = 10, sticky = W, padx=10, pady=1)

        ##inserts a text box for question

        self.txtViewEditQuestion = Text(lblFQandA, height = 1, width = 40)
        self.txtViewEditQuestion.grid(row =  11, column = 0, columnspan = 10, sticky = W, padx=10, pady=1)

        #create label for answer text box

        lblViewEditAnswer = Label(lblFQandA, text = "Answer  ", font=("MS", 8, "bold"), bg="light slate gray", fg = "white")
        lblViewEditAnswer.grid(row = 12, column = 0, columnspan = 10, sticky = W, padx=10, pady=1)

        ##inserts a text box for editing question

        self.txtViewEditAnswer = Text(lblFQandA, height = 1, width = 40)
        self.txtViewEditAnswer.grid(row =  13, column = 0, columnspan = 10, sticky = W, padx=10, pady=(1,15))
        

        #create a labelframe to group choices

        lblFChoices = LabelFrame(self, bg = "light slate gray")
        lblFChoices.grid(row=14, column = 0, columnspan = 10, sticky = W, padx=10, pady=15)
        #create label for Choices text boxes

        lblViewEditChoices = Label(lblFChoices, text = "Choices  ", font=("MS", 8, "bold"), bg="light slate gray", fg = "white")
        lblViewEditChoices.grid(row = 14, column = 0, columnspan = 9, sticky = W, padx=10, pady=10)

        ##inserts a text box for adding a choice1

        self.txtViewEditChoice1 = Text(lblFChoices, height = 1, width = 40)
        self.txtViewEditChoice1.grid(row =  15, column = 0, columnspan = 10, sticky = W, padx=10, pady=5)

       ##inserts a text box for adding a choice2

        self.txtViewEditChoice2 = Text(lblFChoices, height = 1, width = 40)
        self.txtViewEditChoice2.grid(row =  16, column = 0, columnspan = 10, sticky = W, padx=10, pady=5)

	##inserts a text box for adding a choice3

        self.txtViewEditChoice3 = Text(lblFChoices, height = 1, width = 40)
        self.txtViewEditChoice3.grid(row =  17, column = 0, columnspan = 10, sticky = W, padx=10, pady=(5,15))

        ## create Clear Add button

        butClearEdit = Button(self, text = "Undo Edits", font=("MS", 8, "bold"), height=1, width = 15)
        ##butClearAdd["command"]=self.logout  ## look
        butClearEdit.grid(row=18, column=0, columnspan=2, sticky = W, padx=10, pady=5)

        ## create AddAndUpdate button

        butSaveAndUpdate = Button(self, text = "Save and Update", font=("MS", 8, "bold"), height=1, width = 15, fg = "white", bg = "blue")
        ##butAddAndUpdate["command"]=self.logout  ## look
        butSaveAndUpdate.grid(row=18, column=8, columnspan=2, sticky = E, padx=10, pady=5)

        ##insert available questions

    def availableQuestions(self):
        #this should pull questions from shelve file
        with shelve.open('questiondb') as db:
            klist = list(db.keys())
            for questionID in klist:
                questionText = db[questionID].ent
                self.listQ.insert(END,questionText)



#main
root = Tk()  # call the Tk method
root.title("View/Edit Questions") # set the title
app= ViewEditQuestions(root)    # creates a new instance of the Quiz class
root.mainloop()  # starts window with mainloop method

