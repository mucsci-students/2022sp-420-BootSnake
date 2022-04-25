# content of test_sample.py
from relationshipsModel import *
from classModel import *
from sharedItems import *

################################################################################################################################################################
# HELPER FUNCTIONS

# adding to classes directly instead of going through prompts

# reset list of classes so tests dont interfere with each other
def reset():
    listOfClasses.clear()



################################################################################################################################################################
# ADDITIONS


# test basic addition of one class to another
def test_AddOne():
    reset()
    ClassAdd("one")
    ClassAdd("two")
    ret = RelationshipAdd("one", "two", "Aggregation")
    assert ret == "Relationship added successfully for one & two"
    assert "two" in listOfClasses[1].listOfRelationships[0].dest
    assert "Aggregation" in listOfClasses[1].listOfRelationships[0].type
    
# adding relationship both ways 
def test_AddBothWays():
    reset()
    ClassAdd("one")
    ClassAdd("two")
    ret = RelationshipAdd("one", "two", "Aggregation")
    assert ret == "Relationship added successfully for one & two"
    ret = RelationshipAdd("two", "one", "Realization")
    assert ret == "Relationship added successfully for two & one"
    assert "two" in listOfClasses[1].listOfRelationships[0].dest
    assert "Aggregation" in listOfClasses[1].listOfRelationships[0].type
    assert "one" in listOfClasses[0].listOfRelationships[0].dest
    assert "Realization" in listOfClasses[0].listOfRelationships[0].type

# adding relationship on a non existent class
def test_AddFalseClass():
    reset()
    ClassAdd("one")
    ClassAdd("two")
    ret = RelationshipAdd("four", "two", "Inheritance")
    assert ret == "Either the four or two class does not exist."
    assert listOfClasses[1].listOfRelationships == []


# adding when we only have one class
def test_AddOneClass():
    reset()
    ClassAdd("one")
    ret = RelationshipAdd("one", "two", "Aggregation")
    assert ret == "Either the one or two class does not exist."
    assert listOfClasses[0].listOfRelationships == []


# adding when we try with a special character
def test_AddSpecialChar():
    reset()
    ClassAdd("one")
    ret = RelationshipAdd("one", "!", "Inheritance")
    assert ret == "Either the one or ! class does not exist."
    assert listOfClasses[0].listOfRelationships == []


# adding duplicate relationship
def test_addDuplicate():
    reset()
    ClassAdd("one")
    ClassAdd("two")
    ret = RelationshipAdd("one", "two", "Inheritance")
    assert ret == "Relationship added successfully for one & two"
    ret = RelationshipAdd("one", "two", "Inheritance")
    assert ret == "Relationship already exists."

################################################################################################################################################################
# DELETIONS


# deleting a relationship
def test_DelOne():
    reset()
    ClassAdd("one")
    ClassAdd("two")
    ret = RelationshipAdd("one", "two", "Inheritance")
    assert ret == "Relationship added successfully for one & two"
    assert "Inheritance" in listOfClasses[1].listOfRelationships[0].type
    ret = RelationshipDelete("one", "two")
    assert ret == "Successfully deleted one & two"
    assert listOfClasses[1].listOfRelationships == []


# delete on a non existent class/relationship
def test_DelNoRel():
    reset()
    ClassAdd("one")
    ret = RelationshipDelete("one", "two")
    assert ret == "Either one or two does not exist"
    assert listOfClasses[0].listOfRelationships == []

# delete on a non existent relationship, but others exist
def test_DelWrongRel():
    reset()
    ClassAdd("one")
    ClassAdd("two")
    ClassAdd("three")
    ret = RelationshipAdd("one", "three", "Inheritance")
    assert ret == "Relationship added successfully for one & three"
    ret = RelationshipDelete("one", "two")
    assert ret == "Relationship does not exist for deletion!"
    assert listOfClasses[2].listOfRelationships[0].dest == 'three'
    assert "Inheritance" in listOfClasses[2].listOfRelationships[0].type



################################################################################################################################################################
# EDITS


def test_Edit1():
    reset()
    ClassAdd("a")
    ClassAdd("b")
    ret = RelationshipAdd('a', 'b', 'Realization')
    assert ret == "Relationship added successfully for a & b"
    assert "Realization" in listOfClasses[1].listOfRelationships[0].type
    ret = relationshipEdit('a', 'b', 'Inheritance')
    assert ret == "Successfully edited relationship a & b"
    assert "Inheritance" in listOfClasses[1].listOfRelationships[0].type

def test_Edit2():
    reset()
    ClassAdd("a")
    ClassAdd("b")
    ret = RelationshipAdd('a', 'b', 'Realization')
    assert ret == "Relationship added successfully for a & b"
    assert "Realization" in listOfClasses[1].listOfRelationships[0].type
    ret = relationshipEdit('b', 'a', 'Inheritance')
    assert ret == "Relationship does not exist for edit."
    assert "Realization" in listOfClasses[1].listOfRelationships[0].type

def test_Edit3():
    reset()
    ret = relationshipEdit('a', 'b', 'Realization')
    assert ret == "Either the a or b does not exist"

def test_Edit4():
    reset()
    ClassAdd("a")
    ClassAdd("b")
    ret = relationshipEdit('a', 'b', 'Realization')
    assert ret == "Relationship does not exist for edit."
    assert listOfClasses[0].listOfRelationships == []