"""
Last Edit: 02/09/2022
Edited by: Amelia Spanier and Ben Moran

Edit Summary:
Wrote Main(), started writing Exit(), moved Help() from interface.py
"""
from AClass import *
from relationships import *
from UML_attributes import *
from interface import *

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
                ClassAdd()
            elif "2" in userIn:
                ClassRename()
            elif "3" in userIn: 
                ClassDelete()

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
            print("[1] Add\n[2] Delete")
            userIn = input("UML:> ")
            src = input("Source class name: ")
            dest= input("Destination class name: ")
            if "1" in userIn:
                RelationshipAdd(src, dest)
            elif "2" in userIn:
                RelationshipDelete(src, dest)

        elif "4" in userIn:
            print("[1] Save\n[2] Load")
            userIn = input("UML:> ")
            if "1" in userIn:
                #Save(filename)
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
                ListClass(name)
            elif "2" in userIn:
                ListClasses()
                continue
            elif "3" in userIn: 
                ListRelationships()
                continue 

        elif "6" in userIn:
            Help()
            continue
        
        elif "7" in userIn:
            Exit()

"""
This function exits the program on request from user
"""
def Exit():
    userIn = input("Would you like to save before quitting? ")

    if (userIn == "yes"):
        print("File saved!")

    print("Exiting program. Have a nice day!\n")
    exit()

Main()