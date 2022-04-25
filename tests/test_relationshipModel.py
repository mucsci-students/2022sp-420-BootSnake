# content of test_sample.py
from sharedItems import *
import relationshipsModel as r
import classModel as c


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
    c.ClassAdd("one")
    c.ClassAdd("two")
    ret = r.RelationshipAdd("one", "two", "Aggregation")
    assert ret == "Relationship added successfully for one & two"
    assert "two" in listOfClasses[1].listOfRelationships[0].dest
    assert "Aggregation" in listOfClasses[1].listOfRelationships[0].type
test_AddOne()

# adding relationship both ways 
def test_AddBothWays():
    reset()
    c.ClassAdd("one")
    c.ClassAdd("two")
    ret = r.RelationshipAdd("one", "two", "Aggregation")
    assert ret == "Relationship added successfully for one & two"
    ret = r.RelationshipAdd("two", "one", "Realization")
    assert ret == "Relationship added successfully for two & one"
    assert "two" in listOfClasses[1].listOfRelationships[0].dest
    assert "Aggregation" in listOfClasses[1].listOfRelationships[0].type
    assert "one" in listOfClasses[0].listOfRelationships[0].dest
    assert "Realization" in listOfClasses[0].listOfRelationships[0].type
# test_AddBothWays()

# adding relationship on a non existent class
def test_AddFalseClass():
    reset()
    c.ClassAdd("one")
    c.ClassAdd("two")
    ret = r.RelationshipAdd("four", "two", "Inheritance")
    print(ret)
    assert ret == "Either the four or two class does not exist."
    assert listOfClasses[0].listOfRelationships == []
# test_AddFalseClass()

# adding when we only have one class
def test_AddOneClass():
    reset()
    c.ClassAdd("one")
    ret = r.RelationshipAdd("one", "two", "Aggregation")
    print(ret)
    assert ret == "Either the one or two class does not exist."
    assert listOfClasses[0].listOfRelationships == []
# test_AddOneClass()

# adding when we try with a special character
def test_AddSpecialChar():
    reset()
    c.ClassAdd("one")
    ret = r.RelationshipAdd("one", "!", "Inheritance")
    assert ret == "Either the one or ! class does not exist."
    assert listOfClasses[0].listOfRelationships == []
# test_AddSpecialChar()

# adding duplicate relationship
def test_addDuplicate():
    reset()
    c.ClassAdd("one")
    c.ClassAdd("two")
    ret = r.RelationshipAdd("one", "two", "Inheritance")
    assert ret == "Relationship added successfully for one & two"
    ret = r.RelationshipAdd("one", "two", "Inheritance")
    assert ret == "Relationship already exists."
# test_addDuplicate()

################################################################################################################################################################
# DELETIONS


# deleting a relationship
def test_DelOne():
    reset()
    c.ClassAdd("one")
    c.ClassAdd("two")
    ret = r.RelationshipAdd("one", "two", "Inheritance")
    assert ret == "Relationship added successfully for one & two"
    assert "Inheritance" in listOfClasses[1].listOfRelationships[0].type
    ret = r.RelationshipDelete("one", "two")
    assert ret == "Successfully deleted relationship."
    assert listOfClasses[1].listOfRelationships == []
# test_DelOne()

# delete on a non existent class/relationship
def test_DelNoRel():
    reset()
    c.ClassAdd("one")
    ret = r.RelationshipDelete("one", "two")
    assert ret == "Either one or two does not exist"
    assert listOfClasses[0].listOfRelationships == []
# test_DelNoRel()

# delete on a non existent relationship, but others exist
def test_DelWrongRel():
    reset()
    c.ClassAdd("one")
    c.ClassAdd("two")
    c.ClassAdd("three")
    ret = r.RelationshipAdd("one", "three", "Inheritance")

    assert ret == "Relationship added successfully for one & three"
    ret = r.RelationshipDelete("one", "two")
    assert ret == "Error: Relationship does not exist for deletion."
    assert listOfClasses[2].listOfRelationships[0].dest == 'three'
    assert "Inheritance" in listOfClasses[2].listOfRelationships[0].type
# test_DelWrongRel()


################################################################################################################################################################
# EDITS


def test_Edit1():
    reset()
    c.ClassAdd("a")
    c.ClassAdd("b")
    for x in listOfClasses:
        print(x.name)
    ret = r.RelationshipAdd('a', 'b', 'Realization')
    assert ret == "Relationship added successfully for a & b"
    assert "Realization" in listOfClasses[1].listOfRelationships[0].type
    ret = r.relationshipEdit('a', 'b', 'Inheritance')
    assert ret == "Successfully edited relationship a & b"
    "Inheritance" in listOfClasses[1].listOfRelationships[0].type
# test_Edit1()
def test_Edit2():
    reset()
    c.ClassAdd("a")
    c.ClassAdd("b")
    ret = r.RelationshipAdd('a', 'b', 'Realization')
    assert ret == "Relationship added successfully for a & b"
    assert "Realization" in listOfClasses[1].listOfRelationships[0].type
    ret = r.relationshipEdit('b', 'a', 'Inheritance')
    assert ret == "Error: Relationship does not exist for edit."
    "Realization" in listOfClasses[1].listOfRelationships[0].type
# test_Edit2()
def test_Edit3():
    reset()
    ret = r.relationshipEdit('a', 'b', 'Realization')
    assert ret == "Error: Either the a or b does not exist."
# test_Edit3()
def test_Edit4():
    reset()
    c.ClassAdd("a")
    c.ClassAdd("b")
    ret = r.relationshipEdit('a', 'b', 'Realization')
    assert ret == "Error: Relationship does not exist for edit."
    assert listOfClasses[1].listOfRelationships == []
# test_Edit4()