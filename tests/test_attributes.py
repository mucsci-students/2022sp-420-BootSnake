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
from sharedItems import *
from relationshipsModel import *


'''
    In order to execute pytest in Python, a virtual environment must be
    created and activated so that any installation packages will be installed
    in the virtual, rather than in the global Python installation. Once the 
    virtual environment is active, type the command the following command
    to install pytest.
            'pip install pytest'  
    
    Do the following steps to run the pytest in the installed virtual env.
    
        1. Activate the virtual environment by typing the command: 
                    source 'virtual_env_name'/bin/activate 
        2. Run pytest by entering the command:    'python -m pytest' 
'''
def reset():
    listOfClasses.clear()
# This file contains tests that also validate the integrations of 
# various modules by calling functions from other files.


def test_addAClass():
    ClassAdd("classFruit")
    assert "classFruit successfully added!"
    #assert "classFruit" in listOfClasses[0]
    assert listOfClasses[0].name =="classFruit"
    

# test add a field to a specific class
def test_addField():
    ClassAdd("classFruit")
    addField("classFruit","apple", "str")
    #assert "classFruit" in listOfClasses[0]
    assert listOfClasses[0].name =="classFruit"
    assert "Field successfully added!"
    assert listOfClasses[0].listOfFields[0].name =="apple"
      
# test add a duplicate field to a specific class
def test_addDupField():
    reset()
    ClassAdd("classFruit")
    addField("classFruit","apple", "str")
    addField("classFruit","apple", "str")
    #assert "classFruit" in listOfClasses[0]
    assert listOfClasses[0].name =="classFruit"
    assert "Field successfully added!"
    assert listOfClasses[0].listOfFields[0].name =="apple"
    assert "apple existed! No duplicates allowed!"
    

# test add a blank field & empty type to a specific class
def test_addBlankField():
    reset()
    ClassAdd("classFruit")
    addField("classFruit"," ", "str")
    #assert "classFruit" in listOfClasses[0]
    assert listOfClasses[0].name =="classFruit"
    assert "name and type cannot be blank!"
    assert listOfClasses[0].listOfFields == []
 

# test add a field to an invalid class
def test_addFieldInvalidClass():
    ClassAdd("classFruit")
    addField("classFoo","apple", "str")
    #assert "classFruit" in listOfClasses[0]
    assert listOfClasses[0].name =="classFruit"
    assert "classFoo not existed! Enter a valid class!"
    assert listOfClasses[0].name == "classFruit"
    assert listOfClasses[0].listOfFields == []


# test rename a field to a specific class
def test_renameField():
    reset()
    ClassAdd("classFruit")
    addField("classFruit","apple", "str")
    
    #assert "classFruit" in listOfClasses[0]
    assert listOfClasses[0].name =="classFruit"
    assert "Field successfully added!"
    assert listOfClasses[0].listOfFields[0].name =="apple"
    renField("classFruit", "apple","kiwi")
    assert  "apple successfully renamed to kiwi!"
    assert listOfClasses[0].listOfFields[0].name =="kiwi"
          

# test rename an invalid field to a specific class
def test_renameInvalidField():
    reset()
    ClassAdd("classFruit")
    addField("classFruit","apple", "str")
    assert "Field successfully added!"
    #assert "classFruit" in listOfClasses[0]
    assert listOfClasses[0].name =="classFruit"
    assert listOfClasses[0].listOfFields[0].name =="apple"
    renField("classFruit", "kiwi","pear")  
    assert  "Field kiwi not found!"
    assert listOfClasses[0].listOfFields[0].name =="apple"
        
# test rename a field to an invalid class
def test_renameFieldInvalidClass():
    reset()
    ClassAdd("classFruit")
    addField("classFruit","apple", "str")
    assert "Field successfully added!"
    #assert "classFruit" in listOfClasses[0]
    assert listOfClasses[0].name =="classFruit"
    assert listOfClasses[0].listOfFields[0].name =="apple"
    renField("classFoo", "kiwi","pear") 
    assert "classFoo not existed! Enter a valid class!"
    assert listOfClasses[0].name == "classFruit"
    assert listOfClasses[0].listOfFields[0].name =="apple"
        
# test delete a field to a specific class
def test_delField():
    reset()
    ClassAdd("classFruit")
    addField("classFruit","apple", "str")
    assert "Field successfully added!"
    #assert "classFruit" in listOfClasses[0]
    assert listOfClasses[0].name =="classFruit"
    assert listOfClasses[0].listOfFields[0].name =="apple"
    delField("classFruit", "apple")
    assert  "Field apple successfully deleted!"
    assert listOfClasses[0].listOfFields == []
        
        
# test delete an invalid field to a specific class
def test_delInvalidField():
    reset()
    ClassAdd("classFruit")
    addField("classFruit","apple", "str")
    assert "Field successfully added!"
    #assert "classFruit" in listOfClasses[0]
    assert listOfClasses[0].name =="classFruit"
    assert listOfClasses[0].listOfFields[0].name =="apple"
    delField("classFruit", "kiwi")
    assert  "Field kiwi not found! Try again!"
    assert listOfClasses[0].listOfFields[0].name =="apple"

# test delete all fields to a specific class
def test_delAllFields():
    reset()
    ClassAdd("classFruit")
    addField("classFruit","apple", "str")
    assert "Field successfully added!"
    #assert "classFruit" in listOfClasses[0]
    assert listOfClasses[0].name =="classFruit"
    assert listOfClasses[0].listOfFields[0].name =="apple"
    addField("classFruit","kiwi", "str")
    assert "Field successfully added!"
    assert listOfClasses[0].listOfFields[1].name =="kiwi"
    delField("classFruit", "all")
    assert  "All Fields successfully deleted!"
    assert listOfClasses[0].listOfFields == []

# test delete a field to an invalid class
def test_delFieldInvalidClass():
    reset()
    ClassAdd("classFruit")
    addField("classFruit","apple", "str")
    assert "Field successfully added!"
    #assert "classFruit" in listOfClasses[0]
    assert listOfClasses[0].name =="classFruit"
    assert listOfClasses[0].listOfFields[0].name =="apple"
    delField("classFood", "all")
    assert "classFoo not existed! Enter a valid class!"
    assert listOfClasses[0].name == "classFruit"
    assert listOfClasses[0].listOfFields[0].name =="apple"


# test add a method to a specific class
def test_addMethod():
    reset()
    ClassAdd("classFood")
    addMethod("classFood","beef", "str", [])
    assert "classFood successfully added!"
    #assert "classFood" in listOfClasses[0]
    assert listOfClasses[0].name =="classFood"
    assert "Beef successfully added!"
    assert listOfClasses[0].listOfMethods[0].name =="Beef"

# test add a duplicate method to a specific class
def test_addDupMethod():
    reset()
    ClassAdd("classFood")
    addMethod("classFood","beef", "str", [])
    assert "Beef successfully added!"
    assert listOfClasses[0].listOfMethods[0].name =="Beef"
    addMethod("classFood","beef", "str", [])
    assert "beef existed! No duplicated allowed!" 
    assert listOfClasses[0].listOfMethods[0].name =="Beef"
        

# test add a blank method to a specific class
def test_addBlankMethod():
    reset()
    ClassAdd("classFood")
    addMethod("classFood"," ", "str",[])
    assert "classFruit successfully added!"
    #assert "classFruit" in listOfClasses[0]
    assert listOfClasses[0].name =="classFood"
    assert "Name and/or type cannot be blank!"
    assert listOfClasses[0].listOfMethods == []
    

# test rename a method to a specific class
def test_reNameMethod():
    reset()
    ClassAdd("classFood")
    addMethod("classFood","Beef", "str",[])
    assert "Beef successfully added!"
    assert listOfClasses[0].listOfMethods[0].name =="Beef"
    renMethod("classFood","beef","Soup" )
    assert "Method beef successfully renamed to Soup!"
    assert listOfClasses[0].listOfMethods[0].name == "Soup"


# test rename an invalid method to a specific class
def test_renameInvalidMethod():
    reset()
    ClassAdd("classFood")
    addMethod("classFood","Beef", "str",[])
    assert "Beef successfully added!"
    assert listOfClasses[0].listOfMethods[0].name =="Beef"
    renMethod("classFood","soup","chicken")
    assert "Method soup not found!"
    assert listOfClasses[0].listOfMethods[0].name == "Beef"
        
        
# test delete a method to a specific class
def test_delMethod():
    reset()
    ClassAdd("classFood")
    addMethod("classFood","Beef", "str",[])
    ParamAdd("classFood", "Beef", "Param1", "int")
    assert "Beef successfully added!"
    assert listOfClasses[0].listOfMethods[0].name =="Beef"
    delMethod("classFood","beef")
    assert "beef of classFood deleted!"
    assert listOfClasses[0].listOfMethods == []
    
# test delete all methods to a specific class
def test_delAllMethods():
    reset()
    ClassAdd("classFood")
    addMethod("classFood","Beef", "str",[])
    ParamAdd("classFood", "Beef", "Param1", "int")
    ParamAdd("classFood", "Beef", "Param2", "int")
    assert "Beef successfully added!"
    assert listOfClasses[0].listOfMethods[0].name =="Beef"
    addMethod("classFood","soup", "str",[])
    ParamAdd("classFood", "soup", "Param1", "int")
    ParamAdd("classFood", "soup", "Param2", "int")
    assert "soup successfully added!"
    assert listOfClasses[0].listOfMethods[1].name =="Soup"
    delMethod("classFood","all")
    assert "All methods of classFood deleted!"
    assert listOfClasses[0].listOfMethods == []
    
        
# test change the Parameter of a given method in a class.
# this test verifies the integration of other module besides
# AClass
def test_delParam():
    reset()
    ClassAdd("classFood")
    addMethod("classFood","Beef", "str",[])
    ParamAdd("classFood","Beef","param", "str")
    ParamAdd("classFood","Beef","param2", "str")
    assert listOfClasses[0].listOfMethods[0].listOfParams[0].name == "param"
    delParam("classFood","Beef","param")
    assert "param of classFood deleted!"
    assert len(listOfClasses[0].listOfMethods) == 1
    
# test rename a parameter of a given method in provided class.
def test_renameParam():
    reset()
    ClassAdd("classFood")
    addMethod("classFood","Beef", "str",[])
    ParamAdd("classFood","Beef","param", "str")
    assert listOfClasses[0].listOfMethods[0].listOfParams[0].name == "param"
    renameParam("classFood","Beef","param", "myparam")
    assert "param successfully renamed to myparam!"
    assert listOfClasses[0].listOfMethods[0].listOfParams[0].name == "myparam"
    
# test rename an invalid parameter of a given method in provided class.
def test_renameInvalidParam():
    reset()
    ClassAdd("classFood")
    addMethod("classFood","Beef", "str",[])
    ParamAdd("classFood","Beef","param", "str")
    assert listOfClasses[0].listOfMethods[0].listOfParams[0].name == "param"
    renameParam("classFood","Beef","param1", "myparam")
    assert "param1 not found! Try again!"
    assert listOfClasses[0].listOfMethods[0].listOfParams[0].name == "param"
   
    
def test_searchMethodFound():
    reset()
    ClassAdd("one")
    addMethod("one", "m1", "int", [])
    ret = searchMethod("one", "m1")
    assert ret.name == "M1"
def test_renameFieldEmpty():
    reset()
    ClassAdd("classFood")
    ret = renField("classFood", "fieldOne", "fieldTwo")
    assert ret == "No fields for class classFood"

def test_renameFieldDuplicate():
    reset()
    ClassAdd("classFood")
    addField("classFood", "fieldOne", "int")
    ret = renField("classFood", "fieldOne", "fieldOne")
    assert ret == "fieldOne existed! No duplicates allowed!"

def test_addFieldNoClass():
    reset()
    ret = addField("classFood", "fieldOne", "int")
    assert ret == "classFood not existed! Enter a valid class!"

def test_renMethodEmpty():
    reset()
    ClassAdd("classFood")
    ret = renMethod("classFood", "methodOne", "methodTwo")
    assert ret == "No methods found for class classFood"

def test_renMethodDuplicate():
    reset()
    ClassAdd("one")
    addMethod("one", "methodOne", "int", [])
    ret = renMethod("one", "methodOne", "methodOne")
    assert ret == 'method methodOne existed! No duplicates allowed!'

def test_renMethodNoClass():
    reset()
    ret = renMethod("classFood", "methodOne", "methodTwo")
    assert ret == "Class classFood not found! Try again!"

# def test_renMethodDuplicate():
#     reset()
#     ClassAdd("classFood")
#     addMethod("classFood", "methodOne", "int", [])
#     ret = renMethod("classFood", "methodOne", "methodOne")
#     assert ret == "methodOne existed! No duplicates allowed!"

def test_checkName():
    reset()
    ret = checkName("one", "!")
    assert ret == False
    ret = checkName("one", "1fieldone")
    assert ret == False
    ret = checkName("one", "____fieldone")
    assert ret == False
    ret = checkName("one", "import")
    assert ret == False
    ret = checkName("one", "field one")
    assert ret == False


def test_checkMethName():
    reset()
    ClassAdd("one")
    clas = listOfClasses[0]
    ret = checkMethName(clas, "m!")
    assert ret == False
    ret = checkMethName(clas, "1m")
    assert ret == False
    ret = checkMethName(clas, "____methodone")
    assert ret == False
    ret = checkMethName(clas, "method one")
    assert ret == False
    ret = checkMethName(clas, "import")
    assert ret == False

def test_checkParamName():
    reset()
    ClassAdd("one")
    addMethod("one", "methodOne", "int", [])
    met = listOfClasses[0].listOfMethods[0]
    ParamAdd("one", "methodOne", "param1", "int")
    ret = checkParamName(met, "")
    assert ret == False
    ret = checkParamName(met, "!")
    assert ret == False
    ret = checkParamName(met, "import")
    assert ret == False
    ret = checkParamName(met, "param one")
    assert ret == False
    ret = checkParamName(met, "param1")
    assert ret == False
    ret = checkParamName(met, "1param")
    assert ret == False

def test_searchMethod():
    reset()
    ret = searchMethod("one", "m1")
    assert ret == None

def test_searchField():
    reset()
    ret = searchField("one", "f1")
    assert ret == None

def test_delFieldNoClass():
    reset()
    ret = delField("one", "fieldOne")
    assert ret == "one not existed! Enter a valid class!"

def test_delFieldNoFields():
    reset()
    ClassAdd("one")
    ret = delField("one", "fieldOne")
    assert ret == "No fields for one"

def test_addMethodNoClass():
    reset()
    ret = addMethod("one", "methodOne", "int", [])
    assert ret == "Class one not existed! Enter a valid class!"

def test_delOneMethod():
    reset()
    ClassAdd("classFood")
    addMethod("classFood","Beef", "str",[])
    addMethod("classFood","Chicken", "str",[])
    assert "Beef successfully added!"
    assert listOfClasses[0].listOfMethods[0].name =="Beef"
    delMethod("classFood","beef")
    assert "beef of classFood deleted!"
    assert listOfClasses[0].listOfMethods[0].name == "Chicken" 

def test_delMethodEmpty():
    reset()
    ClassAdd("one")
    addMethod("one", "methodOne", "int", [])
    ret = delMethod("one", "methodTwo")
    assert ret == "methodTwo not found! Try again!"

def test_delMethodNoClass():
    reset()
    ClassAdd("one")
    ret = delMethod("one", "methodOne")
    assert ret == "No methods for one"

def test_delParamAll():
    reset()
    ClassAdd("one")
    addMethod("one", "m1", "int", [])
    ParamAdd("one", "m1", "p1", "bool")
    ParamAdd("one", "m1", "p2", "int")
    ret = delParam("one", "m1", "all")
    assert ret == "All parameters of one successfully deleted!"


def test_delParamFalseParam():
    reset()
    ClassAdd("one")
    addMethod("one", "m1", "int", [])
    ParamAdd("one", "m1", "p1", "bool")
    ret = delParam("one", "m1", "p2")
    assert ret == "p2 not found!"

def test_delParamNoMethods():
    reset()
    ClassAdd("one")
    ret = delParam("one", "m1", "p1")
    assert ret == "No methods for one!"

def test_delParamFalseMethod():
    reset()
    ClassAdd("one")
    addMethod("one", "m1", "int", [])
    ret = delParam("one", "m2", "p1")
    assert ret == "m2 not found! Try again!"

def test_renameParamDuplicate():
    reset()
    ClassAdd("one")
    addMethod("one", "m1", "int", [])
    ParamAdd("one", "m1", "p1", "bool")
    ret = renameParam("one", "m1", "p1", "p1")
    assert ret == "p1 existed! No duplicates allowed!"

def test_renameParamEmpty():
    reset()
    ClassAdd("one")
    addMethod("one", "m1", "int", [])
    ret = renameParam("one", "m1", "p1", "p2")
    assert ret == "No parameters for m1"

def test_renameParamFalseMethod():
    reset()
    ClassAdd("one")
    addMethod("one", "m1", "int", [])
    ret = renameParam("one", "m2", "p1", "p2")
    assert ret == "m2 not found! Try again!"

def test_renameParamNoMethods():
    reset()
    ClassAdd("one")
    ret = renameParam("one", "m2", "p1", "p2")
    assert ret == "No methods existed for one! Select a valid class"

def test_renameParamFalseClass():
    reset()
    ClassAdd("one")
    ret = renameParam("two", "m2", "p1", "p2")
    assert ret == "two not found! Try again!"

