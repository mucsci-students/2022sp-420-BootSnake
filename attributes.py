# Project Name  : UML_BootSnake
# File Name     : attributes.py
# Course        : CSCI 420
# Professor     : Dr. Stephanie Schwartz
# BootSnake Team: Amelia S., Andy P., Ben M., Tram T., Travis Z.


###############################################################################

import re # checks if the string contains any special characters
import keyword

from copy import deepcopy
from classModel import *


"""
An attribute is named property of a class that describes the object
being modeled. Generally, the attributes' characteristics depict their
visibility & accessiblity within a given class.

The four types of attribute visibility include Public, Private, Protected
and Package denoted by +, _, #, or ~  signs respectively.

"""


#listOfFields = list()
#listOfMethods = list()
#listOfParams = list()

# Create a character set to check for special characters
regex = re.compile('[@!$%^&*()<>?/\\\|}{:\[\]\']')

regexMeth = re.compile('[@!$%^&*<>?/\\\|}{\[\]\']')
# Create a set of blank spaces to check for spaces between words
match = re.compile('[ ]+')

class MethodClass:
    def __init__(self, name: str ):
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
            return "UML> Field " + fieldname + " successfully added!"
    else:
        print("Class " + classname + " not existed! Enter a valid class!")
        return "Class " + classname + " not existed! Enter a valid class!"
        
   

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
        
        if wantedClass.listOfFields:
                
            # Remove the field(s) from a list of fields when found.
                    
            print(wantedClass.listOfFields)
            while True:
                for item in wantedClass.listOfFields:
                    if item.casefold() == fieldname.casefold().strip():
                        wantedClass.listOfFields.remove(fieldname.lower().strip())
                        print("UML> Field '" + fieldname +"' deleted!")
                        print(wantedClass.listOfFields)
                        return "UML> Field '" + fieldname +"' deleted!")
                        break
                            
                    # If user enters ALL/all to remove all fields.
                    elif fieldname.casefold().strip() == 'all':
                        wantedClass.listOfFields.clear()
                        print("All Fields successfully deleted! Enter 'q' to exit!")
                        print(wantedClass.listOfFields)
                        return "All Fields successfully deleted! Enter 'q' to exit!"
                        break
                             
                else:
                    print("Field " + fieldname + " not found! Try again!")
                    print(wantedClass.listOfFields)
                    return "Field " + fieldname + " not found! Try again!"
                    break
                   
                break   
                
        else: 
            print("No fields for class " + classname  + "! Enter 'q' to exit!")
            return "No fields for class " + classname  + "! Enter 'q' to exit!"
            
                   
    else:
        print("Class " + classname + " not existed! Enter a valid class!")
        return "Class " + classname + " not existed! Enter a valid class!"
        
      

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
        #while True:
        if wantedClass.listOfFields:
            while True:
            # Rename the field(s) from a list of fields by iterating
            # through the list to find its index
                for i in range(len(wantedClass.listOfFields)):
                    if wantedClass.listOfFields[i].casefold().strip() == fieldname.casefold().strip():
                        while True:

                            if (checkName(wantedClass, newname)):
                                wantedClass.listOfFields[i] = newname.lower().strip()
                                print("UML> Field " +fieldname + " successfully renamed!")
                                print(wantedClass.listOfFields)
                                return "UML> Field " +fieldname + " successfully renamed!"
                                break 
                            break
                        break  
                                
                               
                else:
                    print("Field " + fieldname + " not found!")
                    wantedClass.listOfFields
                    return "Field " + fieldname + " not found!"
                    break
                
                break
                        
                
        else: 
            print("No fields for class " + classname + "! Enter 'q' to exit")
            return "No fields for class " + classname + "! Enter 'q' to exit"
    else:
        print("Class " + classname + " not found! Try again!")
        return "Class " + classname + " not found! Try again!"
               
      
###############################################################################

def addMethod(classname: str, methodname: str, paramlist: list()):
    
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
        # verify the validity of the methodname
        if  checkMethName(wantedClass, methodname.title().strip()):    
            
            # check if the method object already existed in the listOfMethods
            if not searchMethod(classname, methodname.strip().title()):
                
                newMethObj = MethodClass(methodname.strip().title())
                wantedClass.listOfMethods.append(newMethObj)
                print("Method " + methodname + " successfully added!")
                print(newMethObj.name)
                print("Class " + classname + "'s listOfMethods:")
                for newMethObj in wantedClass.listOfMethods:
                    print(newMethObj.name)
                     
                
                if len(paramlist.strip().lower() ) > 0:
                    newMethObj.listOfParams.append(paramlist.strip().lower())
                    print("Parameter(s) successfully added!")      
                   
                   
                    newMethObj.listOfParams.sort()
               
                    print(newMethObj.listOfParams)
                    
                
                return "Method " + methodname + " and parameter(s) added!"
                #else:
                    #print("Method " + methodname + " with the same param(s)"+
                    #      paramlist + " existed!")
            else:
                print("Method " + methodname + " existed! No duplicates allowed!")   
                return "Method " + methodname + " existed! No duplicates allowed!"  
               
      
          
    else:
        print("Class " + classname + " not existed! Enter a valid class!")
        return "Class " + classname + " not existed! Enter a valid class!"
    

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
       
        if wantedClass.listOfMethods:
            while True:
                mObj = searchMethod(classname, methodname.strip().title())
                
                if mObj :
                    if mObj.name == methodname.strip().title():
                   
                        if checkMethName(wantedClass, newmethod.strip().title()):
                                
                            mObj.name = newmethod.title().strip()
                            print("UML> Method " + newmethod + " successfully renamed!")
                            return "UML> Method " + newmethod + " successfully renamed!"
                               
                        
                    #print("Method " + methodname + " with same "+
                    #    "param(s) existed! No duplicates allowed!")
                    #break  
                                
                      
                else:
                    print("Method " + methodname + " not found!")
                    return "Method " + methodname + " not found!"
                    break
                break
               
        else: 
            print("No Methods found for class " + classname  + " ! Enter 'q' to exit!")
            return "No Methods found for class " + classname
              
    else:
        print("Class " + classname + " not found! Try again!") 
        return "Class " + classname + " not found! Try again!"
         
###############################################################################              

def delMethod (classname: str, methodname: str):
    '''
    The delMethod deletes a method(s) for a given class provided
    that the class & the method must exist in the system. It provides 
    user with the following choices:
        
        1. Delete a selected method(s) one-by-one.
        2. Delete ALL methods of a class at once.
        3. Opt out. 
    
    When either the selected class or method(s) is not existed, it prompts
    user for a valid name.

    '''

    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)

    if wantedClass:
        #while True:
            if wantedClass.listOfMethods:
                
                    while True:
                        if searchMethod( classname, methodname):   
                            for o in wantedClass.listOfMethods:
                                if o.name.strip().title() == methodname.strip().title():
                                    wantedClass.listOfMethods.remove(o)
                                    print("UML> Method " + methodname + " of class " + classname + " deleted!")
                            
                                    if o.listOfParams:
                                        o.listOfParams.clear()
                                        print("Parameter(s) deleted!")
                            
                        
                                    for o in wantedClass.listOfMethods:
                                        print(o.name)
                                
                            return "UML> Method " + methodname + " of class " + classname + " deleted!"
                            break    
                        
                           
                        # If user enters ALL/all to remove all fields.
                        else:
                            if methodname.casefold().strip() == 'all':
                                wantedClass.listOfMethods.clear()
                                print("All methods of " + classname +" successfully" 
                                + " deleted!. Enter 'q' to exit!")
                   
                                
                                for o in wantedClass.listOfMethods:
                                    for p in o.listOfParams:
                                        o.listOfParams.clear()
                                        print("All parameters of the methods deleted!")
                                    
                               
                                for o in wantedClass.listOfMethods:
                                    print(o.name)
                                return "All methods of " + classname + " successfully" + " deleted!. Enter 'q' to exit!"
                            else:
                                print("Method " + methodname + " not found! Try again!")
                                return "Method " + methodname + " not found! Try again!"
                                break
                    
                        break 
                        
            else: 
                print("No methods for class " + classname  + "! Enter 'q' to exit!")
                return "No methods for class " + classname
    
                                
           
###############################################################################

def changeParam(classname: str, methodname: str, param: str):
    """
        The changeParam replaces a method's param for a given class provided
        that the class & the method must exist in the system. It provides 
        user with the following choices:
        
        1. Replace a selected param(s) one-by-one.
        2. Replace ALL params of a class's method at once.
        3. Opt out. 
    
    When either the selected class or method(s) is not existed, it prompts
    user for a valid name.
    
    """
    
    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)
    if wantedClass:
        if wantedClass.listOfMethods:
               
            # Access to the given method's parameter list of a specified
            # class to find the indicated param
            methObj = searchMethod(classname, methodname)
            if methObj:
                paramO = searchParam(methObj, param)
                if paramO:
                    #paramlist = deepcopy(methObj.listOfParams)
                    #paramlist.pop(paramlist.index(param))
                    #mObj = MethodClass(methodname)
                    #mObj.listOfParams.append(paramlist)
                    methObj.listOfParams.remove(paramO)
                    print("Parameter(s) " + param + " of the method " +
                          "'"+ methodname +"' deleted!")
                    return "Parameter(s) " + param + " of the method " + "'"+ methodname +"' deleted!"
                # If user enters ALL/all to remove all params.      
                elif param.strip().casefold() =='All':
                     methObj.listOfParams.clear()
                     print("All parameters successfully deleted!")
                     return "All parameters successfully deleted!"
                        
                else:
                    print("Method " + methodname + "'s parameter " + param + " not found!")
                    for o in methObj.listOfParams:
                        print(o.name +" : " + o.type)
                    return "Method " + methodname + "'s parameter " + param + " not found!"
              
            else:
                print("Method " + methodname + " not found! Try again!")   
                return "Method " + methodname + " not found! Try again!" 
                
               
        else: 
            print("No Methods existed for class " + classname  + "! Select a valid class!")
            return "No Methods existed for class " + classname  + "! Select a valid class!"
              
    else:
        print("Class " + classname + " not found! Try again!")
        return "Class " + classname + " not found! Try again!"





###############################################################################
# Helper functions

def checkName(wantedClass: str, name: str):
    """"
    
    The function check_name verifies the validity of a field's name
    input by user by checking whether it is blank, non-alphanumeric, 
    reserved keyword, or preceded by an special character(s), an integer(s),
    or non-existing within a class prior to adding the identifier 
    in the system. 
    
    It prompts user if multi-word field name with spaces entered.

    """
    
    if not name.strip():  
        print("UML> Name cannot be blank!")
        return False
            
    #elif len(name.strip()) < 2 or len(name.strip()) > 16:
    #    print("UML> Attribute must be 3-15 characters long!")
            
    elif (regex.search(name.strip()) != None):
        print("UML> No special characters allowed!")
        return False
            
    elif name[:1].strip().isnumeric(): 
        print("UML> Attribute cannot be preceded by an integer(s)!")
        return False
            
    elif name[:3].strip() == "___":     
        print("UML> Leading underscores (> 2) are not allowed!")
        return False
            
    #elif name[-3].strip() == "_":     
    #    print("UML> Trailing underscores (> 2) are not allowed!")
            
    elif keyword.iskeyword(name.strip()):      
        print("UML> Keywords are not allowed!")
        return False

    elif match.search(name.strip()) != None:
        print("UML> No space allowed! Use an underscore!")
        return False
            
    # ignore lowercase or uppercase words entered by user. 
     
    elif name.casefold().strip() in wantedClass.listOfFields:
        print("UML> No duplicates allowed! Field(s) must be unique!")
        return False
    
    else:
       return True   



def checkMethName(wantedClass, name: str):
    
    """"
    
    The function check_name verifies the validity of a method's name
    input by user by checking whether it is blank, non-alphanumeric, 
    reserved keyword, or preceded by an special character(s), an integer(s),
    or non-existing within a class prior to adding the identifier 
    in the system. 
    
    It prompts user if multi-word method name with spaces entered.

    """
    
    if not name.strip():  
        print("UML> Name cannot be blank!")
        return False
            
            
    elif (regexMeth.search(name.strip().title()) != None):
        print("UML> No special characters allowed!")
        return False
            
    elif name[:1].strip().isnumeric(): 
        print("UML> Attribute cannot be preceded by an integer(s)!")
        return False
            
    elif name[:3].strip() == "___":     
        print("UML> Leading underscores (> 2) are not allowed!")
        return False
            
    
    elif keyword.iskeyword(name.strip()):      
        print("UML> Keywords are not allowed!")
        return False

    elif match.search(name.strip().title()) != None:
        print("UML> No space allowed! Use an underscore!")
        return False
    
    else:
        for o in wantedClass.listOfMethods:
            if o.name.title().strip() == name.title().strip():
                print("UML> No duplicates allowed! Method(s) must be unique!")
                return False
        return True
    
       
 
def searchMethod(classname: str, methname: str) :
    # loop through the list of methods of a given class to search for a 
    # existing method in the system.
    wantedClass = ClassSearch(classname, listOfClasses)
    #if wantedClass.listOfMethods:
        #mlist = wantedClass.listOfMethods
    #mObj = MethodClass(methname.strip().title())
    if wantedClass:
        for mObj in wantedClass.listOfMethods:
            if (mObj.name.title() == methname.title().strip()):
                return mObj
    
    else: 
        return None
            
 
#def searchParam(wantedClass: str, methodname: str, param: str, paramtype)
     
   
# search for fields
def searchField(wantedClass: str, name: str):
    if name.casefold().strip() in wantedClass.listOfFields:
       print("UML> No duplicates allowed! Field must be unique.")
    else:
        return True
    
    
def searchParam( methObj: object, param: str):
    
    for x in methObj.listOfParams:
        if x.name.strip().casefold() == param.casefold().strip():
            return x
    #return None
    

'''def ParamListAdd(paramList, paramName, paramType):
    #validParam = CheckNameType(paramName, paramType, methodName)
    if paramList:
    #if validParam:
        thisParam = Param(paramName, paramType)
        paramList.append(thisParam)

    else:
        return None   
        ''' 

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





