# SoftwareEngineeringQuiz

The start page is the main file to run "python startPage.py" and make sure all the pther files are in the current working directory

Current login is U: "JS" , P: "P" , new login system needs to be created

Window structure:

startPage.py and adminOptions.py will be the top level windows and have no masters

Login window belongs to startPage and the various options in there will be children of admin options

to Start the quiz with the current options we'll need to pass the category selected to startPage.py, could pass it empty string at startup and then if it's empty have the start button unclickable.

So then when its selected in admin options a string is passed and that chooses the categories

also add question and view edit question need to receive the same string




