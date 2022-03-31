# Project Name  : UML_BootSnake
# File Name     : gui.py
# Course        : CSCI 420
# Professor     : Dr. Stephanie Schwartz
# BootSnake Team: Amelia S., Andy P., Ben M., Tram T., Travis Z.


###############################################################################

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import ttk

from classModel import *
from relationshipsModel import *
from saveLoadModel import *
from attributesModel import *
from interfaceView import *
from parametersModel import *
import canvas as c




###################################################################################################
'''
Main function to create the GUI.
'''


def saveCall():
    err = False
    filename = filedialog.asksaveasfilename()
    if filename != "":
        err= save(filename)
    #if err is not False:
        #throwMessage(err)

def loadCall():
        err = False
        #filename = filedialog.askopenfilename()
        filename = filedialog.askopenfilename(filetypes=(("Json File", "*.json"),), title="Choose JSON file")
        if filename != "":
            err = load(filename)
        #if err is not False:
            #throwMessage(err)


def clearAll():
    c.my_canvas.delete("all")
    c.boxlist = []




def openAbout():
    message = f"BootSnake 2022 v.2"
    messagebox.showinfo("BootSnake About...", message)

        

# =============================================================================

def gui_run():

# initialize window    
    window = tk.Tk()
    window.title("BootSnake")
    window.geometry("700x300")
    
    # maximize the window
    #window.state('zoomed')
    
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1,weight=1)
    window.grid_columnconfigure(1,weight=1)
    
    #menubar = build_menu(window)

    menubar = tk.Menu(window)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=clearAll)
    filemenu.add_command(label="Open", command=loadCall)
    filemenu.add_command(label="Save", command=saveCall)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    menu_edit = tk.Menu(menubar, tearoff=0)
    menu_edit.add_command(label = "Undo")
    menu_edit.add_command(label = "Redo")
    menubar.add_cascade(label = "Edit", menu = menu_edit)
    
    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index")
    helpmenu.add_command(label="About...", command=openAbout)
    menubar.add_cascade(label="Help", menu=helpmenu)

    window.config(menu=menubar)
    
   
    """ 
        
        The Frame widget acts as a container, grouping and organizing other 
        widgets to provide a nice-looking layout and appearance of the GUI.
        A frame can also be used as a foundation class to implement complex
        widgets.

    """
    # Widget Construction    
    mainFrame = tk.Frame(window, bd=5, relief=tk.FLAT)
    mainFrame.pack(expand=1, fill=BOTH)
    sideFrame = tk.Frame(window)
    
    # create a canvas here by calling the method makeCanvas()
    canvasPanel = c.makeCanvas(mainFrame)
    
    

    # add horizontal & vertical scrollbar to the canvas panel
    # https://riptutorial.com/tkinter/example/27784/scrolling-a-canvas-widget-horizontally-and-vertically
    # https://www.youtube.com/watch?v=0WafQCaok6g
    
    
    hbar = tk.Scrollbar(mainFrame, orient = tk.HORIZONTAL, command=c.my_canvas.xview)
    hbar.pack(fill = tk.X, side = tk.BOTTOM)

    vbar = tk.Scrollbar(mainFrame, orient = tk.VERTICAL, command=c.my_canvas.yview)
    vbar.pack(fill = tk.Y, side = tk.LEFT)
    

    # configure the canvas
    c.my_canvas.pack(side=LEFT,expand=True,fill=BOTH) # move this will change the position of the scrollbars
    c.my_canvas.configure(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    c.my_canvas.bind('<Configure>', lambda e: c.my_canvas.configure(scrollregion=c.my_canvas.bbox("all")))
   



    # make control-tabs for classAdd, relAdd, method, fields, and param
    sidePanel = ttk.Notebook(sideFrame)
    classTab = tk.Frame(master = sidePanel, borderwidth = 3)
    sidePanel.add(classTab, text = "Class")
    sidePanel.insert(0, classTab)

    

    relTab = tk.Frame(master = sidePanel, borderwidth = 3)
    sidePanel.add(relTab, text = "Relation")
    sidePanel.insert(1, relTab)

    listClassTab = tk.Frame(master = sidePanel, borderwidth = 3)
    sidePanel.add(listClassTab, text = "Class/Relation List")
    sidePanel.insert(2, listClassTab)


    classPanel = ttk.Notebook(master = classTab)
    classPanel.grid(row = 3, column = 0, sticky = "w", columnspan = 10)
    methodTab = tk.Frame(classPanel, borderwidth = 3)
    classPanel.add(methodTab, text = "Methods")
    classPanel.insert(0, methodTab)

    
    paramTab = tk.Frame(classPanel, borderwidth = 3)
    classPanel.add(paramTab, text = "Parameters")
    classPanel.insert(1, paramTab)

    fieldTab = tk.Frame(classPanel, borderwidth = 3)
    classPanel.add(fieldTab, text = "Fields")
    classPanel.insert(2, fieldTab)

    sidePanel.pack(expand=1, fill=BOTH)
    
    
    
    # Widget Placement
    mainFrame.grid(row = 0, column = 1, sticky = "nsew", rowspan = 2)
    mainFrame.columnconfigure(1, weight = 1)
    mainFrame.rowconfigure(1, weight = 1)
    
    sideFrame.grid(row = 0, column = 2, sticky = "nse", rowspan = 2)
    sideFrame.columnconfigure(2, weight = 1)
    sideFrame.rowconfigure(0, weight = 1)
    
    
    
    # sidepanel that holds tabs
    sidePanel.grid(row = 0, column = 2, sticky = "nse", rowspan=2)

    # ========================================================================#

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
        'Rename',
    ]

    # ========================================================================#

    # list for entries in entry boxes
    entries = []

    # =========================================================================#


    # calls for UML class to create windows for classAdd/classDelete/classRename
    def classCalls(*args):
        err = False
        if classVar.get() == 'Add':
            windowEntry(1, "Class Add", ["Class Name"])
               
       
        elif classVar.get() == 'Delete':
            windowEntry(1, "Class Delete", ["Class Name"])
         
        
        elif classVar.get() == 'Rename':
            delAttrWinEnt(2, "Class Rename", ["Class Name", "New Class Name"])
         
        
        if err is not False:
            throwMessage(err)
            classVar.set("")

    # calls for UML Relation to create windows for RelationshipsAdd/RelationshipDelete/RelationshipsEdit
    def relationshipCalls(*args):
        err = False
        if relationshipVar.get() == 'Add':
            relWinEntCombo(2,1, "Relationship Add", ["Source Class", "Dest Class"])
           
        elif relationshipVar.get() == 'Delete':
            delAttrWinEnt(2, "Relationship Delete", ["Source Class", "Dest Class"])
            
        
        elif relationshipVar.get() == 'Edit':
            relWinEntCombo(2,1, "Relationship Edit", ["Source Class", "Dest Class"])


    # calls for UML Class' Method to create windows for MethodAdd/MethodDelete/MethodEdit        
    def methodCalls(*args):
        err = False
        if methodsVar.get() == 'Add':
            entries.clear()
            attrWinEnt(3, "Method Add", ["Class Name", 'Method Name', 'Type'])
           
        elif methodsVar.get() == 'Delete':
            entries.clear()
            delAttrWinEnt(2, "Method Delete", ["Class Name", 'Method Name'])
    
        elif methodsVar.get() == 'Rename':
            entries.clear()
            attrWinEnt(3, "Method Rename", ["Class Name", 'Method Name', 'New Method Name'])
            
            if err is not False:
                throwMessage(err)
                methodsVar.set("")


    # calls for UML Methods' Fields to create windows for FieldAdd/FieldDelete/FieldRename
    def fieldCalls(*args):
        err = False
        if fieldsVar.get() == 'Add':
            entries.clear()
            attrWinEnt(3, "Field Add", ["Class Name", 'Field Name', 'Field Type'])
            
            
        elif fieldsVar.get() == 'Delete':
            entries.clear()
            delAttrWinEnt(2, "Field Delete", ["Class Name", 'Field Name'])
            
        
        elif fieldsVar.get() == 'Rename':
            entries.clear()
            attrWinEnt(3, "Field Rename", ["Class Name", 'Field Name', "New Field Name"])
           
            if err is not False:
                throwMessage(err)
                fieldsVar.set("")
        


    # calls for UML Methods' param to create windows for ParamAdd/ParamDelete
    def parameterCalls(*args):
        err = False
        if parameterVar.get() == 'Add':
            entries.clear()
            paramWinEnt(4, "Parameter Add", ["Class Name", "Method Name", "Parameter Name", "Parameter Type"])
            
        
        elif parameterVar.get() == "Delete":
            entries.clear()
            attrWinEnt(3, "Parameter Delete", ["Class Name", "Method Name", "Parameter Name"])
            
        
        elif parameterVar.get() == "Rename":
            entries.clear()
            paramWinEnt(4, "Parameter Rename", ["Class Name", "Method Name", "Parameter Name", "New Param Name"])
            
            if err is not False:
                throwMessage(err)
                parameterVar.set("")


# =============================================================================#

    # calls for UML listClass to create windows for listClasses/listRelationships
    def listClassCall():
        windowEntry(1, "List Class", ["Class Name"])
        
        #message = ListClass(entries[0])
        #throwMessage(message)
        #popup(message)

    def listClassesCall():
        message = ListClasses()
        #throwMessage(message)
        messagebox.showinfo("List Classes", message)

    def listRelationshipsCall():
        message = ListRelationships()
        #throwMessage(message)
        messagebox.showinfo("List Relationships", message)


# =====================================================================================
    # Generates new windows and entry boxes for class, rel, fields, methods, and params
    # makes an arbitrary number of entry boxes for functions
    # makes a new window and adds entry boxes. 
    # updates entries list with those entry box objects to be accessed by other functions
    #   Params:
    #   number of entry boxes
    #   title of window
    #   list of labels for each entry box
    

    # create Class window function
    def windowEntry(numEntries: int, title: str, labels : list):

        # create new pop up window
        root = Toplevel(window)
        root.title(title)
        root.geometry("550x200")
        
        entryObjList = []
        # labels start at row 6, entry boxes/combo at row 7
        
        for x in range(numEntries):
            label = Label(root, text=labels[x]).grid(row=6, column=x, pady=20, padx=5)
            entry = Entry(root)
            entry.grid(row=7, column=x, pady=20, padx=5)
            entryObjList.append(entry)
            
        # set focus to the 1st entry box
        entryObjList[0].focus()
            
       
        # Line Separator to display the message at the top section of the popup.
        lineseparator = ttk.Separator(root, orient = "horizontal")
        lineseparator.grid(row = 4, column = 0, sticky = "ew", columnspan=10)
        #lineseparator.pack(fill= 'x')

        # Label for outputing message.
        msgLabel = tk.Label(root, text = "")
        msgLabel.grid(row = 3, column = 0)

        # button to confirm 
        okButton = tk.Button(master =root, text="Go!", command=lambda:classCommand( 
                            entryObjList[0].get(), msgLabel))
        okButton.grid(row = 9, column = 0, padx = 20, pady = 20)


        # Bind the enter key to the user's pressing button. This acts the same as the
        # user presses the button.
        root.bind('<Return>', lambda event:classCommand(entryObjList[0].get(),msgLabel))            

        entries.clear()

    """ 
    The classCommand function binds the button pressing to the 
    classAdd & ClassDelete functions.
    """
    def classCommand(entry, label: tk.Label):

        if classVar.get() == 'Add':
            res = ClassAdd(entry) 
            label.configure(text=res) 
            entries.clear()
            msg = c.addBoxInfo(entry)
            label.configure(text=msg)
            

        if classVar.get() == 'Delete':
            res = ClassDelete(entry) 
            label.configure(text=res) 
            entries.clear()  


#=================================================================================
    """ 
        The relWinEntCombo function generates a window for Relationships containing:
        2 entry boxes [source and destination classes] & 1 combobox the relationship
        type.

        params: number of box entry, # of combo, reltype, and alert message
    """
    def relWinEntCombo(numEntries: int, combo: int, title: str, labels : list):

        # Make a window for relationship add
        root = tk.Toplevel()
        root.title(title)
        root.geometry("550x200")

        
        # window's label, entry boxes, and combox for types.
        entryObjList = []
        
        # labels start at row 6, entry boxes/combo at row 7
        for x in range(numEntries):
            label = Label(root, text=labels[x]).grid(row=6, column=x, pady=20, padx=5)
            entry = Entry(root)
            entry.grid(row=7, column=x, pady=20, padx=5)
            entryObjList.append(entry)
            
        # set focus to the 1st entry box
        entryObjList[0].focus()
            
        # combobox for relationship types 
        #relType.set("")

        cbLabel = tk.Label(root,text = "Type")
        cbLabel.grid(column=3, row=6)
        typevar = tk.IntVar()
        relList=["Aggregation", "Composition", "Inheritance", "Realization"]
            
        typeCombo=ttk.Combobox(root, values=relList,width=15)
        #cb.place(x=0, y=0)
        typeCombo.grid(row=7,column=3)
        # typeCombo.current(0) #set the option to the 1st element
        # use current() to get the index of the currently selected element, 
        # and use get() method to get the element itself
        # obtain the index of elements in a combo
        #print(typevar.get())
        # get the value of elements in a combo
        #print(relList[typevar.get()])
        #print(cb.get())


        # Line Separator to display the message at the top section of the popup.
        lineseparator = ttk.Separator(root, orient = "horizontal")
        lineseparator.grid(row = 4, column = 0, sticky = "ew", columnspan=10)
        #lineseparator.pack(fill= 'x')


        # Label for outputing message.
        msgLabel = tk.Label(root, text = "")
        msgLabel.grid(row = 3, column = 0)

        # button to confirm 
        okButton = tk.Button(master =root, text="Go!", command=lambda:relationCommand( 
                            entryObjList[0].get(),entryObjList[1].get(),typeCombo.get(), msgLabel))
        okButton.grid(row = 9, column = 0, padx = 20, pady = 20)


        # Bind the enter key to the user's pressing button. This acts the same as the
        # user presses the button.
        root.bind('<Return>', lambda event:relationCommand(entryObjList[0].get(),entryObjList[1].get(),
                    typeCombo.get(), msgLabel))
                    

        entries.clear()

    """ 
        The relationCommand function binds the button to the relationshipAdd/Edit
    """
    def relationCommand(entry, entry2, type, label: tk.Label):
        if relationshipVar.get()=='Add':
            res = RelationshipAdd(entry,entry2,type) 
            label.configure(text=res) 
            entries.clear()
            #print(type)
            #c.addRelLine(entry,entry2,type)
            res = c.makeRelLine(entry,entry,type)
            label.configure(text=res) 
        else:
            res=relationshipEdit(entry, entry2,type)
            label.configure(text=res)
            entries.clear()

#=================================================================================
    """ 
        The attrWinEnt function generates a window for Attributes [methods/fields].
        
        params: # of entry boxes, return type, and alert message.
        
    """
    def attrWinEnt(numEntries: int,  title: str, labels : list):

        # Make a window 
        root = tk.Toplevel()
        root.title(title)
        root.geometry("550x200")

        # window's label, entry boxes, and combox for types.

        entryObjList = []
        # labels start at row 6, entry boxes/combo at row 7
        for x in range(numEntries):
            label = Label(root, text=labels[x]).grid(row=6, column=x, pady=20, padx=5)
            entry = Entry(root)
            entry.grid(row=7, column=x, pady=20, padx=5)
            entryObjList.append(entry)
            
        # set focus to the 1st entry box
        entryObjList[0].focus()
            
       
        # Line Separator to display the message at the top section of the popup.
        lineseparator = ttk.Separator(root, orient = "horizontal")
        lineseparator.grid(row = 4, column = 0, sticky = "ew", columnspan=10)
        #lineseparator.pack(fill= 'x')

        # Label for outputing message.
        msgLabel = tk.Label(root, text = "")
        msgLabel.grid(row = 3, column = 0)

        # button to confirm 
        okButton = tk.Button(master =root, text="Go!", command=lambda:attrCommand( 
                            entryObjList[0].get(),entryObjList[1].get(),entryObjList[2].get(), msgLabel))
        okButton.grid(row = 9, column = 0, padx = 20, pady = 20)


        # Bind the enter key to the user's pressing button. This acts the same as the
        # user presses the button.
        root.bind('<Return>', lambda event:attrCommand(entryObjList[0].get(),entryObjList[1].get()
                   ,entryObjList[2].get(),msgLabel))
                    

        entries.clear()

    """ 
        The attrCommand function binds the button to the Add/Rename functions
        for Methods/Fields/Params.
        
    """
    def attrCommand(entry, entry1, entry2, label: tk.Label):
        if methodsVar.get()=='Add':
            res = addMethod(entry,entry1,entry2, []) 
            label.configure(text=res) 
            entries.clear()
        if methodsVar.get() == 'Rename':
            res = renMethod(entry, entry1,entry2) 
            label.configure(text=res)  
            entries.clear()
        
        if fieldsVar.get()=='Add':
            res = addField(entry,entry1,entry2) 
            label.configure(text=res) 
            entries.clear()  
        
        if fieldsVar.get()=='Rename':
            res = renField(entry,entry1,entry2) 
            label.configure(text=res) 
            entries.clear()

        if parameterVar.get() == "Delete":
            res = delParam(entry,entry1,entry2) 
            label.configure(text=res) 
            entries.clear()


        
#=================================================================================
    """ 
        The attrWinEnt function generates a window for ClassDelete/MethodDelete/
        FieldDelete/RelationshipsDelete.

        params: # of entry boxes, type, and alert message.

    """
    def delAttrWinEnt(numEntries: int,  title: str, labels : list):

        # Make a window
        root = tk.Toplevel()
        root.title(title)
        root.geometry("550x200")

        
        # window's label, entry boxes, and combox for types.

        entryObjList = []
        # labels start at row 6, entry boxes/combo at row 7
        for x in range(numEntries):
            label = Label(root, text=labels[x]).grid(row=6, column=x, pady=20, padx=5)
            entry = Entry(root)
            entry.grid(row=7, column=x, pady=20, padx=5)
            entryObjList.append(entry)
            
        # set focus to the 1st entry box
        entryObjList[0].focus()
            
       
        # Line Separator to display the message at the top section of the popup.
        lineseparator = ttk.Separator(root, orient = "horizontal")
        lineseparator.grid(row = 4, column = 0, sticky = "ew", columnspan=10)
        #lineseparator.pack(fill= 'x')

        # Label for outputing message.
        msgLabel = tk.Label(root, text = "")
        msgLabel.grid(row = 3, column = 0)

        # button to confirm 
        okButton = tk.Button(master =root, text="Go!", command=lambda:delAttrCommand( 
                            entryObjList[0].get(),entryObjList[1].get(), msgLabel))
        okButton.grid(row = 9, column = 0, padx = 20, pady = 20)


        # Bind the enter key to the user's pressing button. This acts the same as the
        # user presses the button.
        root.bind('<Return>', lambda event:delAttrCommand(entryObjList[0].get(),entryObjList[1].get(),msgLabel))
                    

        entries.clear()

    """ 
        The delAttrCommand function binds the button to ClassDelete/MethodDelete/
        FieldDelete/RelationshipsDelete.
        
    """
    def delAttrCommand(entry, entry1, label: tk.Label):
        if methodsVar.get() == 'Delete':
            res = delMethod(entry, entry1) 
            label.configure(text=res) 
            entries.clear()  

        if fieldsVar.get()=='Delete':
            res = delField(entry,entry1) 
            label.configure(text=res)
            entries.clear() 

        if classVar.get() == 'Rename':
            res = ClassRename(entry, entry1) 
            label.configure(text=res)
            entries.clear() 
 
  
        if relationshipVar.get() == 'Delete':
            res = RelationshipDelete(entry,entry1)
            label.configure(text=res) 
            entries.clear()  
#=================================================================================
    """ 
        The paramWinEnt function generates a window for ParamAdd & ParamRename.

    """
    def paramWinEnt(numEntries: int,  title: str, labels : list):

        # Make a window for relationship add
        root = tk.Toplevel()
        root.title(title)
        root.geometry("550x200")

        
        # window's label, entry boxes, and combox for types.

        entryObjList = []
        # labels start at row 6, entry boxes/combo at row 7
        for x in range(numEntries):
            label = Label(root, text=labels[x]).grid(row=6, column=x, pady=20, padx=5)
            entry = Entry(root)
            entry.grid(row=7, column=x, pady=20, padx=5)
            entryObjList.append(entry)
            
        # set focus to the 1st entry box
        entryObjList[0].focus()
            
       
        # Line Separator to display the message at the top section of the popup.
        lineseparator = ttk.Separator(root, orient = "horizontal")
        lineseparator.grid(row = 4, column = 0, sticky = "ew", columnspan=10)
        #lineseparator.pack(fill= 'x')

        # Label for outputing message.
        msgLabel = tk.Label(root, text = "")
        msgLabel.grid(row = 3, column = 0)

        # button to confirm 
        okButton = tk.Button(master =root, text="Go!", command=lambda:paramCommand( 
                            entryObjList[0].get(),entryObjList[1].get(),
                            entryObjList[2].get(),entryObjList[3].get(),  msgLabel))
        okButton.grid(row = 9, column = 0, padx = 20, pady = 20)


        # Bind the enter key to the user's pressing button. This acts the same as the
        # user presses the button.
        root.bind('<Return>', lambda event:paramCommand(entryObjList[0].get(),entryObjList[1].get()
                    ,entryObjList[2].get(),entryObjList[3].get(), msgLabel))
                    

        entries.clear()

    """ 
        The paramCommand function binds the button to the ParamAdd/ParamRename methods
        
    """
    def paramCommand(entry, entry1, entry2, entry3, label: tk.Label):
        if parameterVar.get() == 'Add':
            res = ParamAdd(entry, entry1, entry2, entry3) 
            label.configure(text=res)
            entries.clear()   

        if parameterVar.get() == 'Rename':
            res = renameParam(entry,entry1, entry2, entry3) 
            label.configure(text=res)
            entries.clear()   


# =============================================================================
    # message Box is not used.
    messageBox = tk.Text(window, height=15, width=35, wrap='word')
    messageBox.insert('end', "Messages will appear here.")
    # make a new message with given string
    def throwMessage(mes: str):
        if mes is not None:
            messageBox.delete(1.0, 'end')
            messageBox.insert('end', mes)

# =============================================================================
    """ 
        SYNTAX:
            OptionMenu(master, variable, value, *values, **kwargs)

            1. master is the window that the OptionMenu will be placed in.
            2. variable is the object that holds the currently selected option
               of the OptionMenue and can be implemented as one of the followings:
                    StringVar()
                    IntVar()
                    DoubleVar()
                    BooleanVar()
            3. value depends on the type variable, i.e. StringVar(), then the 
               value can be any name or a set of characters.
            4. *value is the name of the list that stores all the options.
            5. kwargs is the widget specific configuration.

    
    """

    # drop down menu for each control-tabs
    
    classDrop = tk.OptionMenu(classTab, classVar, *classOptions)#.place(x = 0, y =30)
    classDrop.grid(column=0,row=1)
    
    relationshipDrop = tk.OptionMenu(relTab, relationshipVar, *relationshipOptions)#.place(x=60, y=30)
    relationshipDrop.grid(column=0,row=1)
    
    fieldsDrop = tk.OptionMenu(fieldTab, fieldsVar, *fieldsOptions)#.place(x=140, y=30)
    fieldsDrop.grid(column=0,row=1)

    
    methodsDrop = tk.OptionMenu(methodTab, methodsVar, *methodsOptions)#.place(x=200, y=30)
    methodsDrop.grid(column=0,row=1)
    
    parameterDrop = tk.OptionMenu(paramTab, parameterVar, *parameterOptions)#.place(x=275, y=30)
    parameterDrop.grid(column=0,row=1)
    
    #listClassButton = tk.Button(listClassTab, text="List Class", command=listClassCall)#.place(x=75, y=70)
    #listClassButton.grid(column=0,row=3)
    listClassesButton = tk.Button(listClassTab, text="List Classes", command=listClassesCall)
    listClassesButton.grid(column=0,row=3)
    
    listRelationshipsButton = tk.Button(listClassTab, text="List Relationships", command=listRelationshipsCall)#.place(x=165, y=70)
    listRelationshipsButton.grid(column=0,row=9)
    
    #messageBox.place(x=30, y=100)


# =============================================================================

    # keeping track of whether a drop down menu option was selected
    classVar.trace("w", classCalls)
    relationshipVar.trace("w", relationshipCalls)
    methodsVar.trace("w", methodCalls)
    fieldsVar.trace("w", fieldCalls)
    parameterVar.trace("w", parameterCalls)


# =============================================================================
    
    window.mainloop()

# =============================================================================

if __name__ == "__main__":
    gui_run()