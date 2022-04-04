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
    addMethod("classFood","beef", "str")
    assert "classFood successfully added!"
    #assert "classFood" in listOfClasses[0]
    assert listOfClasses[0].name =="classFood"
    assert "Beef successfully added!"
    assert listOfClasses[0].listOfMethods[0].name =="Beef"

# test add a duplicate method to a specific class
def test_addDupMethod():
    reset()
    ClassAdd("classFood")
    addMethod("classFood","beef", "str")
    assert "Beef successfully added!"
    assert listOfClasses[0].listOfMethods[0].name =="Beef"
    addMethod("classFood","beef", "str")
    assert "beef existed! No duplicated allowed!" 
    assert listOfClasses[0].listOfMethods[0].name =="Beef"
        

# test add a blank method to a specific class
def test_addBlankMethod():
    reset()
    ClassAdd("classFood")
    addMethod("classFood"," ", "str")
    assert "classFruit successfully added!"
    #assert "classFruit" in listOfClasses[0]
    assert listOfClasses[0].name =="classFood"
    assert "Name and/or type cannot be blank!"
    assert listOfClasses[0].listOfMethods == []
    

# test rename a method to a specific class
def test_reNameMethod():
    reset()
    ClassAdd("classFood")
    addMethod("classFood","Beef", "str")
    assert "Beef successfully added!"
    assert listOfClasses[0].listOfMethods[0].name =="Beef"
    renMethod("classFood","beef","Soup" )
    assert "Method beef successfully renamed to Soup!"
    assert listOfClasses[0].listOfMethods[0].name == "Soup"


# test rename an invalid method to a specific class
def test_renameInvalidMethod():
    reset()
    ClassAdd("classFood")
    addMethod("classFood","Beef", "str")
    assert "Beef successfully added!"
    assert listOfClasses[0].listOfMethods[0].name =="Beef"
    renMethod("classFood","soup","chicken")
    assert "Method soup not found!"
    assert listOfClasses[0].listOfMethods[0].name == "Beef"
        
        
# test delete a method to a specific class
def test_delMethod():
    reset()
    ClassAdd("classFood")
    addMethod("classFood","Beef", "str")
    assert "Beef successfully added!"
    assert listOfClasses[0].listOfMethods[0].name =="Beef"
    delMethod("classFood","beef")
    assert "beef of classFood deleted!"
    assert listOfClasses[0].listOfMethods == []
    
# test delete all methods to a specific class
def test_delAllMethods():
    reset()
    ClassAdd("classFood")
    addMethod("classFood","Beef", "str")
    assert "Beef successfully added!"
    assert listOfClasses[0].listOfMethods[0].name =="Beef"
    addMethod("classFood","soup", "str")
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
    addMethod("classFood","Beef", "str")
    ParamAdd("classFood","Beef","param", "str")
    assert listOfClasses[0].listOfMethods[0].listOfParams[0].name == "param"
    delParam("classFood","Beef","param")
    assert "param of classFood deleted!"
    assert listOfClasses[0].listOfMethods[0].listOfParams == []
    
# test rename a parameter of a given method in provided class.
def test_renameParam():
    reset()
    ClassAdd("classFood")
    addMethod("classFood","Beef", "str")
    ParamAdd("classFood","Beef","param", "str")
    assert listOfClasses[0].listOfMethods[0].listOfParams[0].name == "param"
    renameParam("classFood","Beef","param", "myparam")
    assert "param successfully renamed to myparam!"
    assert listOfClasses[0].listOfMethods[0].listOfParams[0].name == "myparam"
    
# test rename an invalid parameter of a given method in provided class.
def test_renameInvalidParam():
    reset()
    ClassAdd("classFood")
    addMethod("classFood","Beef", "str")
    ParamAdd("classFood","Beef","param", "str")
    assert listOfClasses[0].listOfMethods[0].listOfParams[0].name == "param"
    renameParam("classFood","Beef","param1", "myparam")
    assert "param1 not found! Try again!"
    assert listOfClasses[0].listOfMethods[0].listOfParams[0].name == "param"
   
    
