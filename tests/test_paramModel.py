"""
paramTest.py
Author: Amelia Spanier
Test file for parameter add & delete methods
"""

from parametersModel import *
from classModel import *
from attributesModel import *
from sharedItems import *

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
reset
Input: none
Description: Clears list of classes to prevent carry-over between tests (to be called after each test)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def reset():
    listOfClasses.clear()


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
PARAMETER ADD
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Test that a param is added properly to a method
# def test_AddOne():
#     reset()
#     ClassAdd("class1")
#     paramlist = list()
#     addMethod("class1", "method1", "str", paramlist)
#     ParamAdd("class1", "method1", "param1", "str")
#     assert listOfClasses[0].listOfMethods[0].listOfParams[0].name == 'param1', "Param name incorrect, should be 'param1'"
#     assert listOfClasses[0].listOfMethods[0].listOfParams[0].type == 'str', "Param type incorrect, should be 'str'"
#     print("Singular parameter addition successful!\n\n")

# Test that ParamAdd() does not add invalid parameters (invalid name OR invalid type)
def test_InvalidNameType():

    reset()
    ClassAdd("class1")
    paramlist = list()
    addMethod("class1", "method1", "str", paramlist)
    ret = ParamAdd("class1", "method1", "@", "str")
    assert not listOfClasses[0].listOfMethods[0].listOfParams, "Invalid parameter added to method, should not happen"
    assert ret == "@ not found!"

    reset()
    ClassAdd("class1")
    paramlist = list()
    addMethod("class1", "method1", "str", paramlist)
    ret = ParamAdd("class1", "method1", "param1", "9")
    assert not listOfClasses[0].listOfMethods[0].listOfParams, "Invalid parameter added to method, should not happen"
    assert ret == "param1 not found!"

    reset()
    ClassAdd("class1")
    paramlist = list()
    addMethod("class1", "method1", "str", paramlist)
    ParamAdd("class1", "method1", "param1", "int")
    ret = ParamAdd("class1", "method1", "param1", "long")
    assert len(listOfClasses[0].listOfMethods[0].listOfParams) == 1, "Invalid parameter added to method, should not happen"
    assert ret == "param1 existed! No duplicates allowed!"

    print("Method does not add parameters when invalid!\n\n")

# Test that method properly exits when class OR method does not exist
def test_ClassMethodDoesNotExist():

    reset()
    ClassAdd("class1")
    paramlist = list()
    addMethod("class1", "method1", "str", paramlist)
    ret = ParamAdd("class2", "method1", "param1", "str")
    assert ret == "class2 not existed! Please input an existing class!"
    assert not listOfClasses[0].listOfMethods[0].listOfParams

    reset()
    ClassAdd("class1")
    paramlist = list()
    addMethod("class1", "method1", "str", paramlist)
    ret = ParamAdd("class1", "method2", "param1", "str")
    assert ret == "Could not find method with name method2. Please input an existing method"
    assert not listOfClasses[0].listOfMethods[0].listOfParams

    print("ParamAdd() exits properly when class or method does not exist!\n\n")


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
PARAMETER DELETE
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Test that a singular param is deleted properly from a method
def test_ParamDeleteOne():
    reset()
    ClassAdd("class1")
    paramlist = list()
    addMethod("class1", "method1", "str", paramlist)
    ParamAdd("class1", "method1", "param1", "str")
    ParamAdd("class1", "method1", "param2", "int")
    wantedMethod = searchMethod("class1", "method1")
    ParamDelete(wantedMethod, "one", "param1")
    assert listOfClasses[0].listOfMethods[0].listOfParams[0].name == 'param2', "Param 'param1' not deleted, list should only contain 'param2'"
    assert len(listOfClasses[0].listOfMethods[0].listOfParams) == 1, "Param list length not correct, should be 1"
    print("Singular parameter deletion successful!\n\n")

# Test that all parameters deleted properly from a method when requested
def test_ParamDeleteAll():
    reset()
    ClassAdd("class1")
    paramlist = list()
    addMethod("class1", "method1", "str", paramlist)
    ParamAdd("class1", "method1", "param1", "str")
    ParamAdd("class1", "method1", "param2", "int")
    wantedMethod = searchMethod("class1", "method1")
    ParamDelete(wantedMethod, "all", "")
    assert not listOfClasses[0].listOfMethods[0].listOfParams, "Param list of method1 contains elements, should be empty"
    print("Full parameter deletion successful!\n\n")

# Test that method properly exits if parameter input does not exist
def test_DeleteNonParam():
    reset()
    ClassAdd("class1")
    paramlist = list()
    addMethod("class1", "method1", "str", paramlist)
    ParamAdd("class1", "method1", "param1", "str")
    wantedMethod = searchMethod("class1", "method1")
    ret = ParamDelete(wantedMethod, "one", "param2")
    assert len(listOfClasses[0].listOfMethods[0].listOfParams) == 1, "Param 'param1' was deleted, should remain in list"
    print("ParamDelete() properly exits if parameter does not exist!\n\n")

# Test that method properly exits if method does not contain parameters
def test_NoParamDelete():
    reset()
    ClassAdd("class1")
    paramlist = list()
    addMethod("class1", "method1", "str", paramlist)
    wantedMethod = searchMethod("class1", "method1")
    ret = ParamDelete(wantedMethod, "one", "param2")
    assert not listOfClasses[0].listOfMethods[0].listOfParams, "No params exist in the method, ParamDelete() should return"
    assert ret == f"No params exist in {wantedMethod}"
    print("ParamDelete() properly exits if method does not contain parameters!\n\n")


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
METHOD CALLS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# test_AddOne()
# test_InvalidNameType()
# test_ClassMethodDoesNotExist()
# test_ParamDeleteOne()
# test_ParamDeleteAll()
# test_DeleteNonParam()
# test_NoParamDelete()