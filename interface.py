from email import message
from classModelController import *

"""
This function loops through the list of classes and sends them to ListClass()
to print out the classes and their contents. It first does a check to see if 
the list is empty.
"""
def ListClasses():
    if len(listOfClasses) == 0:
        return "There are currently no classes."
    messageString = ''
    for c in listOfClasses:
        messageString += ListClass(c.name)
    return messageString

"""
This function takes user input in order to list all of the contents of the 
given class in a nice way.
"""
def ListClass(name):

    # Use the searchClass function to find a matching name to user input
    wantedClass = ClassSearch(name, listOfClasses)

    messageString = ''

    # Check to see if user input a valid class name
    if (wantedClass == None):
        return "Class " + wantedClass + " does not exist."
    
    messageString += name + "\nFields: \n\t"

    # Loop through listOfAttributes
    for x in wantedClass.listOfFields:
        messageString += x + " \n"


    messageString += name + "\nMethods: \n\t"

    # Loop through listOfAttributes
    for x in wantedClass.listOfMethods:
        messageString += x + " \n"
    
    messageString += "\nRelationships: \n\t" 
    
    # Loop through listOfRelationships
    for y in wantedClass.listOfRelationships:
        messageString += wantedClass.name + " -> " + y + '\n'

    return messageString

"""
This function loops through the list of classes and prints a list of
the relationships each of them has
"""
def ListRelationships():
    if len(listOfClasses) == 0:
        print("There are currently no classes.")    # Inform user if there are no classes
        return
    for c in listOfClasses:
        for r in c.listOfRelationships:
            print("\t" + c.name + " -> " + r)                   # For each class, get each of its relationships and print them
    print()
    return

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

    print("Exiting program. Have a nice day!\n")
    exit()
