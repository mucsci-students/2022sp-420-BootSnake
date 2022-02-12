# Project Name  : UML BootSnake
# File Name     : UMLattributes.py
# Course        : CSCI 420
# Professor     : Dr. Stephanie Schwartz
# BootSnake Team: Amelia S., Andy P., Ben M., Tram T., Travis Z.


###############################################################################

import re # checks if the string contains any special characters
import keyword
from AClass import *


"""
An attribute is named property of a class that describes the object
being modeled. Generally, the attributes' characteristics depict their
visibility & accessiblity within a given class.

The four types of attribute visibility include Public, Private, Protected
and Package denoted by +, _, #, or ~  signs respectively.

"""


listOfAttributes = list()

# Create a character set to check for special characters
regex = re.compile('[@!$%^&*()<>?/\\\|}{:\[\]\']')
# Create a set of blank spaces to check for spaces between words
match = re.compile('[ ]+')


def check_name(name, wantedClass):
    '''
    
    The function check_name verifies the validity of an attribute's name
    input by user by checking whether it is blank, non-alphanumeric, 
    reserved keyword, or preceded by an special character(s), an integer(s),
    or non-existing within a class prior to adding the identifier 
    in the system. 
    
    It prompts user if multi-word attribute name with spaces entered.

    '''
    
    if not name.strip():  
        print("UML> Name cannot be blank!")
            
    elif len(name.strip()) < 2 or len(name.strip()) > 16:
        print("UML> Attribute must be 3-15 characters long!")
            
    elif (regex.search(name.strip()) != None):
        print("UML> No special characters allowed!")
            
    elif name[:1].strip().isnumeric(): 
        print("UML> Attribute cannot be preceded by an integer(s)!")
            
    elif name[:3].strip() == "___":     
        print("UML> Leading underscores (> 2) are not allowed!")
            
    #elif name[-3].strip() == "_":     
    #    print("UML> Trailing underscores (> 2) are not allowed!")
            
    elif keyword.iskeyword(name.strip()):     
        print("UML> Keywords are not allowed!")

    elif match.search(name.strip()) != None:
        print("UML> No space allowed! Use an underscore!")
            
    # ignore lowercase or uppercase words entered by user. 
    elif name.casefold().strip() in wantedClass.listOfAttributes:
        print("UML> No duplicates allowed! Attribute must be unique.")
            
    else:
        return True



def attr_add():
    '''
    The function attr_add adds an attribute(s) for a selected, existing class
    in the system provided that the attribute is unique within the class.
    
    This function allows user to continue adding attributes untill user
    presses 'quit'.

    Given the class is not existed, it prompts user for a valid class name. 
    
    Notes: 
        1. 'Uppercase' words will systematically convert to converted to 
            'lowercase' words.
        2. Case-insensitive when searching for attribute(s).

    '''
    

    # prompt user for a specific class to which attribute(s) will be added.
    classname = input('To which class do you want to add attribute(s)?')

    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname,listOfClasses)
    
    if wantedClass:
    
        # Set attadd to something other than 'quit'.
        attname = ''

        # Start a loop that will run until the user enters 'quit'.
        while attname != 'quit':
            # Ask the user for an attribute's name.
            attname = input("UML> Enter an attribute, or enter 'quit': ")
        
            # Add the attribute to a list of attributes if it is valid and
            # continue untill user quits.
            if attname.strip() != 'quit':
                if(check_name(attname, wantedClass)):
                    wantedClass.listOfAttributes.append(attname.lower().strip())
                    print("UML> Attribute successfully added!")
    
        wantedClass.listOfAttributes.sort()
        print(wantedClass.listOfAttributes)

    else: 
        print('Class not found! Please try again!')


###############################################################################


def attr_del ():
    '''
    The function attr_del deletes an attribute(s) for a given class provided
    that the class & the attribute must exist in the system. It provides user 
    with the following choices:
        
        1. Deleting a selected attribute(s) one-by-one.
        2. Delete ALL attributes of a class at once.
        3. Opt out. 
    
    When either the selected class or attribute(s) is not existed, it prompts
    user for a valid name.

    '''


    # prompt user for a specific class to which attribute(s) will be deleted.
    classname =input('To which class do you want to delete attribute(s)?')

    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)

    if wantedClass:
        # display a list of attributes to user 
        print("\nBelow the list of attributes for your selected class")
        print(wantedClass.listOfAttributes)    
        # Set attdel to something other than 'quit'.
        attdel = ''
        if wantedClass.listOfAttributes:
            # Start a loop that will run until the user enters 'quit'.
            while attdel.strip() != 'quit':
                # Ask the user for an attribute or ALL attributes be deleted.
                attdel = input("UML> Enter an attribute or 'All' to delete, or enter 'quit': ")
        
                # Remove the attribute(s) from a list of attributes when found.
                if attdel.strip() != 'quit':
                    for item in wantedClass.listOfAttributes:
                        if item.casefold() == attdel.casefold().strip():
                            wantedClass.listOfAttributes.remove(attdel.casefold().strip())
                            print("UML> Attribute deleted!")
                            print(wantedClass.listOfAttributes)
                            break
                    else: 
                        # If user enters ALL/all to remove all attributes.
                        if attdel.casefold().strip() == 'all':
                            print("Are you sure you want to delete ALL attributes?")
                            print("Type Y to confirm, N to cancel")
                            attdel = input("UML> Enter Y or N, or enter 'quit':")
                        
                            if attdel.strip() == 'Y':
                                wantedClass.listOfAttributes.clear()
                                print("All attributes successfully deleted!")
                                print(wantedClass.listOfAttributes)
                                break
                            else:
                                print(wantedClass.listOfAttributes)         
                        else:
                            print("Attribute not found! Please try again!")
                            print(wantedClass.listOfAttributes)
                            #break

        else: 
            print("No attributes existed for deletion!")                    
    else:
        print('Class Not found! Please try again!')

###############################################################################


def attr_ren ():
    '''
    The function attr_ren renames an existing attribute(s) for a given existing
    class in the system. The newly-created name must be unique within the class. 
    It calls check_name method to verify the validity of the renamed attribute
    prior to updating the attribute name for the class.

    User can continue renaming the selected attributes or stop at any time by
    pressing 'quit'

    When either the selected class or attribute(s) is not existed, it prompts
    user for a valid name.

    '''


    # prompt user for a specific class to which attribute(s) will be renamed.
    classname =input('To which class do you want to rename attribute(s)?')

    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname,listOfClasses)

    if wantedClass:
        
        # display a list of attributes to user 
        print("\nBelow the list of attributes for your selected class")
        print(wantedClass.listOfAttributes)
        # Set attren to something other than 'quit'.
        attren = ''

        if wantedClass.listOfAttributes:
            # Start a loop that will run until the user enters 'quit'.
            while attren.strip() != 'quit':
                # Ask the user for an attribute to be renamed.
                attren = input("UML> Enter an attribute to rename, or enter 'quit': ")
        
                # Rename the attribute(s) from a list of attributes by iterating
                # through the list of attributes to find its index
                for i in range(len(wantedClass.listOfAttributes)):
                    if wantedClass.listOfAttributes[i].casefold().strip() == attren.casefold().strip():
                        while True:
                            newatt = input("UML> Enter a new name, or enter 'quit':")
                            if (check_name(newatt, wantedClass)):
                                wantedClass.listOfAttributes[i] = newatt.casefold()
                                print('UML> Attribute successfully renamed!')
                                print(wantedClass.listOfAttributes)
                                break
                        break    
            
                else:
                    print('Attribute not found!')
                    wantedClass.listOfAttributes

        else: 
            print("No attributes existed to rename!") 

    
    else:
        print('Class not found! please try again!')
       

###############################################################################
# # Give the user some context.
# print("\nWelcome to the BootSnake Geeks camp. What would you like to do?")

# # Set an initial value for choice other than the value for 'quit'.
# command = ''

# # Start a loop that runs until the user enters the value for 'quit'.
# while command != 'q':
    
#     # Give all the choices in a series of print statements.
#     print("\n[1] Enter 1 to input attributes.")
#     print("[2] Enter 2 to display a list of all attributes.")
#     print("[3] Enter 3 to select an attribute to delete.")
#     print("[4] Enter 4 to select an attribute to rename.")
#     print("[q] Enter q to quit.")
    
#     # Ask for the user's choice.
#     command = input('\nUML> What would you like to do? ')

# # Respond to the user's choice.
#     if command == '1':
#         attr_add()
#     elif command == '2':
#         has_attr ()
#     elif command == '3':
#         attr_del()
#     elif command == '4':
#         attr_ren()
#     elif command == 'q':
#         print('\nSee you later.\n')
#     else:
#         print('\nPlease try again.\n')





