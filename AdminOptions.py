from tkinter import *
from lib.loginDetails import loginDetails
import startPage
import shelve
from Category import Category
import os
import tkinter.messagebox as tkm

class AdminOptions(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.createAdminOptions()
        self.getAvailableCategories()
        self.addNewCat()
        self.finalButts()
        self.addQuestionsBtn()
        self.addQsToCat()
        self.viewEditQuestionsBtn()
        self.master.bind("<Return>",self.addCategories)
        self.txtAddNewCategory.focus_set()
        
    def createAdminOptions(self):

        ## create logout button
        
        butLogout = Button(self, text = "Logout", font=("MS", 8, "bold"), height=1, width = 10)
        butLogout["command"]=self.logout  ## look
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
        
        

        #inserts required values into listbox inc. empty string at end
        #Need to be added from file input
    def getAvailableCategories(self):
        self.listCategories = Listbox(self,height=5,exportselection=0)
        scroll = Scrollbar(self, command= self.listCategories.yview)
        self.listCategories.configure(yscrollcommand=scroll.set)

        #Placed list box next to label and scroll bar after.  Listbox and scrollbar aligned
        #to be next to one another
        self.listCategories.grid(row=7, column=2, columnspan=3, sticky=EW)
        scroll.grid(row=7,column=5,sticky=NS+W, rowspan=5)

        self.catList = Category.getList()
        print(self.catList)
        for item in self.catList:
            self.listCategories.insert(END,item)

        self.listCategories.selection_set(END)
        self.listCategories.bind('<<ListboxSelect>>', self.setButtonState)

        #create label for add category text box
    def addNewCat(self):

        lblAddNewCategory = Label(self, text = "Add a New Category:  ", font=("MS", 8, "bold"))
        lblAddNewCategory.grid(row = 4, column = 2, columnspan = 2, sticky = W, padx=10, pady=2)
        
        ##inserts a text box for adding a new category

        self.txtAddNewCategory = Entry(self, width = 25)
        self.txtAddNewCategory.grid(row =  5, column = 2, columnspan = 3, sticky = EW, padx=10, pady=2)

        ##inserts add button
        butAddCategory = Button(self, text = "Add", font=("MS", 8, "bold"),height=1, width = 10,fg="white", bg="blue")
        butAddCategory["command"]=self.addCategories
        print(self.txtAddNewCategory.get()) ## look
        butAddCategory.grid(row=5, column=4, columnspan=1, padx=10, pady=2)

        ##inserts use category and start quiz button

    def addCategories(self,e):
        newCat = self.txtAddNewCategory.get()
        if newCat != '':

            Category.addCategory(newCat)
            self.txtAddNewCategory.delete(0,'end')
            self.getAvailableCategories()
        else:
            tkm.showerror('Error','Enter a category name first')

    def addQuestionsBtn(self):
        butAddQuestions = Button(self, text = "Create Questions", font=("MS", 8, "bold"),height=2, width = 25)
        butAddQuestions["command"]= self.launchAddQuests ## look
        butAddQuestions.grid(row=17, column=2, columnspan=3, sticky = EW, padx=10, pady=2)

    def launchAddQuests(self):
        #get the current value of categories and pass it to addQuestions
        # currentSelection = self.listCategories.curselection()
        # selectedCategory = self.listCategories.get(currentSelection)
        # self.listCategories.selection_clear(currentSelection)
        createQuest = Toplevel(self.master)
        createQuest.grab_set()
        createQuest.title('Add Questions')
        import addQuestion
        addQuestion.addQuestion(createQuest)

    def viewEditQuestionsBtn(self):
        butViewEditQuestions = Button(self, text = "View / Edit Questions", font=("MS", 8, "bold"),height=2, width = 25)
        butViewEditQuestions["command"]=self.launchViewEditQs ## look
        butViewEditQuestions.grid(row=18, column=2, columnspan=3, sticky = EW, padx=10, pady=2)

    
    def launchViewEditQs(self):
        vEdit = Toplevel(self.master)
        vEdit.grab_set()
        vEdit.title('Add Questions')
        import ViewEditQuestionsEntry
        ViewEditQuestionsEntry.ViewEditQuestions(vEdit)



    def finalButts(self):
        self.btnStartQuiz = Button(self, text = "Use category and start quiz \n (10 question min.)", font=("MS", 8, "bold"),height = 4, width = 25,fg="white", bg="blue")
        self.btnStartQuiz["command"]=self.launchQuiz ## look
        self.btnStartQuiz["state"] = "disabled"
        self.btnStartQuiz.grid(row=12, column=2, columnspan=3, rowspan =2, sticky = EW, padx=10, pady=2)

        #create label for category actions

        butDeleteQuestions = Button(self, text = "Delete Questions", font=("MS", 8, "bold"),height=2, width = 25)
        ##butDeleteQuestions["command"]=DeleteQuestions.DeleteQuestions() ## look
        butDeleteQuestions.grid(row=19, column=2, columnspan=3, sticky = EW, padx=10, pady=2)





    def launchQuiz(self):
        selectedCat = self.listCategories.get(self.listCategories.curselection()[0])
        import startPage
        self.master.destroy()
        startPage.main(selectedCat)


    def setButtonState(self,e):
        selectedCat = self.listCategories.get(self.listCategories.curselection()[0])
        print(selectedCat)
        numOfQs = Category.questionCount(selectedCat)
        if (numOfQs < 10 and (self.btnStartQuiz["state"] == "normal")):
            self.btnStartQuiz["state"] = "disabled"
            print('disabled')
        elif (numOfQs == 10 and (self.btnStartQuiz["state"] == "disabled")):
            self.btnStartQuiz["state"] = "normal"
            print('normal')
            print(numOfQs)
            print(self.btnStartQuiz["state"])
        print(numOfQs)

    def launchAddQsToCat(self):
        currentSelection = self.listCategories.curselection()
        selectedCategory = self.listCategories.get(currentSelection)
        self.listCategories.selection_clear(currentSelection)
        addQ = Toplevel(self.master)
        addQ.grab_set()
        addQ.title('Add Questions to Category')
        import addQuestToCat
        addQuestToCat.addQuestToCat(addQ, selectedCategory)
     
    def addQsToCat(self):
        lblForSelectedCategory = Label(self, text = "For Selected Category:  ", font=("MS", 8, "bold"),height=2, width = 25)
        lblForSelectedCategory.grid(row = 20, column = 2, columnspan = 3, sticky = EW, padx=10, pady=2)

        butAddQsToCat  = Button(self, text = "View Questions in Category", font=("MS", 8, "bold"),height=2, width = 21)
        butAddQsToCat["command"] = self.launchAddQsToCat
        butAddQsToCat.grid(row = 21, column = 2, columnspan =3, padx = 10, pady =2, sticky = EW)

        btnDeleteCategory = Button(self, text = "Delete Category", font=("MS", 8, "bold"),height=2, width = 25)
        btnDeleteCategory["command"]=self.deleteCategory
        btnDeleteCategory.grid(row=22, column=2, columnspan=3, sticky = EW, padx=10, pady=2)

    def deleteCategory(self):
        # here delete category from list,
        # also open up questiondb and delete every question with category
        currentSelection = self.listCategories.curselection()
        selectedCategory = self.listCategories.get(currentSelection)
        self.listCategories.selection_clear(currentSelection)
        Category.deleteCategory(selectedCategory)
        self.getAvailableCategories()

    def logout(self):
        self.master.destroy()
        startPage.main()
       
def main():
    root = Tk()  # call the Tk method
    root.title("Admin Options") # set the title
    app= AdminOptions(root)
    app['bg'] = 'gray80'    # creates a new instance of the AdminOptions class
    root.mainloop()  # starts window with mainloop method

if __name__ == "__main__":
    main()