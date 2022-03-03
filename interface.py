from email import message
from classModel import *

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
        return "Class " + name + " does not exist."
    
    messageString += name + "\nFields: \n"

    # Loop through listOfAttributes

    for x in wantedClass.listOfFields:
        messageString += "\t" + x + " \n"


    messageString += "\nMethods: \n\t"

    # Loop through listOfAttributes
    for x in wantedClass.listOfMethods:
        messageString += x.name + " \n"
    
    messageString += "\nRelationships: \n\t" 
    
    # Loop through listOfRelationships
    for y in wantedClass.listOfRelationships:
        messageString += wantedClass.name + " ---"+"("+y.type+")"+"---> " + y.dest + '\n'

    return messageString

"""
This function loops through the list of classes and prints a list of
the relationships each of them has
"""
def ListRelationships():
    message = ''
    if len(listOfClasses) == 0:
        message += "There are currently no classes."    # Inform user if there are no classes
        return message
    for c in listOfClasses:
        for r in c.listOfRelationships:
            message += "\t" + c.name + " ---"+ "("+r.type+")"+ "---> " + r.dest + '\n'               # For each class, get each of its relationships and print them
    return message

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
