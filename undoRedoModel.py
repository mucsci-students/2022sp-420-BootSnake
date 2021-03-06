from classModel import *
from sharedItems import *
from attributesModel import *
from parametersModel import *
from relationshipsModel import *
import canvas as c
import sys
import io



def undo():
    if(len(undoList) == 0):
        return "\nNothing to undo!"
    else:
        undoListInsertable.bool = False
        #The following two lines will suppress the text from ClassAdd()
        suppress_text = io.StringIO()
        
        sys.stdout = suppress_text 

        undoAction = undoList[0]

        #Add to redo list
        redoList.insert(0, undoAction)

        #Check to see if there was a bulk action done
        if(isinstance(undoAction,list)):
            for everyBulkAction in undoAction:
                if(isinstance(everyBulkAction[1],tuple)):
                    everyBulkAction[0](*everyBulkAction[1])
                else:
                    everyBulkAction[0](everyBulkAction[1])
        #Check to see if there are multiple parameters
        elif(isinstance(undoAction[1],tuple)):  
            undoAction[0](*undoAction[1])
        #If none of the above, then it's a single parameter
        else:
            undoAction[0](undoAction[1])
       
        #This here will release the text so I can continue to use print().
        #Don't want to unsuppress the prints if in gui
        if not guiBool.bool:
            sys.stdout = sys.__stdout__

        undoList.pop(0)
        redoClass.redoable = True
        if guiBool.bool:
            c.refreshCanvas()
        return "Undid!"

        
def redo():
    if (not redoClass.redoable):
        redoList.clear()
        return "\nCannot redo!"
    if(len(redoList) == 0):
        return "\nNothing to redo!"
    else:
        undoListInsertable.bool = True
        redoListInsertable.bool = False
        #The following two lines will suppress the text from ClassAdd()
        redoAction = redoList[0]
    
        if (isinstance(redoAction, list)):
            redoClass.redoCaller = True
            redoAction = getOpposite(redoAction[0][0], redoAction[0][1])
            
        else:
            redoClass.redoCaller = True
            redoAction = getOpposite(redoAction[0], redoAction[1])            
        
        suppress_text = io.StringIO()
        sys.stdout = suppress_text 
        
        #Check to see if there are multiple parameters
        if (isinstance(redoAction[1],tuple)):
            redoAction[0](*redoAction[1])
        #If none of the above, then it's a single parameter
        else:
            redoAction[0](redoAction[1])
        #This here will release the text so I can continue to use print().
        #Don't want to unsuppress the prints if in gui
        if not guiBool.bool:
            sys.stdout = sys.__stdout__
        redoList.pop(0)
        if guiBool.bool:
            c.refreshCanvas()
        return "\nRedid!"

def getOpposite(function, param) -> tuple:
    if (isinstance(param, tuple)):
        if (function == ClassAdd):
            return (ClassDelete, (param[0]))
        elif (function == ClassDelete):
            return (ClassAdd, (param[0], param[1]))
        elif (function == ClassRename):
            return (ClassRename, (param[1], param[0]))
        elif (function == RelationshipAdd):
            return (RelationshipDelete, param)
        elif (function == RelationshipDelete):
            return (RelationshipAdd, param)
        elif (function == relationshipEdit):
            return (relationshipEdit, (param[0], param[1], param[3]))
        elif (function == addField):
            return (delField, (param[0], param[1]))
        elif (function == delField):
            return (addField, param)
        elif (function == renField):
            return (renField, (param[0], param[2], param[1]))
        elif (function == delMethod):
            return (addMethod, param)
        elif (function == addMethod):
            return (delMethod, (param[0], param[1]))
        elif (function == renMethod):
            return (renMethod, (param[0], param[2], param[1]))
        elif (function == ParamAdd):
            return (ParamDelete, (param[0], param[1], "one", param[2]))
        elif (function == ParamDelete):
            return (ParamAdd, (param[0], param[1], param[3], param[4]))
        elif (function == renameParam):
            return (renameParam, (param[0], param[1], param[3], param[2]))
        elif (function == coordEdit):
            return (coordEdit, (param[0], param[3], param[4], param[1], param[2]))
    else:
        if (function == ClassAdd):
            return (ClassDelete, param)
        if (function == ClassDelete):
            return (ClassAdd, param)

