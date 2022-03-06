# content of test_sample.py
from relationships import *
from classModel import *


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
    ClassAdd("one")
    ClassAdd("two")
    ret = RelationshipAdd("one", "two", "Aggregation")
    assert ret == "Successfully added relationship."
    assert "two" in listOfClasses[0].listOfRelationships[0].dest
    reset()
    
# adding relationship both ways 
def test_AddBothWays():
    ClassAdd("one")
    ClassAdd("two")
    ret = RelationshipAdd("one", "two", "Aggregation")
    assert ret == "Successfully added relationship."
    ret = RelationshipAdd("two", "one", "Realization")
    assert ret == "Successfully added relationship."
    assert "two" in listOfClasses[0].listOfRelationships[0].dest
    assert "one" in listOfClasses[1].listOfRelationships[0].dest
    reset()

# adding relationship on a non existent class
def test_AddFalseClass():
    ClassAdd("one")
    ClassAdd("two")
    ret = RelationshipAdd("four", "two", "Inheritance")
    assert ret == "Error: Either the source or destination class does not exist."
    assert listOfClasses[0].listOfRelationships == []
    reset()


# adding when we only have one class
def test_AddOneClass():
    ClassAdd("one")
    ret = RelationshipAdd("one", "two", "Aggregation")
    assert ret == "Error: Either the source or destination class does not exist."
    assert listOfClasses[0].listOfRelationships == []
    reset()


# adding when we try with a special character
def test_AddSpecialChar():
    ClassAdd("one")
    ret = RelationshipAdd("one", "!", "Inheritance")
    assert ret == "Error: Either the source or destination class does not exist."
    assert listOfClasses[0].listOfRelationships == []
    reset()

################################################################################################################################################################
# DELETIONS


# deleting a relationship
def test_DelOne():
    ClassAdd("one")
    ClassAdd("two")
    ret = RelationshipAdd("one", "two", "Inheritance")
    assert ret == "Successfully added relationship."
    ret = RelationshipDelete("one", "two")
    assert ret == "Successfully deleted relationship."
    assert listOfClasses[0].listOfRelationships == []
    reset()


# delete on a non existent class/relationship
def test_DelNoRel():
    ClassAdd("one")
    ret = RelationshipDelete("one", "two")
    assert ret == "Error: Either the source or destination class does not exist."
    assert listOfClasses[0].listOfRelationships == []
    reset()

# delete on a non existent relationship, but others exist
def test_DelWrongRel():
    ClassAdd("one")
    ClassAdd("two")
    ClassAdd("three")
    ret = RelationshipAdd("one", "three", "Inheritance")
    assert ret == "Successfully added relationship."
    ret = RelationshipDelete("one", "two")
    assert ret == "Error: Relationship does not exist for deletion."
    assert listOfClasses[0].listOfRelationships.dest == 'three'
    reset()