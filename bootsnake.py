"""
Last Edit: 02/07/2022
Edited by: Amelia Spanier

Edit Summary:
Wrote Main(), started writing Exit(), moved Help() from interface.py
"""

#from AClass import *

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
            print("[1] Add")
            print("[2] Rename")
            print("[3] Delete")
            userIn = input("UML:> ")  

        elif "2" in userIn:
            print("Attribute:")
            print("[1] Add")
            print("[2] Rename")
            print("[3] Delete")
            userIn = input("UML:> ")  

        elif "3" in userIn:
            print("Relationship:")
            print("[1] Add")
            print("[2] Delete")
            userIn = input("UML:> ")
            src = input("Source class name: ")
            dest= input("Destination class name: ")
            if "1" in userIn:
                #RelationshipAdd(src, dest)
                return
            elif "2" in userIn:
                #RelationshipDelete(src, dest)
                return

        elif "4" in userIn:
            print("[1] Save")
            print("[2] Load")
            userIn = input("UML:> ")  

        elif "5" in userIn:
            print("List:")
            print("[1] Class")
            print("[2] Classes")
            print("[3] Relationships")
            userIn = input("UML:> ")  

        elif "6" in userIn:
            Help()

        elif "7" in userIn:
            Exit()

"""
This function reads a text file of helpful instructions for the user and
prints it
"""
def Help():
    helpfile = open('help.txt', 'r')                        # Open text file as read-only
    print(helpfile.read())                                  # Read file & print to terminal
    helpfile.close()
    return

"""
This function exits the program on request from user
"""
def Exit():
    userIn = input("Would you like to save before quitting? ")

    if "yes" in userIn:
        print("File saved!")

    print("Exiting program. Have a nice day!\n")
    exit()

Main()