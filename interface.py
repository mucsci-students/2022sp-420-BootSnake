from AClass import *

"""
This function loops through the list of classes and sends them to ListClass()
to print out the classes and their contents. It first does a check to see if 
the list is empty.
"""
def ListClasses():
    if len(listOfClasses) is 0:
        print("There are currently no classes.")
        return
    for c in listOfClasses:
        ListClass(c)
    return

def ListClass():
    return

def Help():
    return

def Exit():
    return