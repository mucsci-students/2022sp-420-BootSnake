"""
Last edited: 02/07/2022
Authors: Ben Moran, Andy Pham and Tram T

Last edit: added functionality in RelationshipAdd() so it checks
if the relationship already exists. Also merged with class for latest updates.
"""

from AClass import *


class RelClass:
    def __init__(self, src: str, dest: str, type: str):
        self.source = src
        self.destination = dest
        self.type = type


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
def RelationshipAdd(src: str, dest: str, reltype: str):
    srcClass = ClassSearch(src, listOfClasses)
    destClass = ClassSearch(dest, listOfClasses)
    
    if srcClass  and destClass :
              
        if not destClass.name in srcClass.listOfRelationships:
            if srcClass != destClass:
                if (checkRelType(reltype)):
                    # create a new relationship object and adds it to the relationship list
                    relObj = RelClass(src, dest, reltype.strip().lower())
                    srcClass.listOfRelationships.append(relObj)
                    
                    print(srcClass.listOfRelationships)
                    print("Relationships added successfully for classes " + src + " & "+ dest)
                    return 0
                elif not reltype.strip().lower():
                    print("Relationship can't be blank! Select a valid type!")
                    return 5
                else:
                    print("Relationship type " + reltype + " not valid!")
                    return 6
            else:
                print("source and destination can't be the same!")
                return 3
        
        else: 
            print("Relationship existed!")
            return 2  
         
    
    elif srcClass is None  and destClass is None :
            print ("Source and Destination can't be blank!")
            return 4
    else:
        print("Both source & destination must in list of classes!")
        return 1
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
        if srcClass != destClass:
            
            if destClass.name in srcClass.listOfRelationships:
            
            
           
                srcClass.listOfRelationships.remove(destClass.name)
                print("Relationships deleted successfully for classes" + src + " & "+ dest)
                return 0
            else:
                print(destClass.name)
                print(srcClass.name)
                print("Relationship not existed!")
                
                return 3
        else:
            print("source and destination can't be the same!")
            return 2
    
    elif srcClass is None and destClass is None:
        
        print ("Source and Destination can't be blank!")
        return 4
    else:
        print("Both source & destination must in list of classes!")
        return 1
   
    
    
###################################################################################

# Helper function
def checkRelType(reltype: str) -> bool:
    relationshipTypes = {"aggregation", "composition", "inheritance", "realization"}
    
    if reltype.lower().strip() in relationshipTypes:
        return True
    else:
        return False
    

    
    
    
        
