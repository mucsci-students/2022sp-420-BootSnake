# Ben M, Travis Z, Andy P
# GUI implementation of Software engineering program
# sprint 2
# last edited: 2/23/22


from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("bootsnake")
window.geometry("250x200")





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



def test(*args):
    if classVar.get() == 'Add':
        messagebox.showinfo(
            "info name", "class add"
        )


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




classVar.trace("w", test)

# end
window.mainloop()