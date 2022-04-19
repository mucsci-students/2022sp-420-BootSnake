# Ben M, Travis Z, Andy P
# GUI implementation of Software engineering program
# sprint 2
# last edited: 3/2/22


# https://www.youtube.com/watch?v=H3Cjtm6NuaQ

# =================================================================================================================================================================================================================================================================================

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk

from classModel import *
from relationshipsModel import *
from saveLoadModel import *
from attributesModel import *
from interfaceView import *
from parametersModel import *
from sharedItems import *


# =================================================================================================================================================================================================================================================================================



# initialize window
window = tk.Tk()
window.title("bootsnake")
window.geometry("400x200")


# =================================================================================================================================================================================================================================================================================


# list for entries in entry boxes
entries = []



# =================================================================================================================================================================================================================================================================================


# variables to keep track of drop down menu, and lists for drop down options
classVar = StringVar(window)
classOptions = [
    '',
    'Add',
    'Delete',
    'Rename',
]
relationshipVar = StringVar(window)
relationshipOptions = [
    '',
    'Add',
    'Delete',
    'Edit',
]
methodsVar = StringVar(window)
methodsOptions = [
    '',
    'Add',
    'Delete',
    'Rename',
]
fieldsVar = StringVar(window)
fieldsOptions = [
    '',
    'Add',
    'Delete',
    'Rename',
]
parameterVar = StringVar(window)
parameterOptions = [
    '',
    'Add',
    'Change',
]


# =================================================================================================================================================================================================================================================================================


# calls for each file's methods
def classCalls(*args):
    err = False
    if classVar.get() == 'Add':
        windowEntry(1, "Class Add")
        err = ClassAdd(entries[0])
    elif classVar.get() == 'Delete':
        windowEntry(1, "Class Delete")
        err = ClassDelete(entries[0])
    elif classVar.get() == 'Rename':
        windowEntry(2, "Class Rename")
        err = ClassRename(entries[0], entries[1])
    if err is not False:
        throwMessage(err)
    classVar.set("")

def relationshipCalls(*args):
    err = False
    if relationshipVar.get() == 'Add':
        windowEntry(3, "Relationship Add")
        if entries[2] == "Aggregation" or entries[2] == "Composition" or entries[2] == "Inheritance" or entries[2] == "Realization":
            err = RelationshipAdd(entries[0], entries[1], entries[2])
        else:
            throwMessage("Incorrect relationship type. The available options are: Aggregation, Composition, Inheritance, Realization")
            return
    elif relationshipVar.get() == 'Delete':
        windowEntry(2, "Relationship Delete")
        err = RelationshipDelete(entries[0], entries[1])
    elif relationshipVar.get() == 'Edit':
        windowEntry(3, "Relationship Edit")
        print(entries[2])
        if entries[2] == "Aggregation" or entries[2] == "Composition" or entries[2] == "Inheritance" or entries[2] == "Realization":
            err = relationshipEdit(entries[0], entries[1], entries[2])
        else:
            throwMessage("Incorrect relationship type. The available options are: Aggregation, Composition, Inheritance, Realization")
            return
    if err is not False:
        throwMessage(err)
    relationshipVar.set("")

def methodCalls(*args):
    err = False
    if methodsVar.get() == 'Add':
        windowEntry(2, "Method Add")
        err = addMethod(entries[0], entries[1], [])
    elif methodsVar.get() == 'Delete':
        windowEntry(3, "Method Delete")
        err = delMethod(entries[0], entries[1])
    elif methodsVar.get() == 'Rename':
        windowEntry(2, "Method Rename")
        err = renMethod(entries[0], entries[1], entries[2])
    if err is not False:
        throwMessage(err)
    methodsVar.set("")



def fieldCalls(*args):
    err = False
    if fieldsVar.get() == 'Add':
        windowEntry(2, "Field Add")
        err = addField(entries[0], entries[1])
    elif fieldsVar.get() == 'Delete':
        windowEntry(2, "Field Delete")
        err = delField(entries[0], entries[1])
    elif fieldsVar.get() == 'Rename':
        windowEntry(3, "Field Rename")
        err = renField(entries[0], entries[1], entries[2])
    if err is not False:
        throwMessage(err)
    fieldsVar.set("")



def parameterCalls(*args):
    err = False
    if parameterVar.get() == 'Add':
        windowEntry(4, "Parameter Add")
        err = ParamAdd(entries[0], entries[1], entries[2], entries[3])
    elif parameterVar.get() == 'Change':
        windowEntry(3, "Parameter Change")
        err = changeParam(entries[0], entries[1], entries[2])
    if err is not False:
        throwMessage(err)
    parameterVar.set("")


def saveCall():
    err = False
    filename = filedialog.asksaveasfilename()
    if filename != "":
        err= save(filename)
    if err is not False:
        throwMessage(err)

def loadCall():
    err = False
    #filename = filedialog.askopenfilename()
    filename = filedialog.askopenfilename(filetypes=(("Json File", "*.json"),), title="Choose JSON file")
    if filename != "":
        err = load(filename)
    if err is not False:
        throwMessage(err)


def listClassCall():
    windowEntry(1, "List Class")
    message = ListClass(entries[0])
    throwMessage(message)



def listClassesCall():
    message = ListClasses()
    throwMessage(message)



def listRelationshipsCall():
    message = ListRelationships()
    throwMessage(message)


# =================================================================================================================================================================================================================================================================================

# for making an arbitrary number of entry boxes for functions
# makes a new window and adds entry boxes. 
# updates entries list with those entry box objects to be accessed by other functions
def windowEntry(numEntries: int, title: str):

    # create new pop up window
    newWindow = Toplevel(window)
    newWindow.title(title)
    newWindow.geometry("400x200")

    # create start button and entry boxes based on input
    startVar = tk.IntVar()
    startButton = Button(newWindow, text='Go!', command=lambda: startVar.set(1))
    startButton.grid(row=1, column=0, pady=20)
    
    entryObjList = []
    for x in range(numEntries):
        entry = Entry(newWindow)
        entry.grid(row=0, column=x, pady=20, padx=5)
        entryObjList.append(entry)
    
    # waits for button to be pressed before returning to function
    startButton.wait_variable(startVar)

    # once button has been pressed, add string entries to list for usage. this means we can now close the window
    entries.clear()
    for e in entryObjList:
        entries.append(e.get())

    # close window automatically, we cant close until we are done with the entries, so we may not be able to do this with this current implementation
    newWindow.destroy()




# make a new message with given string
def throwMessage(mes: str):
    messagebox.showinfo("Message", mes)


# =================================================================================================================================================================================================================================================================================


# drop down menu and label objects
classLabel = tk.Label(window, text="Class").grid(row=0, column=0)
classDrop = tk.OptionMenu(window, classVar, *classOptions).grid(row=1, column=0)
#classDrop = ttk.Combobox(window, classOptions).grid(row=1, column=0)

relationshipLabel = tk.Label(window, text="Relationship").grid(row=0, column=1)
relationshipDrop = tk.OptionMenu(window, relationshipVar, *relationshipOptions).grid(row=1, column=1)

fieldsLabel = tk.Label(window, text="Fields").grid(row=0, column=2)
fieldsDrop = tk.OptionMenu(window, fieldsVar, *fieldsOptions).grid(row=1, column=2)

methodsLabel = tk.Label(window, text="Methods").grid(row=0, column=3)
methodsDrop = tk.OptionMenu(window, methodsVar, *methodsOptions).grid(row=1, column=3)

parameterLabel = tk.Label(window, text="Paramters").grid(row=0, column=4)
parameterDrop = tk.OptionMenu(window, parameterVar, *parameterOptions).grid(row=1, column=4)

listClassButton = tk.Button(window, text="List Class", command=listClassCall).grid(row=2, column=0)
listClassesButton = tk.Button(window, text="List Classes", command=listClassesCall).grid(row=2, column=1)
listRelationshipsButton = tk.Button(window, text="List Relationships", command=listRelationshipsCall).grid(row=2, column=2)

saveButton = tk.Button(window, text="Save", command=saveCall).grid(row=3, column=0)
loadButton = tk.Button(window, text="Load", command=loadCall).grid(row=3, column=1)



# =================================================================================================================================================================================================================================================================================



# keeping track of whether a drop down menu option was selected
classVar.trace("w", classCalls)
relationshipVar.trace("w", relationshipCalls)
methodsVar.trace("w", methodCalls)
fieldsVar.trace("w", fieldCalls)
parameterVar.trace("w", parameterCalls)




# =================================================================================================================================================================================================================================================================================

# end
window.mainloop()