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

"""
This function takes user input in order to list all of the contents of the 
given class in a nice way.
"""
def ListClass(name):

    # Use the searchClass function to find a matching name to user input
    wantedClass = ClassSearch(name)

    # Check to see if user input a valid class name
    if (wantedClass == None):
        print ("Class " + " does not exist.")
        return
    
    print (name + "\nAttributes: \n\t")

    # Loop through listOfAttributes
    for x in wantedClass.listOfAttributes:
        print (x + " ")
    
    print ("\nRelationships: \n\t")
    
    # Loop through listOfRelationships
    for y in wantedClass.listOfRelationships:
        print (y + " ")

    print ("\n")
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

def Exit():
    return
