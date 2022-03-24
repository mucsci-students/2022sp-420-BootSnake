# Project Name  : UML_BootSnake
# File Name     : canvas.py
# Course        : CSCI 420
# Professor     : Dr. Stephanie Schwartz
# BootSnake Team: Amelia S., Andy P., Ben M., Tram T., Travis Z.


###############################################################################





from decimal import MAX_EMAX
from re import I
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import ttk
from PIL import *  # to use PIL import, install pip install Pillow as PIL is deprecated and pillow is the successor

from classModel import *
from relationshipsModel import *
from saveLoad import *
from attributesModel import *
from interfaceView import *
from parametersModel import *
from gui import *


#####################################################################################

#global variable to keep track of how many rectangle boxes are added
boxlist = list()


# set up a canvas in main panel
def makeCanvas(frame: tk.Frame):
    # when putting a canvas in a function, create a global variable 
    # to ensure that boxes are working properly. 
    global my_canvas
    
    my_canvas = tk.Canvas(frame, bg= "#FFFFFF", width = 400, height=400, scrollregion=(0,0, 5, 5))
    #my_canvas.pack()
    

    
    
    return my_canvas

class makeSquare():
    """
        The makeSquare class contains a constructor to initialize any classbox
        created.

    """
    def __init__(self, name: str, x1:int, y1:int, x2:int, y2:int ):
       
        my_rectangle = my_canvas.create_rectangle(x1, y1, x2, y2, fill = 'red', width = 2, tag=name)
        # create a label for a class rectangle.
        # if changing the order of widget is not an option, use the cavas' tag_raise method
        boxlabel = my_canvas.create_text(((x1+x2)/2),y1, text = name, font=('Helvetica 12 bold'), anchor=S) 
        spacing = 2* len(name)

        yincrement = 20
        # create a field line, field label, and field text inside a class rectangle.
        fline = my_canvas.create_line(x1, y1, x2, y2, fill='green', width =2)
        flabel = my_canvas.create_text(x1 - 50, y1 - 50, text = 'Field(s):', anchor=W)
        ftext = my_canvas.create_text(x1 - 45, y1 - 45, text ="", anchor = N)
        


        # create a method line, method label, and method text inside a class rectangle.
        mline = my_canvas.create_line(x1, y1, x2, y2, fill ='black', width = 2)
        mlabel = my_canvas.create_text(x1 - 30, y1 - 30, text = 'Method(s):', anchor=W)
        mtext = my_canvas.create_text(x1 - 15, y1 - 15, text ="", anchor = N)
        
        
        self.my_rectangle = my_rectangle
        self.name = name
        self.boxlabel = boxlabel
        self.spacing = spacing
        self.fline = fline
        self.flabel = flabel
        self.ftext = ftext
        self.mline = mline
        self.mlabel = mlabel
        self.mtext = mtext
        self.relation = list()
        #canDrag(my_rectangle)



def addRec(name:str):
    """ 
    create a class rectangle when a class is added and add it to the canvas

    """
    
    placed = False # ensure that a box is not previously occupied at the same place.
    x1 = 50
    y1 = 60
    x2 = 160
    y2 = 20
    
    # define the box and ensure they are not overlapped
    
    space:int =0
    if len(boxlist) > 0:
        space = boxlist[len(boxlist)-1].spacing

    
    while not placed:
        if len(my_canvas.find_overlapping((x1-space), y1, x2, y2)) != 0:
            
        # when numerous boxes created that occupy more than the canvas'size,
        # winfo height window Returns a decimal string giving window's height
        # in pixels. When a window is first created its height will be 1 pixel; 
        # the height will eventually be changed by a geometry manager to 
        # fulfill the window's needs. If you need the true height immediately 
        # after creating a widget, invoke update to force the geometry manager
        # to arrange it, or use winfo reqheight to get the window's requested 
        # height instead of its actual height.
            
            if y2 > my_canvas.winfo_height() + 40:
                space = 0
                x1 = 50
                y1 += 50
                x2 = 160
                y2 += 50
            
            else:
                y1 += 10
                y2 += 10

            
        
        else:
            placed = True


    # instantiate class rectangle
    classRec = makeSquare(name, x1, y1,x2,y2)
    # the order of the widgets matters when displayed (bring to front), 
    # otherwise use the tag_raise
    classRec.my_rectangle
    classRec.boxlabel
    classRec.fline
    classRec.flabel
    classRec.ftext
    classRec.mline
    classRec.mlabel
    classRec.mtext

    """
    my_canvas.tag_raise(classRec.my_rectangle)
    my_canvas.tag_raise(classRec.boxlabel)
    my_canvas.tag_raise(classRec.fline)
    my_canvas.tag_raise(classRec.flabel)
    my_canvas.tag_raise(classRec.ftext)
    my_canvas.tag_raise(classRec.mline)
    my_canvas.tag_raise(classRec.mlabel)
    my_canvas.tag_raise(classRec.mtext)
    """

    # Add the new rectangle to the list.
    boxlist.append(classRec)
    updateRecSize(len(boxlist)-1)




###############################################################################

def updateRecSize(wbox: int):
    boxname = boxlist[wbox].name
    longname = 2 * len(boxlist[wbox].name)
    
    x1, y1, x2, y2 = my_canvas.coords(boxlist[wbox].my_rectangle)
    my_canvas.coords((boxlist[wbox].my_rectangle), x1, y1, x2, y2)
    my_canvas.coords((boxlist[wbox].boxlabel), ((x1+x2)/2), y1+15)

    mid = (x1+x2)/2
    # set line
    xf, yf = my_canvas.coords(boxlist[wbox].flabel)
    my_canvas.coords((boxlist[wbox].fline), x1, y1+20, x2, y1+20)
    my_canvas.coords((boxlist[wbox].flabel), x1+5, yf)
    my_canvas.coords((boxlist[wbox].ftext), x1+10, yf)
    my_canvas.itemconfigure((boxlist[wbox].fline))
    my_canvas.itemconfigure((boxlist[wbox].flabel))
    xm, ym = my_canvas.coords(boxlist[wbox].mlabel)
    my_canvas.coords((boxlist[wbox].mline), x1, y1+30,x2, y1+30)
    my_canvas.coords((boxlist[wbox].mlabel), x1+5, ym)
    my_canvas.coords((boxlist[wbox].mtext), x1+10, ym)

    return mid

    





    


##############################################################################

def searchBox(name:str):
    """
    The searchBox function searches for the class rectangle by name
    """
    i = 0
    
    while i < len(boxlist):
        if boxlist[i].name== name:
            return i

    i += 1


def searchBoxLoc(name:str):
    """
    The searchBoxLoc function locates the class rectangle's position
    """
    i = 0
    while i < len(boxlist):
        if boxlist[i].my_rectangle == name:
            return i

        i += 1




#############################################################################

def addBoxInfo(name: str):
    for o in boxlist:
        if o.name == name:
            msg: str = f"Box {name} already created!"
            return msg       
    addRec(name)

    
            









#########################################################################

class relLine():
    """
    
    This class contains a constructor to initialize the relationship types when
    created.
    
    """
    def __init__(self, x1,y1, x2,y2, src, dest, reltype):
        srcloc = searchBoxLoc(src)
        destloc = searchBoxLoc(dest)
        
        relline = my_canvas.create_line(x1,y1,x2, y2, arrow=tk.LAST, fill=reltype) 
        my_canvas.tag_lower(relline)
        boxlist[srcloc].relation.append((src, relline, dest))
        boxlist[destloc].relation.append((dest, relline, src))
        
    
def addRelLine(src:str, dest:str, reltype:str):
    srcloc = searchBox(src)
    destloc = searchBox(dest)
   
    if (reltype == "Aggregation"):
        color = "green"
        
    if (reltype == "Composition"):
        color = "yellow"
        
    if (reltype == "Inheritance"):
        color = "red"

    else:
        color = "purple"

    srcrec = boxlist[searchBox(src)].my_rectangle
    destrec = boxlist[searchBox(dest)].my_rectangle
    xsrc = my_canvas.coords(srcrec)[0]
    ysrc = my_canvas.coords(srcrec)[1]
    xdest = my_canvas.coords(destrec)[0]
    ydest = my_canvas.coords(destrec)[1]


    #instantiate the line
    myLine = relLine(xsrc, ysrc, xdest, ydest,srcrec, destrec,color)

    
