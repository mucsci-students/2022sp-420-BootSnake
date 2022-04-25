"""
---------------------------
Last edited: 03/06/22
Editor: Andy Pham
Summary of edit:

Complete refactoring of the code to fit the new format the functions in 
classModel had. Also created test code for ClassRename and ClassDelete.

Description of program:
A test file used to test all the methods in classModel.
---------------------------
"""

#To test class methods, I have to import them all and the global class list.
from classModel import *

#This will be used to test ClassRename and how it impacts relationships.
from relationshipsModel import *

from sharedItems import *

#The following 2 imports are to silence prints from AClass.
import sys
import io

def test_classAdd_ValidName():
    listOfClasses.clear()
    listOfInputs = ['hi','HI','Hi','Hi1','h2o','Hello_World','Trailing__']
    index = 0
    while(index < len(listOfInputs)):
        #The following two lines will suppress the text from ClassAdd()
        suppress_text = io.StringIO()
        sys.stdout = suppress_text 
        ClassAdd(listOfInputs[index])
        sys.stdout = sys.__stdout__
        result = len(listOfClasses)
        index = index + 1
    assert result == 7
# test_classAdd_ValidName()

def test_classAdd_InvalidName():
    ClassAdd("duplicate")
    listOfInputs = ['duplicate','1NumberFirst','','    Spaces','Hello World','Hello~','Hello`','Hello_World!','@twitter','#Hashtag','HollarHollarGet$','Hundred%','Super^Script','D&D','*_*','I8(','I8)','__Leading','Fire-Emblem','New_Game+','=3','W[','WOh]','NO{','SDF}','SEMI;','COLON:','SINGLEQUOTE\'','DOUBLEQUOTE\"','VER|TICAL','BACKSLASH\\','C,OMMA','LESSER<','PER.IOD','>GREENTEXT','/FORWARDSLASH','QUE?','if','class','else','while','elif','def','for']
    
    index = 0
    while(index < len(listOfInputs)):
        #The following two lines will suppress the text from classAdd()
        suppress_text = io.StringIO()
        sys.stdout = suppress_text
        ClassAdd(listOfInputs[index])
        sys.stdout = sys.__stdout__
        result = len(listOfClasses)
        #We will try the assert, if it fails we go to except.
        assert result == 1
        index = index + 1
# test_classAdd_InvalidName()

def test_classRename_validRename():
    listOfClasses.clear()
    ClassAdd("class1")
    ClassAdd("class2")
    relation = relationship("Aggregation", listOfClasses[0].name, listOfClasses[1].name)
    listOfClasses[1].listOfRelationships.append(relation)
    #The following two lines will suppress the text from classAdd()
    suppress_text = io.StringIO()
    sys.stdout = suppress_text
    ClassRename("class2","RenamedClass2")
    sys.stdout = sys.__stdout__
    result1 = listOfClasses[0].name
    result2 = listOfClasses[1].listOfRelationships[0].dest
    assert result1 == 'RenamedClass2'
    assert result2 == 'RenamedClass2'
    listOfClasses.clear()
# test_classRename_validRename()

def test_classDelete_validDelete():
    listOfClasses.clear()
    ClassAdd("dontDeleteMePlz")
    #The following two lines will suppress the text from classAdd()
    suppress_text = io.StringIO()
    sys.stdout = suppress_text
    ClassDelete("dontDeleteMePlz")
    sys.stdout = sys.__stdout__
    assert len(listOfClasses) == 0
# test_classDelete_validDelete()
#input("Press enter to run tests on ClassAdd...\n")
