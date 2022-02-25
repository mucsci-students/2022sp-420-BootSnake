# Project Name  : UML_BootSnake
# File Name     : attributes.py
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


listOfFields = list()
listOfMethods = list()
listOfParams = list()

# Create a character set to check for special characters
regex = re.compile('[@!$%^&*()<>?/\\\|}{:\[\]\']')
# Create a set of blank spaces to check for spaces between words
match = re.compile('[ ]+')

class MethodClass:
    def __init__(self,name):
        self.name = name
        self.listOfParams = list()
       
    
        
    
    
    
def addField(classname : str, fieldname :str):
    '''
    The add_field adds a field(s) for a selected, existing class
    in the system provided that the field is unique within the class.
    
    This function allows user to continue adding fields untill user
    presses 'quit'.

    Given the class is not existed, it prompts user for a valid class name. 
    
    Notes: 
        1. 'Uppercase' words will systematically convert to converted to 
            'lowercase' words.
        2. Case-insensitive when searching for field(s).

    '''
    

    #call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)
    
    if wantedClass:
        
        # Add the attribute to a list of attributes if it is valid
        #  and continue untill user quits.
            
        if(checkName(wantedClass, fieldname)):
            wantedClass.listOfFields.append(fieldname.lower().strip())
            print("UML> Field " + fieldname + " successfully added!")
    
    wantedClass.listOfFields.sort()
    print(wantedClass.listOfFields)
   

###############################################################################


def delField (classname: str, fieldname:str):
    '''
    The del_field deletes a field(s) for a given class provided
    that the class & the field must exist in the system. It provides user 
    with the following choices:
        
        1. Deleting a selected field(s) one-by-one.
        2. Delete ALL fields of a class at once.
        3. Opt out. 
    
    When either the selected class or field(s) is not existed, it prompts
    user for a valid name.

    '''


    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)

    if wantedClass:
        # display a list of fields to user 
        while True:
            if wantedClass.listOfFields:
                while True:
                # Remove the field(s) from a list of fields when found.
                    
                    print(wantedClass.listOfFields)
                    for item in wantedClass.listOfFields:
                        if item.casefold() == fieldname.casefold().strip():
                            wantedClass.listOfFields.remove(fieldname.casefold().strip())
                            print("UML> Field '" + fieldname +"' deleted!")
                            print(wantedClass.listOfFields)
                            break
                            
                        # If user enters ALL/all to remove all fields.
                        elif fieldname.casefold().strip() == 'all':
                            wantedClass.listOfFields.clear()
                            print("All Fields successfully deleted! Enter 'q' to exit!")
                            print(wantedClass.listOfFields)
                            break
                             
                    else:
                        print("Field " + fieldname + " not found! Try again!")
                        print(wantedClass.listOfFields)
                        break
                    break
                    
                
                break 
                
            else: 
                print("No fields for class " + classname  + "! Enter 'q' to exit!")
                break
                   
    else:
        print("Class " + classname + " not existed! Enter a valid class!")
        
      

###############################################################################


def renField (classname: str, fieldname: str, newname: str):
    '''
    The ren_field renames an existing field(s) for a given existing
    class in the system. The newly-created name must be unique within the class. 
    It calls check_name method to verify the validity of the renamed field
    prior to updating the field name for the class.

    User can continue renaming the selected field or stop at any time by
    pressing 'quit'

    When either the selected class or field(s) is not existed, it prompts
    user for a valid name.

    '''

    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)
    if wantedClass:
        while True:
            if wantedClass.listOfFields:
                while True:
                    # Rename the field(s) from a list of fields by iterating
                    # through the list to find its index
                    for i in range(len(wantedClass.listOfFields)):
                        if wantedClass.listOfFields[i].casefold().strip() == fieldname.casefold().strip():
                            while True:

                                if (checkName(wantedClass, newname)):
                                    wantedClass.listOfFields[i] = newname.casefold().strip()
                                    print("UML> Field " +fieldname + " successfully renamed!")
                                    print(wantedClass.listOfFields)
                                    break   
                                
                                else:
                                    break 
                                    
                            break   
                        
                    else:
                        print("Fields " + fieldname + "not found!")
                        wantedClass.listOfFields
                        break
                    break
                    
                break
            
            else: 
                print("No fields for class " + classname + "!. Enter 'q' to exit")
                break
      
###############################################################################

def addMethod(classname: str, methodname: str, paramlist: list =[]):
    
    '''
    The addMethod adds a method(s) for a selected, existing class
    in the system provided that the method has unique identifiers within 
    the class.
    
    This function allows user to continue adding methods untill user
    presses 'quit'.

    Given the class is not existed, it prompts user for a valid class name. 
    
    Notes: 
        1. 'Uppercase' words will systematically convert to converted to 
            'properrcase' words.
        2. Case-insensitive when searching for method(s).

    '''
    
    
    
    # search for the class in the system
    wantedClass = ClassSearch(classname, listOfClasses)
    if wantedClass:
        while True:
            if len(methodname.strip().casefold())> 0 and match.search(methodname.strip().casefold()) == None:
            
                if searchMethod(wantedClass, methodname.strip().casefold()):
                    while True:
                        if paramlist:
                            while True:
                                
                                wantedClass.listOfMethods.append(methodname.strip().title())
                                
                                listOfParams.append(paramlist)
                                wantedClass.listOfMethods.sort()
                                #listOfParameters.sort()
                                print(wantedClass.listOfMethods)
                                print(listOfParams)
                                
                                break
                            break
                        else:
                            print("Parameter(s) can be added later!")
                            wantedClass.listOfMethods.append(methodname.strip().title())
                            wantedClass.listOfMethods.sort()
                            print(wantedClass.listOfMethods)
                            #print(newMethodObj.listOfParams)
                            
                            break
                    break
                else:
                    print("Method existed! No duplicates allowed!")
                    break
                
                    
            else:
                print("Method name can't be blank! and/or No space allowed " +
                      "'Use an underscore!'. Enter a valid method name!")
                break
        
    else:
        print("Class " + classname + " not existed! Enter a valid class!")
    

###############################################################################

def renMethod (classname: str, methodname: str, newmethod: str):
    '''
    The renMethod renames an existing method(s) for a given existing
    class in the system. The newly-created name must be unique within the class. 
    It calls searchName method to verify the validity of the renamed method
    prior to updating the method name for the class.

    User can continue renaming the selected method or stop at any time by
    pressing 'quit'

    When either the selected class or method(s) is not existed, it prompts
    user for a valid name.

    '''
    

    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)
    if wantedClass:
        while True:
            if wantedClass.listOfMethods:
                while True:
                    # Rename the method(s) from a list of methods by iterating
                    # through the list to find its index
                    for i in range(len(wantedClass.listOfMethods)):
                        if wantedClass.listOfMethods[i].casefold().strip() == methodname.casefold().strip():
                            while True:

                                if len(methodname.strip().title())> 0 and match.search(methodname.strip().title()) == None:
                                    if searchMethod(wantedClass, newmethod.strip().casefold()):
                                        wantedClass.listOfMethods[i] = newmethod.title().strip()
                                        print("UML> Method " + methodname + " successfully renamed!")
                                        print(wantedClass.listOfMethods)
                                        break 
                                    else:
                                        print("Method " + methodname + " existed! No duplicates allowed!")
                                        break  
                                
                                else:
                                    break 
                                    
                            break   
                        
                    else:
                        print("Method " + methodname + " not found!")
                        wantedClass.listOfMethods
                        break
                    break
                    
                break
            
            else: 
                print("No Methods  found for class " + classname  + " !. Enter 'q' to exit!")
                break
      
###############################################################################              

def delMethod (classname: str, methodname:str):
    '''
    The delMethod deletes a method(s) for a given class provided
    that the class & the method must exist in the system. It provides 
    user with the following choices:
        
        1. Deleting a selected method(s) one-by-one.
        2. Delete ALL methods of a class at once.
        3. Opt out. 
    
    When either the selected class or method(s) is not existed, it prompts
    user for a valid name.

    '''

    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)

    if wantedClass:
        # display a list of methods to user 
        while True:
            if wantedClass.listOfMethods:
                while True:
                
                    for item in wantedClass.listOfMethods:
                        if item.casefold() == methodname.casefold().strip():
                            wantedClass.listOfMethods.remove(methodname.casefold().strip())
                            print("UML> Method " + methodname + " of class" + classname + " deleted!")
                            print(wantedClass.listOfMethods)
                            break
                         
                        # If user enters ALL/all to remove all fields.
                        elif methodname.casefold().strip() == 'all':
                            wantedClass.listOfMethods.clear()
                            print("All methods of " + classname +" successfully" 
                                  + " deleted!. Enter 'q' to exit!")
                            print(wantedClass.listOfMethods)
                            break
                             
                    else:
                        print("Method " + methodname + " not found! Try again!")
                        print(wantedClass.listOfMethods)
                        break
                    break
                break
            else: 
                print("No methods for class " + classname  + "!. Enter 'q' to exit!")
                break
           
###############################################################################

def addParam(classname: str, methodname:str, parname: str ):
    
    """
    add a parameter to a provided method of a given class
    
    """
    
    wantedClass = ClassSearch(classname, listOfClasses)
    if wantedClass:
        while True:
            wantedMethod = searchMethod(classname, methodname)
            if not wantedMethod:
                while True:
                    param = searchParam(methodname, parname)
                    if not param:
                        listOfMethods.append(parname)
                        break
                    
                    
        



###############################################################################
# Helper functions

def checkName(wantedClass: str, name: str):
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
            
    #elif len(name.strip()) < 2 or len(name.strip()) > 16:
    #    print("UML> Attribute must be 3-15 characters long!")
            
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
    elif name.casefold().strip() in wantedClass.listOfFields:
        print("UML> No duplicates allowed! Attribute must be unique.")
            
    else:
        return True   



def searchMethod(wantedClass: str, name: str):
    if name.title().strip() in wantedClass.listOfMethods:
        print("UML> No duplicates allowed! Method must be unique.")
            
    else:
        return True   
       
     
   
# search for fields
def searchField(wantedClass: str, name: str):
    if name.casefold().strip() in wantedClass.listOfFields:
       print("UML> No duplicates allowed! Field must be unique.")
    else:
        return True
    
    
def searchParam(method: str, param: str):
    if param.casefold().strip() in method.listOfParameters:
        print("UML> No duplicates allowed! Parameter must be unique.")
    else:
        return True
    

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





