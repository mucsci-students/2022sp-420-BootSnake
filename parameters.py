"""
parameters.py
Authors: Amelia Spanier, Tram Trinh
"""

import re
import keyword
# TODO: include file containing method functions

def paramList = list()

class Param:
    def __init__(self,name,paramType):
        self.name = name
        self.type = paramType

def CheckNameType(paramName, paramType, methodName):
    # TODO: write check for paramName validity
    # TODO: write check for paramType validity
    return

"""
ParamAdd
Input: name of class containing method, name of method to add to, parameter's name, parameter's type
Description: Creates a parameter with a valid name & type and appends to a given method's parameter list
"""
def ParamAdd(className, methodName, paramName, paramType):

    wantedClass = className      # TODO: check list of classes to find inout name

    if not wantedClass:
        print("Could not find class with name " + className + ". Please input an existing class.")
        return None

    wantedMethod = methodName    # TODO: check list of methods to find input name

    if wantedMethod:
        
        validParam = CheckNameType(paramName, paramType, methodName)

        if validParam:
            thisParam = Param(paramName, paramType)
            wantedMethod.listofparams.append(thisParam)     # TODO: use correct name of param list to append param

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
def ParamListAdd(paramList, paramName, paramType):
    validParam = CheckNameType(paramName, paramType, methodName)

    if validParam:
        thisParam = Param(paramName, paramType)
        paramList.append(thisParam)

    else:
        return None