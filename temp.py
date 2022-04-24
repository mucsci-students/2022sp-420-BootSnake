import pytest

from classModel import *
from attributesModel import *
from parametersModel import *
from sharedItems import *
from relationshipsModel import *
from undoRedoModel import *
from parametersModel import *

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