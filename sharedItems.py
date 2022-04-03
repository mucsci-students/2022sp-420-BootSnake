#A global list that will be used to keep all the classes.
listOfClasses = list()
undoList = list()
redoList = list()
class undoListBool:
     def __init__(self,bool):
        self.bool = bool 
undoListInsertable = undoListBool(True)

class redoListBool:
    def __init__(self,bool):
        self.bool = bool
redoListInsertable = redoListBool(True)

#Searches through class list and return given name.    
def ClassSearch(name, classList):
    #We can use this for loop as a means to check every entry in the list for 
    #the name.
    for x in classList:
        if(x.name == name):
            return x #We then return the object for the other functions to use.
    
    #If we get to this point then that means we couldn't find the class so 
    #we'll return None.
    return None

