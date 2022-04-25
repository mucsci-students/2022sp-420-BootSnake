"""
Last edited: 03/02/2022
Authors: Ben Moran, Andy Pham and Tram T

Last edit: changed relationships to be an object that has a destination and 
type.
"""

from classModel import *
from sharedItems import *

# relationship object that stores the type of relationship along with 
# destination of the relationship.
class relationship:
    def __init__(self,type,src,dest):
        self.type = type
        self.dest = dest
        self.src = src


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
    msg =""
    res = None
    srcClass = ClassSearch(src, listOfClasses)
    destClass = ClassSearch(dest, listOfClasses)
    if srcClass is not None and destClass is not None:
        for r in srcClass.listOfRelationships:
            if r.dest == destClass.name:
                print("Error: Relationship already exists.")
                msg = f"Relationship already exists."
                return msg
        
        newRelationship = relationship(type,src, dest)
        res = srcClass.listOfRelationships.append(newRelationship)
        print("Successfully added relationship.")
        msg =f"Relationship added successfully for {src} & {dest}"

        if (undoListInsertable.bool):
            undoList.insert(0, (RelationshipDelete, (src, dest, type)))
        return msg
    
    else:
        print("Error: Either the source or destination class does not exist.")
        msg = f"Either the {src} or {dest} class does not exist."
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
def RelationshipDelete(src: str, dest: str, type = 0):
    
    msg =""
    res = None
    
    srcClass = ClassSearch(src, listOfClasses)
    destClass = ClassSearch(dest, listOfClasses)
    if srcClass is not None and destClass is not None:
        for r in srcClass.listOfRelationships:
            if r.dest == dest:
                if (undoListInsertable.bool):
                    undoList.insert(0, (RelationshipAdd, (src, dest, r.type)))
                res = srcClass.listOfRelationships.remove(r)
                print("Successfully deleted relationship.")
                msg = "Successfully deleted relationship."
                return msg
        
        print("Error: Relationship does not exist for deletion.")
        msg = "Error: Relationship does not exist for deletion."
        return msg
    else:
        print("Error: Either the source or destination class does not exist.")
        msg = f"Either {src} or {dest} does not exist"
        return msg
    

def relationshipEdit(src: str, dest: str, type: str, new = 0):
    
    msg=""
    res = None

    srcClass = ClassSearch(src, listOfClasses)
    destClass = ClassSearch(dest, listOfClasses)
    if srcClass is not None and destClass is not None:
        for r in srcClass.listOfRelationships:
            if r.dest == dest:
                if (undoListInsertable.bool):
                    undoList.insert(0, (relationshipEdit, (src, dest, r.type, type)))
                res = r.type = type
                print("Successfully edited relationship.")
                msg = f"Successfully edited relationship {src} & {dest}"

                return msg
        
        print("Error: Relationship does not exist for edit.")
        msg = f"Error: Relationship does not exist for edit."
        return msg
    else:
        print("Error: Either the source or destination class does not exist.")
        msg = f"Error: Either the {src} or {dest} does not exist."
        return msg
