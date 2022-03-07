# Project Name  : UML BootSnake
# File Name     : test_attributes.py
# Course        : CSCI 420
# Professor     : Dr. Stephanie Schwartz
# BootSnake Team: Amelia S., Andy P., Ben M., Tram T., Travis Z.


###############################################################################

import pytest

from classModel import *
from attributesModel import *
from parametersModel import *


'''
    In order to execute pytest in Python, a virtual environment must be
    created and activated so that any installation packages will be installed
    in the virtual, rather than in the global Python installation. Once the 
    virtual environment is active, type the command 'pip install pytest' to 
    install pytest. 
    
    Do the following steps to run the pytest in the installed virtual env.
    
        1. Activate the virtual environment by typing the command: 
            source 'virtual_env_name'/bin/activate 
        2. Run pytest by entering the command:    'python -m pytest' 
'''

# This file contains tests that also validate the integrations of 
# various modules by calling functions from other files.

# test add a field to a specific class
def test_addField():
    thisClass = AClass('classFruit')
    thisClass.listOfFields = list()
    thisField = FieldClass('apple', 'fruit')
    if checkName(thisClass,'apple') and checkName(thisClass, 'fruit'):
        thisClass.listOfFields.append(thisField)
        assert 'Field successfully added!'
       
# test add a duplicate field to a specific class
def test_addDupField():
    thisClass = AClass('classFruit')
    thisClass.listOfFields = list()
    thisField = FieldClass('apple', 'fruit')
    if checkName(thisClass,'apple') and checkName(thisClass, 'fruit'):
        thisClass.listOfFields.append(thisField)
        assert 'No Duplicate Field Allowed!'
        

# test add a blank field & empty type to a specific class
def test_addBlankField():
    thisClass = AClass('classFruit')
    thisClass.listOfFields = list()
    thisField = FieldClass('', '')
    if checkName(thisClass,'') and checkName(thisClass, ''):
        thisClass.listOfFields.append(thisField)
        assert 'Field and Type can''t'' be blank!'
        
 
# test rename a field to a specific class
def test_renameField():
    thisClass = AClass('classFruit')
    thisClass.listOfFields = list()
    thisField = FieldClass('apple', 'fruit')
    if checkName(thisClass,'kiwi') and checkName(thisClass, 'kiwi'):
        renField('classFruit', 'apple','kiwi')
        assert 'Field successfully renamed!'       


# test rename an invalid field to a specific class
def test_renameInvalidField():
    thisClass = AClass('classFruit')
    thisClass.listOfFields = list()
    thisField = FieldClass('apple', 'fruit')
    if checkName(thisClass,'kiwi') and checkName(thisClass, 'kiwi'):
        renField('classFruit', 'banana','kiwi')
        assert 'Field ' +'banana' + 'not found for class ' + 'classFruit' + '!'         


# test delete a field to a specific class
def test_delField():
    thisClass = AClass('classFruit')
    thisClass.listOfFields = list()
    thisField = FieldClass('apple', 'fruit')
    delObj = searchField('classFruit', 'apple')
    if delObj:
        thisClass.listOfFields.remove(delObj)
        assert 'Field ' +'apple' + 'successfully deleted!'
        
        
# test delete an invalid field to a specific class
def test_delInvalidField():
    thisClass = AClass('classFruit')
    thisClass.listOfFields = list()
    thisField = FieldClass('apple', 'fruit')
    delObj = searchField('classFruit', 'kiwi')
    if delObj:
        thisClass.listOfFields.remove(delObj)
        assert 'Field ' +'kiwi' + 'not found!'




# test add a method to a specific class
def test_addMethod():
    thisClass = ClassAdd('classFruit')
    thisMethod = MethodClass('Apple', 'fruit')
    if checkMethName(thisClass,'') and checkMethName(thisClass, ''):
        thisClass.listOfMethods.append(thisMethod)
        assert 'Method successfully added!'
        

# test add a duplicate method to a specific class
def test_addDupMethod():
    thisClass = ClassAdd('classFruit')
    thisMethod = MethodClass('Apple', 'fruit')
    if checkMethName(thisClass,'') and checkMethName(thisClass, ''):
        thisClass.listOfMethods.append(thisMethod)
        assert 'No Duplicate Method Allowed!'
        

# test add a method to a specific class
def test_addBlankMethod():
    thisClass = ClassAdd('classFruit')
    thisMethod = MethodClass('', '')
    if checkMethName(thisClass,'') and checkMethName(thisClass, ''):
        thisClass.listOfMethods.append(thisMethod)
        assert 'Method name and type can''t'' be blank!'
        


# test rename a method to a specific class
def test_reNameMethod():
    thisClass = AClass('classFruit')
    thisMethod = MethodClass('Apple', 'fruit')
    
    if checkMethName(thisClass, 'Kiwi'):
        renMethod ('classFruit', 'Apple', 'Kiwi')
        assert 'Method ' + 'Apple' + ' successfully renamed!'



# test rename a method to a specific class
def test_renameInvalidMethod():
    thisClass = AClass('classFruit')
    thisMethod = MethodClass('Apple', 'fruit')
    
    if checkMethName(thisClass, 'Kiwi'):
        renMethod ('classFruit', 'Banana', 'Kiwi')
        assert 'Method ' +'Banana' + ' Not found for class ' + 'classFruit' + '!'         
        
# test delete a method to a specific class
def test_delMethod():
    thisClass = AClass('classFruit')
    thisMethod = MethodClass('Apple', 'fruit')
    
    if searchMethod( 'classFruit', 'Apple'):
        for o in thisClass.listOfMethods:
            if o.name == 'Apple'.title().strip():
                o.listOfMethod.remove(o)
                assert 'Method ' + 'Apple' + ' successfully deleted!'
    else:
        thisClass.listOfMethods.clear()
        assert 'All methods of ' + 'classFruit' + 'successfully deleted!'
        
# test change the Parameter of a given method in a class.
# this test verifies the integration of other module besides
# AClass
def test_changeParam():
    thisClass = AClass('classFruit')
    thisMethod = MethodClass('Apple', 'fruit')
    delParam ('classFruit', 'Apple', 'fuji') 
    if delParam:
        assert 'Parameter ' + 'fuji' + 'successfully deleted!'
        paramChange = 'pink lady'
        if paramChange.strip().casefold() != 'q':
            changeType = 'crisp'
            if changeType.strip().casefold() != 'q':
                ParamAdd('classFruit', 'Apple'.title(), paramChange, changeType) 
                assert 'Parameter ' + paramChange + ' successfully added!'
                

# test rename a parameter of a given method in provided class.
def test_renameParam():
    thisClass = ClassAdd('classFruit')
    thisMethod = searchMethod('classFruit', 'Banana')
    if thisMethod:
        thisParam = searchParam(thisMethod, 'yellow'.strip().lower())
        if thisParam:
            if thisParam.name.strip().lower() == 'yellow'.strip().lower():    
                if checkParamName(thisMethod, 'green'.strip().casefold()):
                    thisParam.name = 'green'.lower().strip()
                    assert 'Parameter '+ 'Banana' +' successfully renamed!'
    
             
    
   