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
    msg: str =""
    srcClass = ClassSearch(src, listOfClasses)
    destClass = ClassSearch(dest, listOfClasses)
    if srcClass is not None and destClass is not None:
        for r in srcClass.listOfRelationships:
            if r.dest == destClass.name:
                msg = f"Relationship already exists."
                print(msg)
                return msg
        newRelationship = relationship(type, dest)
        srcClass.listOfRelationships.append(newRelationship)
        msg = f"Successfully added relationship."
        print(msg)
        return msg 
    else:
        msg = f"Error: Either the source or destination class does not exist."
        print(msg)
        return msg
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
    
    msg: str =""
    
    srcClass = ClassSearch(src, listOfClasses)
    destClass = ClassSearch(dest, listOfClasses)
    if srcClass is not None and destClass is not None:
        for r in srcClass.listOfRelationships:
            if r.dest == dest:
                srcClass.listOfRelationships.remove(r)
                msg = f"Successfully deleted relationship!"
                print(msg)
                return msg
        
        msg = f"Error: Relationship does not exist for deletion."
        print(msg)
        return msg
    
    else:
        msg = f"Error: Either the source or destination class does not exist."
        print(msg)
        return msg
    

def relationshipEdit(src: str, dest: str, type: str):
    
    msg: str =""
    srcClass = ClassSearch(src, listOfClasses)
    destClass = ClassSearch(dest, listOfClasses)
    if srcClass is not None and destClass is not None:
        for r in srcClass.listOfRelationships:
            if r.dest == dest:
                r.type = type
                msg = f"Successfully edited relationship!"
                print(msg)
                return msg
        msg = f"Error: Relationship does not exist for edit."
        print(msg)
        return msg
    else:
        msg = f"Error: Either the source or destination class does not exist."
        print(msg)
        return msg


