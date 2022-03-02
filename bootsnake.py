"""
Last Edit: 02/09/2022
Edited by: Amelia Spanier and Ben Moran
"""
from classModelController import *
from relationships import *
from UML_attributes import *
from interface import *
from saveLoad import *

"""
Main method in which user will be redirected to the proper
method based upon input
"""
def Main():

    while 1:
        print("Welcome to Bootsnake! Here are your available elements:\n[1] Class\n[2] Attribute")
        print("[3] Relationships\n[4] Save/Load\n[5] Lists\n[6] Help\n[7] Quit")
        userIn = input("\nUML:> ")       # Prompt user for input
        print()

        if "1" in userIn:
            print("Class:")
            print("[1] Add\n[2] Rename\n[3] Delete")
            userIn = input("UML:> ")
            if "1" in userIn:
                name = input("Input class name: ")
                ClassAdd(name)
            elif "2" in userIn:
                name = input("Input class to rename: ")
                newName = input("Input new name: ")
                ClassRename(name, newName)
            elif "3" in userIn: 
                name = input("Input class name: ")
                ClassDelete(name)

        elif "2" in userIn:
            print("Attribute:")
            print("[1] Add\n[2] Rename\n[3] Delete")
            userIn = input("UML:> ")
            if "1" in userIn:
                attr_add()
            elif "2" in userIn:
                attr_ren()
            elif "3" in userIn: 
                attr_del()

        elif "3" in userIn:
            print("Relationship:")
            print("[1] Add\n[2] Delete\n[3] Edit")
            userIn = input("UML:> ")
            src = input("Source class name: ")
            dest= input("Destination class name: ")
            type = ""
            if "1" in userIn:
                RelationshipAdd(src, dest, typeChecker())
            elif "2" in userIn:
                RelationshipDelete(src, dest)
            elif "3" in userIn:
                relationshipEdit(src, dest, typeChecker())

        elif "4" in userIn:
            print("[1] Save\n[2] Load")
            userIn = input("UML:> ")
            filename = input("Enter filename: ")
            if "1" in userIn:
                save(filename)
                continue
            elif "2" in userIn:
                #Load(filename)
                continue

        elif "5" in userIn:
            print("List:")
            print("[1] Class\n[2] Classes\n[3] Relationships")
            userIn = input("UML:> ")
            if "1" in userIn:
                name = input("Class name: ")
                mes = ListClass(name)
                print(mes)
            elif "2" in userIn:
                mes = ListClasses()
                print(mes)
                continue
            elif "3" in userIn: 
                ListRelationships()
                continue 

        elif "6" in userIn:
            Help()
            continue
        
        elif "7" in userIn:
            Exit()

        print()

def typeChecker():
    type = ""
    print("[1] Aggregation\n[2] Composition\n[3] Inheritance\n[4] Realization")
    while (type == ""):
        addInput = input("Relationship type: ")
        if "1" in addInput:
            type = "Aggregation"
        elif "2" in addInput:
            type = "Composition"
        elif "3" in addInput:
            type = "Inheritance"
        elif "4" in addInput:
            type = "Realization"
    return type
Main()