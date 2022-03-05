"""
parameters.py
Authors: Amelia Spanier, Tram Trinh
"""

import re
import keyword
from classModel import *
from attributes import *

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
def ParamAdd(className, methodName, paramName, paramType):

    wantedClass = ClassSearch(className, listOfClasses)        # get requested class from list of classes

    if not wantedClass:
        print("Could not find class with name " + className + ". Please input an existing class.")
        return None

    wantedMethod = searchMethod(className, methodName)          # get requested method from class's list of methods

    if wantedMethod:
        
        validParam = CheckNameType(paramName, paramType, wantedMethod)      # check that name and type of param are valid

        if validParam:
            thisParam = Param(paramName, paramType)             # new param with given name & type
            wantedMethod.listOfParams.append(thisParam)         # append new param to method's list of params
            print("Parameter " + paramName +" successfully added!")
            print("List of parameters for method " + methodName + ":")
            for o in wantedMethod.listOfParams:
                print(o.name + " : " + o.type)

        else:
            return None

    else:
        print("Could not find method with name " + methodName + ". Please input an existing method.")
        return None

"""
ParamListAdd
Input: parameter list, parameter's name, parameter's type
Description: Specialized param add for parameter change method use (possible to merge with regular ParamAdd?)
"""
def ParamListAdd(wantedMethod, paramName, paramType):
    validParam = CheckNameType(paramName, paramType, wantedMethod)      # check that name and type of param are valid

    if validParam:
        thisParam = Param(paramName, paramType)                 # new param with given name & type
        wantedMethod.listOfParams.append(thisParam)             # append new param to method's list of params
        print("Parameter " + paramName + " : " + paramType +" successfully added!")
        for o in wantedMethod.listOfParams:
            print(o.name + " : " + paramType)

    else:
        return None

"""
ParamDelete
Input: method expecting param deletion, whether user wants to delete one or all parameters in the list,
parameter's name (empty if ALL delete)
Description: Deletes one or all params from a given method
"""
def ParamDelete(wantedMethod, delAmnt, paramName):
    
    if wantedMethod.listOfParams: 
        if delAmnt == 'all':
            wantedMethod.listOfParams.clear()           # If user wants to delete all params, clear list
            print("All parameters successfully deleted!")
            print(wantedMethod.listOfParams)

        elif delAmnt == 'one':
            for param in wantedMethod.listOfParams:
                if param.name.casefold().strip() == paramName.casefold().strip():
                    wantedMethod.listOfParams.remove(param)
                    print("UML> Attribute deleted!")
                    for o in wantedMethod.listOfParams:
                        print(o.name + " : " + o.type)
                    break
    else:
        print("No params exist in this method!")

"""
CheckNameType
Input: given parameter name, given parameter type, method expecting param addition
Description: Checks that both name & type of the new param are valid and that a param with the same
name does not exist within the method. Both name & type must be valid in order for the param to be
added to the method's list of params
"""
def CheckNameType(paramName: str, paramType: str, methodName):
        
    if (not paramName.strip()) or (not paramType.strip()):  
        print("UML> Name cannot be blank!")
        return False
            
            
    elif (regex.search(paramName.strip()) != None) or (regex.search(paramType.strip()) != None):
        print("UML> No special characters allowed!")
        return False
            
    elif (paramName[:1].strip().isnumeric()) or (paramType[:1].strip().isnumeric()): 
        print("UML> Param name and type cannot be preceded by an integer(s)!")
        return False
    
            
    elif (keyword.iskeyword(paramName.strip())) or (keyword.iskeyword(paramType.strip())):      
        print("UML> Keywords are not allowed!")
        return False

    elif (match.search(paramName.strip()) != None) or (match.search(paramType.strip()) != None):
        print("UML> No space allowed! Use an underscore!")
        return False
            
    else:
        for o in methodName.listOfParams:
            if o.name.lower().strip() == paramName.lower().strip():
                print("UML> No duplicates allowed! Method(s) must be unique!")
                return False
        return True