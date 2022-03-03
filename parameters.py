"""
parameters.py
Authors: Amelia Spanier, Tram Trinh
"""

import re
import keyword
from AClass import *
from attributes import *

regex = re.compile('[@!$%^&()<>?/\\\|}{\[\]\']')

class Param:
    def __init__(self,name,paramType):
        self.name = name
        self.type = paramType

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

"""
ParamAdd
Input: name of class containing method, name of method to add to, parameter's name, parameter's type
Description: Creates a parameter with a valid name & type and appends to a given method's parameter list
"""
def ParamAdd(className, methodName, paramName, paramType):

    wantedClass = ClassSearch(className)

    if not wantedClass:
        print("Could not find class with name " + className + ". Please input an existing class.")
        return None

    wantedMethod = searchMethod(className, methodName)

    if wantedMethod:
        
        validParam = CheckNameType(paramName, paramType, wantedMethod)

        if validParam:
            thisParam = Param(paramName, paramType)
            wantedMethod.listOfParams.append(thisParam)
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
Description: Adds a parameter to a disconnected parameter list for specific use in adding multiple parameters in
parameter change
"""
def ParamListAdd(wantedMethod, paramName, paramType):
    validParam = CheckNameType(paramName, paramType, wantedMethod)

    if validParam:
        thisParam = Param(paramName, paramType)
        wantedMethod.listOfParams.append(thisParam)
        print("Parameter " + paramName + " : " + paramType +" successfully added!")
        for o in wantedMethod.listOfParams:
            print(o.name + " : " + paramType)

    else:
        return None