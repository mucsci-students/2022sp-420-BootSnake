"""
parameters.py
Authors: Amelia Spanier, Tram Trinh
"""

import re
import keyword
from classModel import *
from attributesModel import *
from sharedItems import *

regex = re.compile('[@!$%^&()<>?/\\\|}{\[\]\']')
# Create a set of blank spaces to check for spaces between words
match = re.compile('[ ]+')

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
    msg: str =""
    
    wantedClass = ClassSearch(className, listOfClasses)        # get requested class from list of classes

    if not wantedClass:
        print("Could not find class with name " + className + ". Please input an existing class.")
        msg = f"{className} not existed! Please input an existing class!"
        return msg

    wantedMethod = searchMethod(className, methodName)          # get requested method from class's list of methods

    if wantedMethod:
        
        if not searchParam(wantedMethod, paramName.casefold()):
            validParam = CheckNameType(paramName, paramType, wantedMethod)      # check that name and type of param are valid

            if validParam:
                thisParam = Param(paramName, paramType)             # new param with given name & type
                wantedMethod.listOfParams.append(thisParam)         # append new param to method's list of params
                print("Parameter " + paramName +" successfully added!")
                msg = f"{paramName} successfully added!"
                print("List of parameters for method " + methodName + ":")
                for o in wantedMethod.listOfParams:
                    print(o.name + " : " + o.type)

                return msg

            else:
                print(paramName + " not found!")
                msg = f"{paramName} not found!"
                return msg
        else:
            print("paramName existed! No duplicates allowed!")
            msg = f"{paramName} existed! No duplicates allowed!"
            return msg

    else:
        print("Could not find method with name " + methodName + ". Please input an existing method.")
        msg = f"Could not find method with name {methodName}. Please input an existing method"
        return msg

"""
ParamDelete
Input: method expecting param deletion, whether user wants to delete one or all parameters in the list,
parameter's name (empty if ALL delete)
Description: Deletes one or all params from a given method
"""
def ParamDelete(wantedMethod, delAmnt, paramName):
    
    msg: str = ""
    if wantedMethod.listOfParams: 
        if delAmnt == 'all':
            wantedMethod.listOfParams.clear()           # If user wants to delete all params, clear list
            print("All parameters successfully deleted!")
            msg = f"All parameter successfully deleted!"
            print(wantedMethod.listOfParams)

        elif delAmnt == 'one':
            for param in wantedMethod.listOfParams:
                if param.name.casefold().strip() == paramName.casefold().strip():
                    wantedMethod.listOfParams.remove(param)
                    print("UML> " + paramName + " deleted!")
                    msg = f"{paramName} deleted!"
                    
                    for o in wantedMethod.listOfParams:
                        print(o.name + " : " + o.type)
                break

            msg = f"{paramName} does not exist in {wantedMethod.name}"

    else:
        print("No params exist in this method!")
        msg = f"No params exist in {wantedMethod.name}"
    
    return msg
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
        print("UML:> No space allowed! Use an underscore!")
        return False
            
    else:
        for o in methodName.listOfParams:
            if o.name.lower().strip() == paramName.lower().strip():
                print("UML> No duplicates allowed! Method(s) must be unique!")
                return False
        return True
    
    
    
##############################################################################################  
def ParamDelete(wantedMethod, delAmnt, paramName):
    
    msg: str = ""
    if wantedMethod.listOfParams: 
        if delAmnt == 'all':
            wantedMethod.listOfParams.clear()           # If user wants to delete all params, clear list
            print("All parameters successfully deleted!")
            msg = f"All parameter successfully deleted!"
            print(wantedMethod.listOfParams)

            return msg

        elif delAmnt == 'one':
            for param in wantedMethod.listOfParams:
                if param.name.casefold().strip() == paramName.casefold().strip():
                    wantedMethod.listOfParams.remove(param)
                    print("UML> " + paramName + " deleted!")
                    msg = f"{paramName} deleted!"
                    
                    for o in wantedMethod.listOfParams:
                        print(o.name + " : " + o.type)
                    break

                    return msg
            msg = f" does not exist in {wantedMethod.name}"
    else:

        print("No params exist in this method!")
        msg = f"No params exist in {wantedMethod.name}"
        return msg
    
def searchMethod(classname: str, methname: str) :
    # loop through the list of methods of a given class to search for a 
    # existing method in the system.
    wantedClass = ClassSearch(classname, listOfClasses)
    
    if wantedClass:
        for mObj in wantedClass.listOfMethods:
            if (mObj.name.title() == methname.title().strip()):
                return mObj
    
    else: 
        return None
#########################################################################################    
# search for a parameter    
def searchParam( methObj: object, param: str):
    
    for x in methObj.listOfParams:
        if x.name.strip().casefold() == param.casefold().strip():
            return x
    return None
