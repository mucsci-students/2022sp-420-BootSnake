"""
parameters.py
Authors: Amelia Spanier, Tram Trinh
"""

import re
import keyword
from sqlite3 import paramstyle
from classModel import *
from sharedItems import *
from attributesModel import *

regex = re.compile('[@!$%^&()<>?/\\\|}{\[\]\']')

class Param:
    def __init__(self,name,paramType):
        self.name = name
        self.type = paramType

"""
ParamAdd
Input: name of class containing method, name of method to add to, parameter's name, parameter's type
Description: Creates a parameter with a valid name & type and appends to a given method's parameter list
"""
def ParamAdd(className, methodName, paramName, paramType, delAmnt = 0, wantedMethod = 0):
    if not redoClass.redoCaller and redoClass.redoable:
        redoClass.redoable = False
    redoClass.redoCaller = False

    wantedClass = ClassSearch(className, listOfClasses)        # get requested class from list of classes

    if not wantedClass:
        return "Could not find class with name " + className + ". Please input an existing class."

    wantedMethod = searchMethod(className, methodName)          # get requested method from class's list of methods

    if wantedMethod:
        
        validParam = CheckNameType(paramName, paramType, wantedMethod)      # check that name and type of param are valid

        if validParam:
            thisParam = Param(paramName, paramType)             # new param with Bgiven name & type
            wantedMethod.listOfParams.append(thisParam)         # append new param to method's list of params
            if(undoListInsertable.bool):
                undoList.insert(0,(ParamDelete,(className, methodName,"one",paramName, paramType)))
            print("Parameter " + paramName +" successfully added!")
            print("List of parameters for method " + methodName + ":")
            for o in wantedMethod.listOfParams:
                print(o.name + " : " + o.type)
            return("Parameter " + paramName +" successfully added!")

        else:
            return "Parameter does not fit criteria for validity."

    else:
        return "Could not find method with name " + methodName + ". Please input an existing method."

"""
ParamListAdd
Input: parameter list, parameter's name, parameter's type
Description: Specialized param add for parameter change method use (NOT IN USE)
"""
def ParamListAdd(wantedMethod, paramName, paramType):
    if not redoClass.redoCaller and redoClass.redoable:
        redoClass.redoable = False
    redoClass.redoCaller = False

    validParam = CheckNameType(paramName, paramType, wantedMethod)      # check that name and type of param are valid

    if validParam:
        thisParam = Param(paramName, paramType)                 # new param with given name & type
        wantedMethod.listOfParams.append(thisParam)             # append new param to method's list of params
        print("Parameter " + paramName + " : " + paramType +" successfully added!")
        for o in wantedMethod.listOfParams:
            print(o.name + " : " + paramType)

    else:
        return "Parameter does not fit criteria for validity."

"""
ParamDelete
Input: method expecting param deletion, whether user wants to delete one or all parameters in the list,
parameter's name (empty if ALL delete)
Description: Deletes one or all params from a given method
"""
def ParamDelete(classname: str, methodname: str, delAmnt = 0, paramName = 0, paramType = 0):
    if not redoClass.redoCaller and redoClass.redoable:
        redoClass.redoable = False
        
    redoClass.redoCaller = False
    wantedMethod = searchMethod (methodname)

    if wantedMethod.listOfParams: 
        if delAmnt == 'all':
            if(undoListInsertable.bool):
                oldListOfParams = list(wantedMethod.listOfParams)
                reverseList = list()
                for everyParam in oldListOfParams:
                    reverseList.insert(0,(ParamAdd,(classname,methodname,everyParam.name, everyParam.type, 'all', wantedMethod)))
                undoList.insert(0,reverseList)
            wantedMethod.listOfParams.clear()           # If user wants to delete all params, clear list
            print("All parameters successfully deleted!")
            print(wantedMethod.listOfParams)

        elif delAmnt == 'one':
            for param in wantedMethod.listOfParams:
                if param.name.casefold().strip() == paramName.casefold().strip():
                    if(undoListInsertable.bool):
                        undoList.insert(0,(ParamAdd,(classname,methodname,param.name, param.type, 'one', wantedMethod)))
                    wantedMethod.listOfParams.remove(param)
                    print("UML> Attribute deleted!")
                    for o in wantedMethod.listOfParams:
                        print(o.name + " : " + o.type)
                    break
    else:
        print("No params exist in this method!")
        return "No params exist in this method!"

"""
CheckNameType
Input: given parameter name, given parameter type, method expecting param addition
Description: Checks that both name & type of the new param are valid and that a param with the same
name does not exist within the method. Both name & type must be valid in order for the param to be
added to the method's list of params
"""
def CheckNameType(paramName: str, paramType: str, methodName):
        
    if (not paramName.strip()) or (not paramType.strip()):  
        print("UML:> Name cannot be blank!")
        return False
            
            
    elif (regex.search(paramName.strip()) != None) or (regex.search(paramType.strip()) != None):
        print("UML:> No special characters allowed!")
        return False
            
    elif (paramName[:1].strip().isnumeric()) or (paramType[:1].strip().isnumeric()): 
        print("UML:> Param name and type cannot be preceded by an integer(s)!")
        return False
    
            
    elif (keyword.iskeyword(paramName.strip())) or (keyword.iskeyword(paramType.strip())):      
        print("UML:> Keywords are not allowed!")
        return False

    elif (match.search(paramName.strip()) != None) or (match.search(paramType.strip()) != None):
        print("UML:> No space allowed! Use an underscore!")
        return False
            
    else:
        for o in methodName.listOfParams:
            if o.name.lower().strip() == paramName.lower().strip():
                print("UML:> No duplicates allowed! Parameter(s) must be unique!")
                return False
        return True