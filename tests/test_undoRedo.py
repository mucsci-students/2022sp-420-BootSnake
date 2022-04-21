import pytest

from classModel import *
from attributesModel import *
from parametersModel import *
from sharedItems import *
from relationshipsModel import *
from undoRedoModel import *

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
test_urClassDelete()

# test addField
def test_urAddField():
    ClassAdd("Test")
    addField("Test", "Apple", "int")
    undo()
    assert "Undid!"
    assert len(listOfClasses[0].listOfFields) == 0
