# content of test_sample.py
from relationships import *
from AClass import *


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
    RelationshipAdd("one", "two")
    assert "two" in listOfClasses[0].listOfRelationships[0]
    reset()
    
# adding relationship both ways 
def test_AddBothWays():
    addClasses("one")
    addClasses("two")
    RelationshipAdd("one", "two")
    RelationshipAdd("two", "one")
    assert "two" in listOfClasses[0].listOfRelationships[0]
    assert "one" in listOfClasses[1].listOfRelationships[0]
    reset()

# adding relationship on a non existent class
def test_AddFalseClass():
    addClasses("one")
    addClasses("two")
    RelationshipAdd("four", "two")
    assert listOfClasses[0].listOfRelationships == []
    reset()


# adding when we only have one class
def test_AddOneClass():
    addClasses("one")
    RelationshipAdd("one", "two")
    assert listOfClasses[0].listOfRelationships == []
    reset()


# adding when we try with a special character
def test_AddSpecialChar():
    addClasses("one")
    RelationshipAdd("one", "!")
    assert listOfClasses[0].listOfRelationships == []
    reset()

################################################################################################################################################################
# DELETIONS


# deleting a relationship
def test_DelOne():
    addClasses("one")
    addClasses("two")
    RelationshipAdd("one", "two")
    RelationshipDelete("one", "two")
    assert listOfClasses[0].listOfRelationships == []
    reset()


# delete on a non existent relationship
def test_DelNoRel():
    addClasses("one")
    RelationshipDelete("one", "two")
    assert listOfClasses[0].listOfRelationships == []
    reset()

# delete on a non existent relationship, but others exist
def test_DelWrongRel():
    addClasses("one")
    addClasses("two")
    addClasses("three")
    RelationshipAdd("one", "three")
    RelationshipDelete("one", "two")
    assert listOfClasses[0].listOfRelationships == ['three']
    reset()