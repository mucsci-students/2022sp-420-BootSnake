# content of test_sample.py
from relationships import *
from classModelController import *


################################################################################################################################################################
# HELPER FUNCTIONS

# adding to classes directly instead of going through prompts
def addClasses(name):
    myClass = AClass(name)
    listOfClasses.append(myClass)

# reset list of classes so tests dont interfere with each other
def reset():
    listOfClasses.clear()



################################################################################################################################################################
# ADDITIONS


# test basic addition of one class to another
def test_AddOne():
    addClasses("one")
    addClasses("two")
    ret = RelationshipAdd("one", "two")
    assert ret == 0
    assert "two" in listOfClasses[0].listOfRelationships[0]
    reset()
    
# adding relationship both ways 
def test_AddBothWays():
    addClasses("one")
    addClasses("two")
    ret = RelationshipAdd("one", "two")
    assert ret == 0
    ret = RelationshipAdd("two", "one")
    assert ret == 0
    assert "two" in listOfClasses[0].listOfRelationships[0]
    assert "one" in listOfClasses[1].listOfRelationships[0]
    reset()

# adding relationship on a non existent class
def test_AddFalseClass():
    addClasses("one")
    addClasses("two")
    ret = RelationshipAdd("four", "two")
    assert ret == 1
    assert listOfClasses[0].listOfRelationships == []
    reset()


# adding when we only have one class
def test_AddOneClass():
    addClasses("one")
    ret = RelationshipAdd("one", "two")
    assert ret == 1
    assert listOfClasses[0].listOfRelationships == []
    reset()


# adding when we try with a special character
def test_AddSpecialChar():
    addClasses("one")
    ret = RelationshipAdd("one", "!")
    assert ret == 1
    assert listOfClasses[0].listOfRelationships == []
    reset()

################################################################################################################################################################
# DELETIONS


# deleting a relationship
def test_DelOne():
    addClasses("one")
    addClasses("two")
    ret = RelationshipAdd("one", "two")
    assert ret == 0
    ret = RelationshipDelete("one", "two")
    assert ret == 0
    assert listOfClasses[0].listOfRelationships == []
    reset()


# delete on a non existent class/relationship
def test_DelNoRel():
    addClasses("one")
    ret = RelationshipDelete("one", "two")
    assert ret == 1
    assert listOfClasses[0].listOfRelationships == []
    reset()

# delete on a non existent relationship, but others exist
def test_DelWrongRel():
    addClasses("one")
    addClasses("two")
    addClasses("three")
    ret = RelationshipAdd("one", "three")
    assert ret == 0
    ret = RelationshipDelete("one", "two")
    assert ret == 2
    assert listOfClasses[0].listOfRelationships == ['three']
    reset()