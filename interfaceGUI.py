# Ben M, Travis Z, Andy P
# GUI implementation of Software engineering program
# sprint 2
# last edited: 3/1/22


# https://www.youtube.com/watch?v=H3Cjtm6NuaQ


from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk

from classModelController import *
from relationships import *
from saveLoad import *
from UML_attributes import *

# initialize window
window = tk.Tk()
window.title("bootsnake")
window.geometry("400x200")

# list for entries in entry boxes
entries = []


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
]
fieldsVar = StringVar(window)
fieldsOptions = [
    '',
    'Add',
    'Delete',
    'Rename',
]
methodsVar = StringVar(window)
methodsOptions = [
    '',
    'Add',
    'Delete',
    'Rename',
]


# calls for each file's methods
def classCalls(*args):
    if classVar.get() == 'Add':
        windowEntry(1)
        entry_list = ""
        for entry in entries:
            entry_list = entry_list + str(entry.get() + '\n')
        #ClassAdd(entries[0].get())
        return
    elif classVar.get() == 'Delete':
        windowEntry(1)
        return
        #ClassDelete()
    elif classVar.get() == 'Rename':
        windowEntry(2)
        return
        #ClassRename()


def relationshipCalls(*args):
    if relationshipVar.get() == 'Add':
        RelationshipAdd()
    elif relationshipVar.get() == 'Delete':
        RelationshipDelete()


def methodCalls(*args):
    if methodsVar.get() == 'Add':
        return
    elif methodsVar.get() == 'Delete':
        return
    elif methodsVar.get() == 'Rename':
        return


def fieldCalls(*args):
    if fieldsVar.get() == 'Add':
        return
    elif fieldsVar.get() == 'Delete':
        return
    elif fieldsVar.get() == 'Rename':
        return


def saveCall():
    filename = filedialog.asksaveasfilename()
    save(filename)

def loadCall():
    filename = filedialog.askopenfilename()
    #filename = filedialog.askopenfilename(filetypes=(("Json files", "*.json*")))
    load(filename)





# for making an arbitrary number of entry boxes for functions
def windowEntry(numEntries: int):
    newWindow = Toplevel(window)
    newWindow.title("Entry")
    newWindow.geometry("400x200")

    startButton = Button(newWindow, text='Go!', command=newWindow.destroy)
    startButton.grid(row=1, column=0, pady=20)
    for x in range(numEntries):
        entry = Entry(newWindow)
        entry.grid(row=0, column=x, pady=20, padx=5)
        entries.append(entry)


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
# startButton = tk.Button(window, text="Start", command=test).grid(row=1, column=2)

saveButton = tk.Button(window, text="Save", command=saveCall).grid(row=1, column=4)
loadButton = tk.Button(window, text="Load", command=loadCall).grid(row=1, column=5)



# keeping track of whether a drop down menu option was selected
classVar.trace("w", classCalls)
relationshipVar.trace("w", relationshipCalls)
methodsVar.trace("w", relationshipCalls)
fieldsVar.trace("w", methodCalls)



# end
window.mainloop()