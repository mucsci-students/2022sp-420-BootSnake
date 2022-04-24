import pytest

from classModel import *
from attributesModel import *
from parametersModel import *
from sharedItems import *
from relationshipsModel import *
from undoRedoModel import *
from parametersModel import *


def reset():
    listOfClasses().clear()

# test undo on no commands
def test_undoNothing():
    undo()
    assert "Nothing to undo!"

# test redo on no commands
def test_redoNothing():
    redo()
    assert "Nothing to redo!"

# test undo redo class add
def test_urClassAdd():
    ClassAdd("Test")
    undo()
    assert "Undid!"
    assert len(listOfClasses) == 0
    redo()
    assert "Redid!"
    assert listOfClasses[0].name == "Test"
# test_urClassAdd()

# test class rename
def test_urClassRename():
    ClassAdd("Test")
    ClassRename("Test", "Orange")
    undo()
    assert "Undid!"
    assert listOfClasses[0].name == "Test"
    redo()
    assert "Redid!"
    assert listOfClasses[0].name == "Orange"
# test_urClassRename()

# test class delete
def test_urClassDelete():
    ClassAdd("Test")
    ClassDelete("Test")
    undo()
    assert "Undid!"
    assert listOfClasses[0].name == "Test"
    redo()
    assert "Redid!"
    assert len(listOfClasses) == 0
# test_urClassDelete()

# test class delete with full class
def test_urClassFullDelete():
    ClassAdd("Test")
    ClassAdd("Quiz")
    addField("Test", "Orange", "string")
    addMethod("Test", "Fruit", "void")
    ParamAdd("Test", "Fruit", "grape", "float")
    RelationshipAdd("Test", "Quiz", "Aggregation")
    ClassDelete("Test")
    undo()
    assert "Undid!"
    assert listOfClasses[1].name == "Test"
    assert listOfClasses[1].listOfFields[0].name == "Orange"
    assert listOfClasses[1].listOfMethods[0].name == "Fruit"
    assert listOfClasses[1].listOfMethods[0].listOfParams[0].name == "grape"
    assert listOfClasses[1].listOfRelationships[0].type == "Aggregation"
    redo()
    assert "Redid!"
    assert len(listOfClasses) == 1
# test_urClassFullDelete()

# test addField
def test_urAddField():
    ClassAdd("Test")
    addField("Test", "Apple", "int")
    undo()
    assert "Undid!"
    assert len(listOfClasses[0].listOfFields) == 0
    redo()
    assert "Redid!"
    assert listOfClasses[0].listOfFields[0].name == "Apple"
# test_urAddField()

# test rename field
def test_urRenField():
    ClassAdd("Test")
    addField("Test", "Apple", "int")
    renField("Test", "Apple", "Orange")
    undo()
    assert "Undid!"
    assert listOfClasses[0].listOfFields[0].name == "Apple"
    redo()
    assert "Redid!"
    assert listOfClasses[0].listOfFields[0].name == "Orange"
# test_urRenField()

# test delete field
def test_urDelField():
    ClassAdd("Test")
    addField("Test", "Apple", "int")
    delField("Test", "Apple")
    undo()
    assert "Undid!"
    assert listOfClasses[0].listOfFields[0].name == "Apple"
    redo()
    assert "Redid!"
    assert len(listOfClasses[0].listOfFields) == 0
# test_urDelField()

# test add method
def test_urAddMethod():
    ClassAdd("Test")
    addMethod("Test", "Fruit", "void")
    undo()
    assert "Undid!"
    assert len(listOfClasses[0].listOfMethods) == 0
    redo()
    assert "Redid!"
    assert listOfClasses[0].listOfMethods[0].name == "Fruit"
# test_urAddMethod()

# test rename method
def test_urRenMethod():
    ClassAdd("Test")
    addMethod("Test", "Fruit", "void")
    renMethod("Test", "Fruit", "Vegetables")
    undo()
    assert "Undid!"
    assert listOfClasses[0].listOfMethods[0].name == "Fruit"
    redo()
    assert "Redid!"
    assert listOfClasses[0].listOfMethods[0].name == "Vegetables"
# test_urRenMethod()

# test delete method
def test_urDelMethod():
    ClassAdd("Test")
    addMethod("Test", "Fruit", "void")
    delMethod("Test", "Fruit")
    undo()
    assert "Undid!"
    assert listOfClasses[0].listOfMethods[0].name == "Fruit"
    redo()
    assert "Redid!"
    assert len(listOfClasses[0].listOfMethods) == 0
# test_urDelMethod()

# test delete method with parameters
def test_urDelMethodWParam():
    ClassAdd("Test")
    addMethod("Test", "Fruit", "void")
    ParamAdd("Test", "Fruit", "Orange", "int")
    delMethod("Test", "Fruit")
    undo()
    assert "Undid!"
    assert listOfClasses[0].listOfMethods[0].name == "Fruit"
    assert listOfClasses[0].listOfMethods[0].listOfParams[0].name == "Orange"
    redo()
    assert "Redid!"
    assert len(listOfClasses[0].listOfMethods) == 0
# test_urDelMethodWParam()

# test parameter add
def test_urParamAdd():
    ClassAdd("Test")
    addMethod("Test", "Fruit", "void")
    ParamAdd("Test", "Fruit", "Orange", "int")
    undo()
    assert "Undid!"
    assert listOfClasses[0].listOfMethods[0].name == "Fruit"
    assert len(listOfClasses[0].listOfMethods[0].listOfParams) == 0
    redo()
    assert "Redid!"
    assert listOfClasses[0].listOfMethods[0].listOfParams[0].name == "Orange"
test_urParamAdd()

# test parameter rename
def test_urRenParam():  
    ClassAdd("Test")
    addMethod("Test", "Fruit", "void")
    ParamAdd("Test", "Fruit", "Orange", "int")
    renameParam("Test", "Fruit", "Orange", "Grape")
    undo()
    assert "Undid!"
    assert listOfClasses[0].listOfMethods[0].name == "Fruit"
    assert listOfClasses[0].listOfMethods[0].listOfParams[0].name == "Orange"
    redo()
    assert "Redid!"
    assert listOfClasses[0].listOfMethods[0].listOfParams[0].name == "Grape"
# test_urRenParam()

# test parameter delete
def test_urDelParam():
    ClassAdd("Test")
    addMethod("Test", "Fruit", "void")
    ParamAdd("Test", "Fruit", "Orange", "int")
    wantedMethod = searchMethod("Test", "Fruit")
    ParamDelete("Test", "Fruit", wantedMethod, "one", "Orange")
    undo()
    assert "Undid!"
    assert listOfClasses[0].listOfMethods[0].name == "Fruit"
    assert listOfClasses[0].listOfMethods[0].listOfParams[0].name == "Orange"
    redo()
    assert "Redid!"
    assert len(listOfClasses[0].listOfMethods[0].listOfParams) == 0
# test_urDelParam()

# test relationship add
def test_urRelAdd():
    ClassAdd("Test")
    ClassAdd("Quiz")
    RelationshipAdd("Test", "Quiz", "Aggregation")
    undo()
    assert "Undid!"
    assert len(listOfClasses[1].listOfRelationships) == 0
    redo()
    assert "Redid!"
    assert listOfClasses[1].listOfRelationships[0].type == "Aggregation"
# test_urRelAdd()

# test relationship edit
def test_urRelEdit():
    ClassAdd("Test")
    ClassAdd("Quiz")
    RelationshipAdd("Test", "Quiz", "Aggregation")
    relationshipEdit("Test", "Quiz", "Composition")
    undo()
    assert "Undid!"
    assert listOfClasses[1].listOfRelationships[0].type == "Aggregation"
    redo()
    assert "Redid!"
    assert listOfClasses[1].listOfRelationships[0].type == "Composition"
# test_urRelEdit()

# test relationship delete
def test_urRelDelete():
    ClassAdd("Test")
    ClassAdd("Quiz")
    RelationshipAdd("Test", "Quiz", "Aggregation")
    RelationshipDelete("Test", "Quiz")
    undo()
    assert "Undid!"
    assert listOfClasses[1].listOfRelationships[0].type == "Aggregation"
    redo()
    assert "Redid!"
    assert len(listOfClasses[1].listOfRelationships) == 0
test_urRelDelete()