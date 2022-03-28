"""
Last edited: 03/02/2022
Authors: Ben Moran, Andy Pham and Tram T

Last edit: changed relationships to be an object that has a destination and 
type.
"""

from classModel import *

# relationship object that stores the type of relationship along with 
# destination of the relationship.
class relationship:
    def __init__(self,type,dest):
        self.type = type
        self.dest = dest


"""
This function takes in two strings (class names) and uses the ClassSearch
function to verify they exist. It then checks that the relationship
does not already exist, then appends the 'destination' class
to the 'source' list of relationships.

Returns:
0 - OK
1 - either source or dest class does not exist
2 - relationship already exists
"""
def RelationshipAdd(src: str, dest: str, type: str):
    srcClass = ClassSearch(src, listOfClasses)
    destClass = ClassSearch(dest, listOfClasses)
    if srcClass is not None and destClass is not None:
        for r in srcClass.listOfRelationships:
            if r.dest == destClass.name:
                return "Error: Relationship already exists."
        newRelationship = relationship(type, dest)
        srcClass.listOfRelationships.append(newRelationship)
        return "Successfully added relationship."
    else:
        return "Error: Either the source or destination class does not exist."
"""
This function takes in two strings (class names) and uses the ClassSearch
function to verify they exist. It then checks that the relationship
does already exist, then removes the 'destination' class
from the 'source' list of relationships.

Returns:
0 - OK
1 - Either source or dest class does not exist
2 - relationship does not exist for deletion
"""
def RelationshipDelete(src: str, dest: str):
    srcClass = ClassSearch(src, listOfClasses)
    destClass = ClassSearch(dest, listOfClasses)
    if srcClass is not None and destClass is not None:
        for r in srcClass.listOfRelationships:
            if r.dest == dest:
                srcClass.listOfRelationships.remove(r)
                return "Successfully deleted relationship."
        return "Error: Relationship does not exist for deletion."
    else:
        return "Error: Either the source or destination class does not exist."
    

def relationshipEdit(src: str, dest: str, type: str):
    srcClass = ClassSearch(src, listOfClasses)
    destClass = ClassSearch(dest, listOfClasses)
    if srcClass is not None and destClass is not None:
        for r in srcClass.listOfRelationships:
            if r.dest == dest:
                r.type = type
                return "Successfully edited relationship."
        return "Error: Relationship does not exist for edit."
    else:
        return "Error: Either the source or destination class does not exist."

