"""
Last edited: 02/07/2022
Authors: Ben Moran, Andy Pham and Tram T

Last edit: added functionality in RelationshipAdd() so it checks
if the relationship already exists. Also merged with class for latest updates.
"""

from AClass import *


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
def RelationshipAdd(src: str, dest: str):
    srcClass = ClassSearch(src, listOfClasses)
    destClass = ClassSearch(dest, listOfClasses)
    if srcClass is not None and destClass is not None:
        if not destClass.name in srcClass.listOfRelationships:
            srcClass.listOfRelationships.append(destClass.name)
            return 0
        else:
            return 2
    else:
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
        if destClass.name in srcClass.listOfRelationships:
            srcClass.listOfRelationships.remove(destClass.name)
            return 0
        else:
            return 2
    else:
        return 1
