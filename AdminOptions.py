from tkinter import *


class AdminOptions(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createAdminOptions()
        
    def createAdminOptions(self):

        ## create logout button
        
        butLogout = Button(self, text = "Logout", font=("MS", 8, "bold"), height=1, width = 10)
        ##butLogout["command"]=self.logout  ## look
        butLogout.grid(row=0, column=5, columnspan=2, sticky = NE, padx=5, pady=0)
        
        ## create logo
        photo = PhotoImage(file="Images/logo.gif")
        labelLogo = Label(self,image = photo)
        labelLogo.image=photo
        labelLogo.grid(row=0, column=0 )

        ##sets title
        lblAdminOptions = Label(self, text = "Admin Options  ", font=("MS", 14, "bold"))
        lblAdminOptions.grid(row = 1, column = 2, columnspan = 6, sticky = W, padx=10, pady=2)

        # sets manage stats button and label

        butManageStatsSchools = Button(self, text = "Manage Statistics/Schools", font=("MS", 8, "bold"),height=2, width = 25)
        ##butManageStatsSchools["command"]=self.Statistics ## look
        butManageStatsSchools.grid(row=3, column=2, columnspan=3, sticky = EW, padx=10, pady=2)

        lblManageStatSchools = Label(self, text = "For Events:  ", font=("MS", 8, "bold"))
        lblManageStatSchools.grid(row = 2, column = 2, columnspan = 2, sticky = W, padx=10, pady=2)
       
        #sets up category choice label
        
        lblCategories = Label(self, text="Select a Category: ", font=('MS', 8, 'bold'))
        lblCategories.grid(row=6, column=2, columnspan=3, sticky=W, padx=10, pady=2)

        #Listboxes are used to display list that can be chosen.  default is browse
        #which allows a single item.  uses scroll.  default is 10 lines.   set it for 3
        #will want to read and clear value so use self before name to make it available
        #later in the program
        
        self.listCategories = Listbox(self,height=5)
        scroll = Scrollbar(self, command= self.listCategories.yview)
        self.listCategories.configure(yscrollcommand=scroll.set)

        #Placed list box next to label and scroll bar after.  Listbox and scrollbar aligned
        #to be next to one another
        self.listCategories.grid(row=7, column=2, columnspan=3, sticky=EW)
        scroll.grid(row=7,column=4,sticky=NS, rowspan=5)

        #inserts required values into listbox inc. empty string at end
        #Need to be added from file input
        for item in ["Cat1", "Cat2", "Cat3", "Cat4", "Cat5", ""]:
            self.listCategories.insert(END,item)

        #create label for add category text box

        lblAddNewCategory = Label(self, text = "Add a New Category:  ", font=("MS", 8, "bold"))
        lblAddNewCategory.grid(row = 4, column = 2, columnspan = 2, sticky = W, padx=10, pady=2)
        
        ##inserts a text box for adding a new category

        self.txtAddNewCategory = Text(self, height = 1, width = 25)
        self.txtAddNewCategory.grid(row =  5, column = 2, columnspan = 3, sticky = EW, padx=10, pady=2)

        ##inserts add button
        butAddCategory = Button(self, text = "Add", font=("MS", 8, "bold"),height=1, width = 10,fg="white", bg="blue")
        ##butAddCategory["command"]=AddQuestions.AddCategory() ## look
        butAddCategory.grid(row=5, column=4, columnspan=1, padx=10, pady=2)

        ##inserts use category and start quiz button
        
        butStartQuiz = Button(self, text = "Use category and start quiz", font=("MS", 8, "bold"),height=2, width = 25,fg="white", bg="blue")
        ##butStartQuiz["command"]=TakeQuiz.StartQuiz() ## look
        butStartQuiz.grid(row=12, column=2, columnspan=3, sticky = EW, padx=10, pady=2)

        #create label for category actions

        lblForSelectedCategory = Label(self, text = "For Selected Category:  ", font=("MS", 8, "bold"),height=2, width = 25)
        lblForSelectedCategory.grid(row = 16, column = 2, columnspan = 3, sticky = EW, padx=10, pady=2)

        
        ##inserts add edit delete buttons
        
        butAddQuestions = Button(self, text = "Add Questions", font=("MS", 8, "bold"),height=2, width = 25)
        ##butAddQuestions["command"]=AddQuestions.AddQuestions() ## look
        butAddQuestions.grid(row=17, column=2, columnspan=3, sticky = EW, padx=10, pady=2)

        butViewEditQuestions = Button(self, text = "View / Edit Questions", font=("MS", 8, "bold"),height=2, width = 25)
        ##butViewEditQuestions["command"]=EditQuestions.EditQuestions() ## look
        butViewEditQuestions.grid(row=18, column=2, columnspan=3, sticky = EW, padx=10, pady=2)

        butDeleteQuestions = Button(self, text = "Delete Questions", font=("MS", 8, "bold"),height=2, width = 25)
        ##butDeleteQuestions["command"]=DeleteQuestions.DeleteQuestions() ## look
        butDeleteQuestions.grid(row=19, column=2, columnspan=3, sticky = EW, padx=10, pady=2)

        butDeleteCategory = Button(self, text = "Delete Category", font=("MS", 8, "bold"),height=2, width = 25)
        ##butDeleteCateory["command"]=DeleteQuestions.DeleteCategory()
        butDeleteCategory.grid(row=20, column=2, columnspan=3, sticky = EW, padx=10, pady=2)
        

       

		
                        

#main
root = Tk()  # call the Tk method
root.title("Admin Options") # set the title
app= AdminOptions(root)    # creates a new instance of the AdminOptions class
root.mainloop()  # starts window with mainloop method
