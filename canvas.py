# Project Name  : UML_BootSnake
# File Name     : canvas.py
# Course        : CSCI 420
# Professor     : Dr. Stephanie Schwartz
# BootSnake Team: Amelia S., Andy P., Ben M., Tram T., Travis Z.


###############################################################################



#from decimal import MAX_EMAX
#from re import I
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import ttk
from PIL import *  # to use PIL import, install pip install Pillow as PIL is deprecated and pillow is the successor
import PIL.ImageGrab as ImageGrab


from classModel import *
from relationshipsModel import *
from saveLoadModel import *
from attributesModel import *
from interfaceView import *
from parametersModel import *
from sharedItems import *
from gui import *


#####################################################################################

#global variable to keep track of how many rectangle boxes are added
boxlist = list()


# set up a canvas in main panel
def makeCanvas(frame: tk.Frame):
    # when putting a canvas in a function, create a global variable 
    # to ensure that boxes are working properly. 
    # Set the scrollable region for the Canvas. If the total canvas'
    # size is  500 by 500, but only 300 by 300 is viewable. 
    # The scroll region should always be larger than the width and height.
    
    global my_canvas
    
    my_canvas = tk.Canvas(frame, bg= "#FFFFFF", width = 400, height=400, scrollregion=(0,0, 500, 500))
    #my_canvas.pack()
    
    return my_canvas

# save a screenshot of the canvas
def saveCanvas(filename : str):
    x = my_canvas.winfo_rootx() + my_canvas.winfo_x()
    y = my_canvas.winfo_rooty() + my_canvas.winfo_y()
    xx = x + my_canvas.winfo_width() - 20
    yy = y + my_canvas.winfo_height()
    ImageGrab.grab(bbox=(x, y, xx, yy)).save(filename)
    #my_canvas.after(1000, saveCanvas(filename))


class makeSquare():
    """
        The makeSquare class contains a constructor to initialize any classbox
        created.

    """
    def __init__(self, name: str, x1:int, y1:int, x2:int, y2:int ):
       
        my_rectangle = my_canvas.create_rectangle(x1, y1, x2, y2, fill = 'red', width = 2, tag=name)
        # create a label for a class rectangle.
        # if changing the order of widget is not an option, use the cavas' tag_raise method
        boxlabel = my_canvas.create_text(((x1+x2)/2),y1, text = name, font=('Roboto'), anchor=S) #'Helvetica 12 bold'
        spacing = 2* len(name)

        yincrement = 20
        # create a field line, field label, and field text inside a class rectangle.
        fline = my_canvas.create_line(x1, y1, x2, y2, fill='black', width =2)
        flabel = my_canvas.create_text(x1 - 40, y1 - 40, text = 'Field(s):', anchor=W)
        ftext = my_canvas.create_text(x1 - 45, y1 - 45, text ="", anchor = N)
        


        # create a method line, method label, and method text inside a class rectangle.
        mline = my_canvas.create_line(x1, y1, x2, y2, fill ='black', width = 2)
        mlabel = my_canvas.create_text(x1 - 15, y1 - 15, text = 'Method(s):', anchor=W)
        mtext = my_canvas.create_text(x1 - 10, y1 - 10, text ="", anchor = N)
        
        
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
        self.yincrement = yincrement
        dragBox(my_rectangle)



def addRec(name:str):
    """ 
    create a class rectangle when a class is added and add it to the canvas

    """
    
    placed = False # ensure that a box is not previously occupied at the same place.
    x1 = 50
    y1 = 80
    x2 = 160
    y2 = 15
    
    # checking if there were coordinates assigned beforehand (load)
    my_class = ClassSearch(name, listOfClasses)
    if my_class.x != 0 or my_class.y != 0:
        x2 = my_class.x
        y2 = my_class.y
        x1 = x2 + 120
        y1 = y2 + 65
    
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
            
            else: # align boxes vertically
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
    for o in boxlist:
        print(my_canvas.coords(o.name))
    updateBoxSize(len(boxlist)-1)

    loc = searchBox(name)
    x1, y1, x2, y2 = my_canvas.coords(boxlist[loc].my_rectangle)

    my_class.x = x1
    my_class.y = y1



###############################################################################

def updateBoxSize(wbox: int):
    """
    The undateBoxsize function updates the width of the box located at the
    given index in the boxlist.
    """
    boxname = boxlist[wbox].name
    boxwidth = 4 * len(boxlist[wbox].name)

    
    for o in listOfClasses:
        for x in o.listOfFields:
            fname = x.name + " " + x.type
            if len(fname)*2 > boxwidth:
                boxwidth = len(fname)*2
        
        for m in o.listOfMethods:
            mname = m.name + " " + m.type + "("
            if len(mname)*2 > boxwidth:
                boxwidth = len(mname)*2
            for p in m.listOfParams:
                pname = p.name + " " + p.type +")"
                if len(pname)*2 > boxwidth:
                    boxwidth = len(pname)*2
    
    boxlist[wbox].spacing = boxwidth

    # get the coordinates of the box
    x1, y1, x2, y2 = my_canvas.coords(boxlist[wbox].my_rectangle)
    my_canvas.coords((boxlist[wbox].my_rectangle), x1, y1, x2, y2)
    my_canvas.coords((boxlist[wbox].boxlabel), ((x1+x2)/2), y1+15)

    midpoint = (x1+x2)/2
    # to resize the rectangle box using the coords().
    # set line
    xf, yf = my_canvas.coords(boxlist[wbox].flabel)
    my_canvas.coords((boxlist[wbox].fline), x1, y1+15, x2, y1+15)
    my_canvas.coords((boxlist[wbox].flabel), x1+5, yf)
    my_canvas.coords((boxlist[wbox].ftext), x1+35, yf)
    my_canvas.itemconfigure((boxlist[wbox].fline))
    my_canvas.itemconfigure((boxlist[wbox].flabel))
    xm, ym = my_canvas.coords(boxlist[wbox].mlabel)
    my_canvas.coords((boxlist[wbox].mline), x1, y1+40,x2, y1+40)
    my_canvas.coords((boxlist[wbox].mlabel), x1+5, ym)
    my_canvas.coords((boxlist[wbox].mtext), x1+35, ym)

    
###########################################################################################

def updateBoxHeight(h:int):
    boxlist[h].yincrement = 30
    name = boxlist[h].name
    
    # increase the box's height to contain fields, methods, & params.
    for o in listOfClasses:
        for x in o.listOfFields:
            boxlist[h].yincrement +=15
    
    for m in o.listOfMethods:
        boxlist[h].yincrement += 45
        for p in m.listOfParams:
            boxlist[h].yincrement += 15
    

    wantedClass = ClassSearch(boxlist[h].name, listOfClasses)
    #print(len(wantedClass.listOfFields))
   
    # get the coords of the box
    x1, y1, x2, y2 = my_canvas.coords(boxlist[h].my_rectangle)
    
    # get the coords of field label
    xf, yf = my_canvas.coords(boxlist[h].flabel)
   
    # method's text
    xm, ym = my_canvas.coords(boxlist[h].mtext)
    # method's label
    xl, yl = my_canvas.coords(boxlist[h].mlabel)
    
    # move the method's label according to the length of fields.
    my_canvas.coords(boxlist[h].mlabel, xl, yf+20 +20*len(wantedClass.listOfFields) )
    xl, yl = my_canvas.coords(boxlist[h].mlabel)
    my_canvas.coords(boxlist[h].mline, x1, yl-10, x2, yl-10)
    
    # move the method's text according to method's label.
    my_canvas.coords(boxlist[h].mtext, xm+5, yl+10)

    # move the class box
    my_canvas.coords(boxlist[h].my_rectangle, x1, y1,x2, y1 + boxlist[h].yincrement + 30)

    
    # bring all components to front
    boxlist[h].my_rectangle
    boxlist[h].boxlabel
    boxlist[h].fline
    boxlist[h].flabel
    boxlist[h].ftext
    boxlist[h].mline
    boxlist[h].mlabel
    boxlist[h].mtext


##############################################################################

def searchBox(name:str):
    """
    The searchBox function searches the boxlist of classes for the given 
    classname by name and return its index.
    """
    i = 0
    
    while i < len(boxlist):
        if boxlist[i].name== name:
            #print(boxlist[i].name)
            return i

        i += 1


def searchBoxLoc(name:str):
    """
    The searchBoxLoc function searches the boxlist of rectangles for 
    the given rectangle by name and return its index.
    """
    i = 0
    while i < len(boxlist):
        if boxlist[i].my_rectangle == name:
            return i

        i += 1



#############################################################################

def addBoxInfo(name: str):
    """

    addBoxInfo function verifies that no duplicates allowed when 
    creating boxes.

    """
    for o in boxlist:
        if o.name == name:
            msg: str = f"Box {name} already created!"
            return msg       
    addRec(name)




def makeRelLine(src: str, dest: str, type:str):
    """
    The makeRelLine function adds a relation line to the box.
    """
    msg =""
    
    for o in listOfClasses:
        for x in o.listOfRelationships:
            
            if searchBox(x.src) ==  searchBox(x.dest):
                
                msg = f"Relation existed!"
                return msg
        addRelLine(src, dest, type)
    
    
    

def addFieldInfo(name:str):
    """
    The addFieldInfo adds a list of fields in the box
    """

    boxloc = searchBox(name)
    
    wantedClass = ClassSearch(name, listOfClasses)
    
    fieldtext =""
    for o in wantedClass.listOfFields:
        fieldtext = fieldtext + " " + o.name + " " + o.type + "\n"
    
    
    my_canvas.itemconfigure(boxlist[boxloc].ftext, text = fieldtext, justify = tk.LEFT, state=tk.DISABLED)
    updateBoxSize(boxloc)
    updateBoxHeight(boxloc)



def addMethodInfo(name:str):
    """
    The addMethodInfo adds a list of methods & params in the box.
    """
    boxloc = searchBox(name)
    methodtext =""

    wantedClass = ClassSearch(name, listOfClasses)
    
    for m in wantedClass.listOfMethods:
            methodtext = methodtext + " " + m.name + " " + m.type + "(\n"
            for p in m.listOfParams:
                methodtext = methodtext + " " + p.name + " " + p.type +"\n" 
                        
            methodtext = methodtext +")\n\n"
    
    
    my_canvas.itemconfigure(boxlist[boxloc].mtext, text = methodtext, justify = tk.LEFT, state=tk.DISABLED)
    updateBoxSize(boxloc)
    updateBoxHeight(boxloc)



def renameBox(name:str, newname:str):
    """
    The renameBox updates the box's label to the new label provided that the
    label does not already exist in the boxlist.
    """
    
    # if newname is not in boxlist
    if (searchBox(newname) == None):
        i = 0
        for o in boxlist:
            if name == o.name:
                boxlist[i].name = newname
                break
                
            else:
                i +=1
    
        # rename the text of the box
        my_canvas.itemconfigure((boxlist[i].boxlabel), text=newname) 
        # update the width of the box
        updateBoxSize(i)


def delBox(name: str):
    """
    The delBox deletes the given box and any relation associated 
    with it, if any.
    """
    
    boxloc = searchBox(name)
    # delete all lines associated with the source box
    # ('src','dest',reltype,relline )
    #   [0] ,  [1] ,  [2]  , [3]
    
    for i in boxlist:
        
        while len(i.relation) > 0:
            my_canvas.delete(i.relation[0][1])
            my_canvas.delete(i.relation[0][3])
            i.relation.pop(0)
        i.relation = []
    
        
    # delete all box's components
    my_canvas.delete(boxlist[boxloc].my_rectangle)
    my_canvas.delete(boxlist[boxloc].boxlabel)
    my_canvas.delete(boxlist[boxloc].fline)
    my_canvas.delete(boxlist[boxloc].flabel)
    my_canvas.delete(boxlist[boxloc].ftext)

    my_canvas.delete(boxlist[boxloc].mline)
    my_canvas.delete(boxlist[boxloc].mlabel)
    my_canvas.delete(boxlist[boxloc].mtext)

    boxlist.pop(boxloc)


def delLine(name: str):
    boxloc = searchBox(name)
    # delete all lines associated with the source box
    # ('src','dest',reltype,relline )
    #   [0] ,  [1] ,  [2]  , [3]
    
    for i in boxlist:
        
        while len(i.relation) > 0:
            #my_canvas.delete(i.relation[0][1])
            my_canvas.delete(i.relation[0][3])
            i.relation.pop(0)
        i.relation = []
    
def editLine(src: str, dest:str, type:str):
    delLine(src)
    addRelLine(src,dest,type)
#####################################################################
#https://www.youtube.com/watch?v=Z4zePg2M5H8

def dragBox(my_rectangle):

    my_canvas.tag_bind(my_rectangle,"<B1-Motion>", on_drag)
    my_canvas.tag_bind(my_rectangle,"<ButtonRelease-1>", on_release)

# save location to class when mouse button is released
def on_release(e):
    global clicked
    clicked = my_canvas.find_closest(e.x,e.y)
    i = 0
    
    for o in boxlist:
        if clicked[0] in {o.my_rectangle, o.boxlabel, o.flabel, o.ftext, o.mlabel, o.mtext, o.fline, o.mline}:
            blabel = o.boxlabel
            box = o.my_rectangle
            break
        i += 1

    loc = searchBox(o.name)
    x1, y1, x2, y2 = my_canvas.coords(boxlist[loc].my_rectangle)
    
    my_class = ClassSearch(boxlist[loc].name, listOfClasses)
    my_class.x = x1
    my_class.y = y1


def on_drag(e):
    #e.x
    #e.y
    """
    .find_closest(x, y, halo=None, start=None) returns a singleton Tuple containing 
    # the object ID of the object closest to point (x, y). 
    # If there are no qualifying objects, returns an empty tuple.
    # Use the halo argument to increase the effective size of the point. 
    # For example, halo=5 would treat any object within 5 pixels of (x, y) as overlapping.
    # If an object ID is passed as the start argument, this method returns the 
    # highest qualifying object that is below start in the display list.
    
    .find_enclosed(x1, y1, x2, y2) returns a list of the object IDs of all objects 
    that occur completely within the rectangle whose top left corner is (x1, y1) 
    and bottom right corner is (x2, y2).

    .coords(tagOrId, x0, y0, x1, y1, ..., xn, yn).If only the tagOrId argument is passed, 
    returns a tuple of the coordinates of the lowest or only object specified by that argument.
    The number of coordinates depends on the type of object. In most cases it will be a 
    4-tuple (x1, y1, x2, y2) describing the bounding box of the object. Move an object 
    by passing in new coordinates.
    """
    
    global clicked
    clicked = my_canvas.find_closest(e.x,e.y)
    i = 0
    
    
    # get the index of the clicked-on box's contents returned by .find_closest() 
    # by iterating through a dict. 
    for o in boxlist:
        if clicked[0] in {o.my_rectangle, o.boxlabel, o.flabel, o.ftext, o.mlabel, o.mtext, o.fline, o.mline}:
            blabel = o.boxlabel
            box = o.my_rectangle
            break
        i += 1
    
    # bring-to-front all selected items of the clicked-on box
    my_canvas.coords(boxlist[i].my_rectangle)
    my_canvas.coords(boxlist[i].boxlabel)
   
    my_canvas.coords(boxlist[i].flabel)
    my_canvas.coords(boxlist[i].ftext)
    
    my_canvas.coords(boxlist[i].mlabel)
    my_canvas.coords(boxlist[i].mtext)
    my_canvas.coords(boxlist[i].fline)
    my_canvas.coords(boxlist[i].mline)
    
    # set the coordinates of the box & retain its shape while dragging
    x1 = e.x-30 - boxlist[i].spacing
    y1 = e.y-10
    x2 = e.x+50 + boxlist[i].spacing
    y2 = e.y+ boxlist[i].yincrement

    # get the coordinators of the box
    midx1, midy1, midx2, midy2 = my_canvas.coords(boxlist[i].my_rectangle)
    
    # move the box's components
    my_canvas.coords(box, x1, y1, x2 + 30, y2 + 30)
    my_canvas.coords(blabel, x1+55+boxlist[i].spacing, y1+15)

    # field section
    my_canvas.coords(boxlist[i].fline, x1, y1 + 15, x2 + 30, y1 + 15)
    my_canvas.coords(boxlist[i].flabel, midx1 + 5, y1+25)
    xf,yf = my_canvas.coords(boxlist[i].flabel)
    my_canvas.coords(boxlist[i].ftext, x1+20, yf+5)
    

    # method section
    my_canvas.coords(boxlist[i].mlabel, midx1 + 5, y1 + 50)
   
    
    xm,ym = my_canvas.coords(boxlist[i].mlabel)
    
    my_canvas.coords(boxlist[i].mline, x1, y1 + 40 , x2 + 30, y1 + 40)
    my_canvas.coords(boxlist[i].mtext,x1+20, ym+10)

    # move relationship line associated with the boxes by looping through
    # the boxlist's relation list to find all items in the box's relation list:
    # src, line-type, dest, shape, & relation type. Then use the 
    # canvas.coords() method to redefine the points.
    
    # i.e. the id/the tag of the line/any widget that moved, canvas.coords(line) 
    # method returns the coordinates of the line/widget[pt1 & pt2], representing the 
    # origin & the end of the line. One of these two points will be the start 
    # coordinate of the new line when moving the object. When releasing the mouse,
    # a function will be called. The first argument of that function is event 
    # containing the coordinates of the mouse when releasing the mouse button.
    # These coordinates (event.x and event.y) will be the end of the new line.
    
    #print(boxlist[i].relation)
    
    # loc = searchBox(o.name)
    # x1, y1, x2, y2 = my_canvas.coords(boxlist[loc].my_rectangle)
    
    # my_class = ClassSearch(boxlist[i].name, listOfClasses)
    # my_class.x = x1
    # my_class.y = y1


    if len(boxlist[i].relation) > 0:
        for o in boxlist[i].relation:
            # ('src','dest',reltype,relline )
            #   [0] ,  [1] ,  [2]  , [3]
            if o[0] == 'src':
                x1,y1,x2,y2 = my_canvas.coords(o[3])
                my_canvas.coords(o[3], midx1, midy1, x2, y2)
                
            if o[0] == 'dest':
                x1,y1,x2,y2 = my_canvas.coords(o[3])
                my_canvas.coords(o[3], x1, y1, midx1, midy1)
                            
    

#########################################################################

class relLine():
    """
    
    This class contains a constructor to initialize the relationship types when
    created.

    The relation types are created using the create_polygon to make the shape
    of the relation types and the create_line widgets.

    A polygon [requires at least 3 coordinators => an isosceles triangle]
    
    state: tk.NORMAL state - default
           tk.HIDDEN makes the widget invisible, 
           tk.DISABLED makes it unresponsive to the mouse.

    SYNTAX: 
            id = C.create_polygon(x0, y0, x1, y1, ..., option, ...)

    REFERRENCE:
        https://www.youtube.com/watch?v=yXdf12H-2x8
        https://python-course.eu/tkinter/canvas-widgets-in-tkinter.php
    
    """

    def __init__(self, x1,y1, x2,y2, src, dest, reltype):
        srcloc = searchBoxLoc(src)
        destloc = searchBoxLoc(dest)
        
        
        if (reltype == "Aggregation"):
            color = "green"
            dashline = False
         
        elif (reltype == "Composition"):
            color = "yellow"
            dashline = False

        elif (reltype == "Inheritance"):
            color = "blue"
            dashline = False  

        else:
            color = "purple"
            dashline = True 

        if not dashline:
            relline = my_canvas.create_line(x1,y1,x2, y2, arrow=tk.LAST, fill=color, width=2) 
        
        else:
            relline = my_canvas.create_line(x1,y1,x2, y2, arrow=tk.LAST,fill=color, width=2, dash=(200,200)) 
        
        # tag_lower() and tag_raise() methods of the canvas brings the item to front
        my_canvas.tag_lower(relline)
        
        # add the relation components to the relation list.
        boxlist[srcloc].relation.append(('src','dest',reltype,relline )) #[0]src, [1]dest, [2]type, [3]line
        boxlist[destloc].relation.append(('dest','src',reltype,relline))
        
def addRelLine(src:str, dest:str, reltype:str):
    
    srcrec = boxlist[searchBox(src)].my_rectangle
    destrec = boxlist[searchBox(dest)].my_rectangle
    xsrc = my_canvas.coords(srcrec)[0]
    ysrc = my_canvas.coords(srcrec)[1]
    xdest = my_canvas.coords(destrec)[0]
    ydest = my_canvas.coords(destrec)[1]

    
    #instantiate the line
    myLine = relLine(xsrc, ysrc, xdest, ydest,srcrec, destrec,reltype)

