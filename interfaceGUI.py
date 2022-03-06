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
from relationships import *
from saveLoad import *
from attributes import *
from interface import *
from parameters import *


# =================================================================================================================================================================================================================================================================================



# initialize window
window = tk.Tk()
window.title("bootsnake")
window.geometry("700x300")


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
    'Delete',
]


# =================================================================================================================================================================================================================================================================================


# calls for each file's methods
def classCalls(*args):
    err = False
    if classVar.get() == 'Add':
        windowEntry(1, "Class Add", ["Class Name"])
        err = ClassAdd(entries[0])
    elif classVar.get() == 'Delete':
        windowEntry(1, "Class Delete", ["Class Name"])
        err = ClassDelete(entries[0])
    elif classVar.get() == 'Rename':
        windowEntry(2, "Class Rename", ["Class Name", "New Class Name"])
        err = ClassRename(entries[0], entries[1])
    if err is not False:
        throwMessage(err)
    classVar.set("")

def relationshipCalls(*args):
    err = False
    if relationshipVar.get() == 'Add':
        windowEntry(3, "Relationship Add", ["Source Class", "Dest Class", "Type"])
        if entries[2] == "Aggregation" or entries[2] == "Composition" or entries[2] == "Inheritance" or entries[2] == "Realization":
            err = RelationshipAdd(entries[0], entries[1], entries[2])
        else:
            throwMessage("Incorrect relationship type. The available options are: \nAggregation \nComposition \nInheritance \nRealization")
            return
    elif relationshipVar.get() == 'Delete':
        windowEntry(2, "Relationship Delete", ["Source Class", "Dest Class", "Type"])
        err = RelationshipDelete(entries[0], entries[1])
    elif relationshipVar.get() == 'Edit':
        windowEntry(3, "Relationship Edit", ["Source Class", "Dest Class", "New Type"])
        print(entries[2])
        if entries[2] == "Aggregation" or entries[2] == "Composition" or entries[2] == "Inheritance" or entries[2] == "Realization":
            err = relationshipEdit(entries[0], entries[1], entries[2])
        else:
            throwMessage("Incorrect relationship type. The available options are: \nAggregation \nComposition \nInheritance \nRealization")
            return
    if err is not False:
        throwMessage(err)
    relationshipVar.set("")

def methodCalls(*args):
    err = False
    if methodsVar.get() == 'Add':
        windowEntry(3, "Method Add", ["Class Name", 'Method Name', 'Return Type'])
        err = addMethod(entries[0], entries[1], entries[2], [])
    elif methodsVar.get() == 'Delete':
        windowEntry(3, "Method Delete", ["Class Name", 'Method Name'])
        err = delMethod(entries[0], entries[1])
    elif methodsVar.get() == 'Rename':
        windowEntry(3, "Method Rename", ["Class Name", 'Method Name', 'New Method Name'])
        err = renMethod(entries[0], entries[1], entries[2])
    if err is not False:
        throwMessage(err)
    methodsVar.set("")



def fieldCalls(*args):
    err = False
    if fieldsVar.get() == 'Add':
        windowEntry(3, "Field Add", ["Class Name", 'Field Name', 'Field Type'])
        err = addField(entries[0], entries[1], entries[2])
    elif fieldsVar.get() == 'Delete':
        windowEntry(2, "Field Delete", ["Class Name", 'Field Name'])
        err = delField(entries[0], entries[1])
    elif fieldsVar.get() == 'Rename':
        windowEntry(3, "Field Rename", ["Class Name", 'Field Name', "New Field Name"])
        err = renField(entries[0], entries[1], entries[2])
    if err is not False:
        throwMessage(err)
    fieldsVar.set("")



def parameterCalls(*args):
    err = False
    if parameterVar.get() == 'Add':
        windowEntry(4, "Parameter Add", ["Class Name", "Method Name", "Parameter Name", "Parameter Type"])
        err = ParamAdd(entries[0], entries[1], entries[2], entries[3])
    elif parameterVar.get() == "Delete":
        windowEntry(3, "Parameter Delete", ["Class Name", "Method Name", "Parameter Name"])
        err = delParam(entries[0], entries[1], entries[2])
    elif parameterVar.get() == "Rename":
        windowEntry(4, "Parameter Rename", ["Class Name", "Method Name", "Parameter Name", "New Param Name"])
        err = delParam(entries[0], entries[1], entries[2], entries[3])
    if err is not False:
        throwMessage(err)
    parameterVar.set("")


# =================================================================================================================================================================================================================================================================================


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



# =================================================================================================================================================================================================================================================================================


def listClassCall():
    windowEntry(1, "List Class", ["Class Name"])
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
# Params:
# number of entry boxes
# title of window
# list of labels for each entry box
def windowEntry(numEntries: int, title: str, labels : list):

    # create new pop up window
    newWindow = Toplevel(window)
    newWindow.title(title)
    newWindow.geometry("550x200")

    # create start button and entry boxes based on input
    startVar = tk.IntVar()
    startButton = Button(newWindow, text='Go!', command=lambda: startVar.set(1))
    startButton.grid(row=2, column=0, pady=20)
    
    entryObjList = []
    for x in range(numEntries):
        label = Label(newWindow, text=labels[x]).grid(row=0, column=x, pady=20, padx=5)
        entry = Entry(newWindow)
        entry.grid(row=1, column=x, pady=20, padx=5)
        entryObjList.append(entry)
    
    # waits for button to be pressed before returning to function
    startButton.wait_variable(startVar)

    # once button has been pressed, add string entries to list for usage. this means we can now close the window
    entries.clear()
    for e in entryObjList:
        entries.append(e.get())

    # close window automatically, we cant close until we are done with the entries, so we may not be able to do this with this current implementation
    newWindow.destroy()



messageBox = tk.Text(window, height=15, width=35, wrap='word')
messageBox.insert('end', "Messages will appear here.")
# make a new message with given string
def throwMessage(mes: str):
    if mes is not None:
        messageBox.delete(1.0, 'end')
        messageBox.insert('end', mes)


# =================================================================================================================================================================================================================================================================================


# drop down menu and label objects
classLabel = tk.Label(window, text="Class").place(x=0, y=0)
classDrop = tk.OptionMenu(window, classVar, *classOptions).place(x=0, y=30)
#classDrop = ttk.Combobox(window, classOptions).grid(row=1, column=0)

relationshipLabel = tk.Label(window, text="Relationship").place(x=50, y=0)
relationshipDrop = tk.OptionMenu(window, relationshipVar, *relationshipOptions).place(x=60, y=30)

fieldsLabel = tk.Label(window, text="Fields").place(x=140, y=0)
fieldsDrop = tk.OptionMenu(window, fieldsVar, *fieldsOptions).place(x=140, y=30)

methodsLabel = tk.Label(window, text="Methods").place(x=200, y=0)
methodsDrop = tk.OptionMenu(window, methodsVar, *methodsOptions).place(x=200, y=30)

parameterLabel = tk.Label(window, text="Parameters").place(x=275, y=0)
parameterDrop = tk.OptionMenu(window, parameterVar, *parameterOptions).place(x=275, y=30)

listClassButton = tk.Button(window, text="List Class", command=listClassCall).place(x=0, y=70)
listClassesButton = tk.Button(window, text="List Classes", command=listClassesCall).place(x=75, y=70)
listRelationshipsButton = tk.Button(window, text="List Relationships", command=listRelationshipsCall).place(x=165, y=70)

saveButton = tk.Button(window, text="Save", command=saveCall).place(x=0, y=110)
loadButton = tk.Button(window, text="Load", command=loadCall).place(x=50, y=110)

quitButton = tk.Button(window, text="Quit", command=exit).place(x=0, y=150)

messageBox.place(x=400, y=40)


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