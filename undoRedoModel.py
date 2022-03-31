global undoListInsertable
undoListInsertable = True
from classModel import *
from attributesModel import *
from parametersModel import *
from relationshipsModel import *

undoList = list()
redoList = list()


def undo():
    if(len(undoList) != 0):
        global undoListInsertable
        undoListInsertable = False
        undoAction = undoList[0]
        #Check to see if there are multiple parameters
        if(isinstance(undoAction[1],tuple)):
            undoAction[0](*undoAction[1])
        #Check to see if there was a bulk action done
        elif(isinstance(undoAction[1],list)):
            for everyBulkAction in undoAction[1]:
                if(isinstance(everyBulkAction[1],tuple)):
                    everyBulkAction[0](*everyBulkAction[1])
                else:
                    everyBulkAction[0](everyBulkAction[1])
        #If none of the above, then it's a single parameter
        else:
            undoAction[0](undoAction[1])
