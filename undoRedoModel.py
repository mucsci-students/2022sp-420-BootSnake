
from classModel import *
from sharedItems import *
from attributesModel import *
from parametersModel import *
from relationshipsModel import *
import sys
import io



def undo():
    if(len(undoList) == 0):
        return "\nNothing to undo!"
    else:
        undoListInsertable.bool = False
        #The following two lines will suppress the text from ClassAdd()
        undoAction = undoList[0]
        suppress_text = io.StringIO()
        
        sys.stdout = suppress_text 
        
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
        sys.stdout = sys.__stdout__
        undoList.pop(0)
        return "Undid!"

        
    

