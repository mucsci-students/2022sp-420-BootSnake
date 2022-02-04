from asyncio.windows_events import NULL
from AClass import *


# def RelationshipAdd(src: AClass, dest: AClass):
#     src.listOfRelationships.append(dest.name)

def RelationshipAdd(src: str, dest: str):
    srcClass = ClassSearch(src)
    destClass = ClassSearch(dest)
    if srcClass is not None and destClass is not None:
        srcClass.listOfRelationships.append(destClass.name)
    
"""
"""
def RelationshipDelete(src: str, dest: str):
    return
