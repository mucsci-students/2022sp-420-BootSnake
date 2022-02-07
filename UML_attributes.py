# Project Name: UML BootSnake
# File Name   : UMLattributes.py
# Course      : CSCI 420
# Professor   : Dr. Stephanie Schwartz
# Author      : BootSnake Team (Amelia S., Andy P., Ben M., Tram T., Travis Z.)


###############################################################################

import re # checks if the string contains any special characters
import keyword
#from AClass import *




"""
An attribute is named property of a class that describes the object
being modeled. Generally, the attributes' characteristics depict their
visibility & accessiblity within a given class.

The four types of attribute visibility include Public, Private, Protected
and Package denoted by +, -, #, or ~  signs respectively.

"""


listOfAttributes = list()
# Create a character set and pass it as argument in compile method.
regex = re.compile('[@!$%^&*()<>?/\\\|}{:\[\]\']')


def attr_add():
    '''
    The function attr_add adds an attribute(s) for a selected,
    existing class in the system provided that the attribute
    is unique within the class.
    
    Requirements: 
    Reserved keywords & special characters are not allowed.

    Multiword attributes with spaces and/or capitals will 
    systematically be combined (grouped) & converted to 
    all lowercases. 

    '''
    
    # Set attadd to something other than 'quit'.
    attadd = ''

    # Start a loop that will run until the user enters 'quit'.
    while attadd.strip() != 'quit':
        # Ask the user for an attribute's name.
        attadd = input("UML> Enter an attribute, or enter 'quit': ")
        
        # Add the attribute to a list of attributes.
        
        if attadd.strip() != 'quit':
            if not attadd.strip():  
                print("UML> Name cannot be blank!")
            
            elif len(attadd.strip()) < 2 or len(attadd.strip()) > 16:
                print("UML> Attribute must be 3-15 characters long!")
            
            elif (regex.search(attadd.strip()) != None):
                print("UML> No special characters allowed!")
            
            elif attadd[:1].strip().isnumeric(): 
                print("UML> Attribute cannot be preceded by an integer(s)!")
            
            elif attadd[:3].strip() == "___":     
                print("UML> Leading underscores (> 2) are not allowed!")
            
            elif attadd[-3].strip() == "_":     
                print("UML> Trailing underscores (> 2) are not allowed!")
            
            elif keyword.iskeyword(attadd.strip()):     
                print("UML> Keywords are not allowed!")
            
            # ignore lowercase or uppercase words. 
            elif attadd.casefold().strip().replace(" ", "") in listOfAttributes:
                print("UML> No duplicates allowed! Attribute must be unique.")
            
            else:
                listOfAttributes.append(attadd.strip().lower().replace(" ", ""))
                print("UML> Attribute successfully added!")
    
    listOfAttributes.sort()
    print(listOfAttributes)


def display_list ():
    if not listOfAttributes:
        print("No attributes found!")
    else:
        print(listOfAttributes)

###############################################################################


def attr_del ():
    '''
    The function attr_del removes an attribute(s) for a given class
    provided that the class is existing in the system.

    Options: 
            Delete a selected attribute of a given class one-by-one.
            Delete ALL attributes of a class at once. 

    '''

    if not listOfAttributes:
        print("No attributes found!")
    
    else:
        print(listOfAttributes)
    
    # Set attdel to something other than 'quit'.
    attdel = ''

    # Start a loop that will run until the user enters 'quit'.
    while attdel.strip() != 'quit':
        # Ask the user for an attribute to be deleted.
        attdel = input("UML> Enter the attribute to delete, or enter 'quit': ")
        
        # Remove the attribute(s) from a list of attributes.
        if attdel.strip() != 'quit':
            
            for item in listOfAttributes:
                    if item.casefold() == attdel.casefold().strip():
                        listOfAttributes.remove(attdel.casefold().strip())
                        print("UML> Attribute deleted!")
                        print(listOfAttributes)
                        break
            else: 
                # if user enters ALL or all to remove all attributes.
                if attdel.casefold().strip() == 'all':
                    print("Are you sure you want to delete ALL attributes?")
                    print("Type Y to confirm, N to cancel")
                    attdel = input("UML> Enter Y or N, or enter 'quit':")
                    if attdel.strip() == 'Y':
                        listOfAttributes.clear()
                        print("All attributes successfully deleted!")
                        print(listOfAttributes)
                        break
                    else:
                        print(listOfAttributes)         
                else:
                    print("Attribute not found")
                    print(listOfAttributes)
                    #break

###############################################################################


def attr_ren ():
    '''
    The function attr_ren renames an existing attribute(s) for a given class
    in the system. The newly-created name must be unique within the class.

    '''
    if not listOfAttributes:
        print("No attributes found!")
    
    else:
        print(listOfAttributes)

    # Set attren to something other than 'quit'.
    attren = ''

    # Start a loop that will run until the user enters 'quit'.
    while attren.strip() != 'quit':
        # Ask the user for an attribute to be renamed.
        attren = input("UML> Enter an attribute to rename, or enter 'quit': ")
        
        # Rename the attribute(s) from a list of attributes.
        
        #iterate through the list of attributes to find its index
        for i in range(len(listOfAttributes)):
            if listOfAttributes[i].casefold().strip() == attren.casefold().strip():
                while True:
                    newatt = input("UML> Enter a new name, or enter 'quit':")
                    if not newatt.strip() :  
                        print("UML> Name cannot be blank!")
            
                    elif len(newatt.strip()) < 3 or len(newatt.strip()) > 16:
                        print("UML> Attribute must be 3-15 characters long!")
            
                    elif (regex.search(newatt.strip()) != None):
                        print("UML> No special characters allowed!")
            
                    elif newatt[:1].strip().isnumeric(): 
                        print("UML> Attribute cannot be preceded by an integer(s)!")
            
                    elif newatt[:3].strip() == "___":     
                        print("UML> Leading underscores (> 2) are not allowed!")
            
                    elif newatt[-3].strip() == "_":     
                        print("UML> Trailing underscores (> 2) are not allowed!")
            
                    elif keyword.iskeyword(newatt.strip()):     
                        print("UML> Keywords are not allowed!")
            
                    # ignore lowercase or uppercase words. 
                    elif newatt.casefold().strip().replace(" ", "") in listOfAttributes:
                        print("UML> No duplicates allowed! Attribute must be unique.")
            
                    else:
                        listOfAttributes[i] = newatt.casefold().replace(" ", "")
                        print("UML> Attribute successfully renamed!")
                        print(listOfAttributes)
                        break
                break    
        else:
            print("Attribute not found!")
            listOfAttributes
            


###############################################################################
# Give the user some context.
print("\nWelcome to the BootSnake Geeks camp. What would you like to do?")

# Set an initial value for choice other than the value for 'quit'.
command = ''

# Start a loop that runs until the user enters the value for 'quit'.
while command != 'q':
    
    # Give all the choices in a series of print statements.
    print("\n[1] Enter 1 to input attributes.")
    print("[2] Enter 2 to display a list of all attributes.")
    print("[3] Enter 3 to select an attribute to delete.")
    print("[4] Enter 4 to select an attribute to rename.")
    print("[q] Enter q to quit.")
    
    # Ask for the user's choice.
    command = input("\nUML> What would you like to do? ")

# Respond to the user's choice.
    if command == '1':
        attr_add()
    elif command == '2':
        display_list ()
    elif command == '3':
        attr_del()
    elif command == '4':
        attr_ren()
    elif command == 'q':
        print("\nSee you later.\n")
    else:
        print("\nPlease try again.\n")

