# Project Name  : UML_BootSnake
# File Name     : canvas.py
# Course        : CSCI 420
# Professor     : Dr. Stephanie Schwartz
# BootSnake Team: Amelia S., Andy P., Ben M., Tram T., Travis Z.


###############################################################################

from classModel import *
from relationshipsModel import *
from saveLoadModel import *
from attributesModel import *
from interfaceView import *
from parametersModel import *
from gui import *
from canvas import *


undoList = list()
redoList = list()

class SaveLocation():

    def __init__(self,mode):
    
        classCopy = list()  
        coordList = list()
        fieldCopy = list()
        methodCopy = list()
        paramCopy = list()
        relationCopy = list()

        # make a copy of methods, params, fields, and relationships.
        for o in listOfClasses:
            for m in o.listOfMethods:
                for p in m.listOfParams:
                    paramCopy.append(p.name, p.type)
                
                methodCopy.append(m.name, m.type, paramCopy.copy())

            
            for f in o.listOfFields:
                fieldCopy.append(f.name, f.type)

            for r in o.listOfRelationships:
                relationCopy.append(r.src,r.dest, r.type)

            
            self.listOfRelationships = relationCopy

            if mode =="gui":
                boxCoords = getXY(o.name)
                x = boxCoords[0]
                y = boxCoords[1]

            else:
                x = o.positionx
                y = o.positiony

            # Put together all of the lists and class name, fields, methods, params,
            # x & y location and append it to the list.
            classObj = {"name": x.name , "fields": fieldCopy , "methods": methodCopy, "positionx": x, "positiony":y}
            classCopy.append(classObj)

            fieldCopy = []
            methodCopy = []
            paramCopy =[]

        self.coordList = coordList
        self.classCopy = classCopy

def saveLoc( mode = "gui"):
    undoList.append(SaveLocation(mode))


def getXY(name:str):
    loc = searchBox(name)
    x1, y1, x2, y2 = my_canvas.coords(boxlist[loc].my_rectangle)
    midx = abs(x2-x1)/2
    return (midx, y1)

        

