# Project Name  : UML_BootSnake
# File Name     : attributes.py
# Course        : CSCI 420
# Professor     : Dr. Stephanie Schwartz
# BootSnake Team: Amelia S., Andy P., Ben M., Tram T., Travis Z.


###############################################################################

import re # checks if the string contains any special characters
import keyword

# Project Name  : UML_BootSnake
# File Name     : attributes.py 
# Course        : CSCI 420
# Professor     : Dr. Stephanie Schwartz
# BootSnake Team: Amelia S., Andy P., Ben M., Tram T., Travis Z.


###############################################################################

import re # checks if the string contains any special characters
import keyword


from classModel import *
from parametersModel import *
from sharedItems import *



"""
An attribute is named property of a class that describes the object
being modeled. Generally, the attributes' characteristics depict their
visibility & accessiblity within a given class.

The four types of attribute visibility include Public, Private, Protected
and Package denoted by +, _, #, or ~  signs respectively.

"""

# Create a character set to check for special characters
regex:str =""
regex = re.compile('[@!$%^&*()<>?/\\\|}{:\[\]\']')

regexMeth:str =""
regexMeth = re.compile('[@!$%^&*<>?/\\\|}{\[\]\']')

# Create a set of blank spaces to check for spaces between words
match:str =""
match = re.compile('[ ]+')

class MethodClass:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        self.listOfParams = list()
        
        

class FieldClass:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
       
    
        
########################################################################################    
    
 
  
def addField(classname : str, fieldname : str, fieldtype: str):
    """
    The addField adds a field(s) for a selected, existing class
    in the system provided that the field is unique within the class.
    
    This function allows user to continue adding fields untill user
    presses 'quit'.

    Given the class is not existed, it prompts user for a valid class name. 
    
    Notes: 
        1. 'Uppercase' words will systematically convert to converted to 
            'lowercase' words.
        2. Case-insensitive when searching for field(s).

    """
    
    """ 
        To use formatted string literals, begin a string with f or F before 
        the opening quotation mark or triple quotation mark. Inside the string,
        Python expressions, variables or literal values, are enclosed between 
        { and } characters.

        Need the returned message to show up in the GUI
    
    """
    # variable to hold message display in GUI
    msg: str =""
    
    #call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)
    
    if wantedClass:
        # validate the fieldname and fieldtype.
        if checkName(wantedClass, fieldname) and checkName(wantedClass, fieldtype):
            if not searchField(classname,fieldname.strip().casefold()):
                        
                newField = FieldClass(fieldname, fieldtype)
                wantedClass.listOfFields.append(newField)
                print("UML> Field " + fieldname + " successfully added!")
                msg = f"{fieldname} successfully added to {classname}."
            
                wantedClass.listOfFields.sort(key = lambda x : x.name)
                #for o in wantedClass.listOfFields:
                #    print(o.name)
                    
                return msg
    
            else:
                print("Field " + fieldname + " existed! No duplicates allowed!")
                msg = f"{fieldname} existed! No duplicates allowed!"
    else:
        print("Class " + classname + " not existed! Enter a valid class!")
        msg =f"{classname} not existed! Enter a valid class!"
        return msg
        
   

###############################################################################


def delField (classname: str, fieldname:str):
    """
    The delField deletes a field(s) for a given class provided
    that the class & the field must exist in the system. It provides user 
    with the following choices:
        
        1. Deleting a selected field(s) one-by-one.
        2. Delete ALL fields of a class at once.
        3. Opt out. 
    
    When either the selected class or field(s) is not existed, it prompts
    user for a valid name.

    """

    msg: str =""
    
    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)

    if wantedClass:
        
        if wantedClass.listOfFields:
                
            while True:
                if searchField(classname, fieldname.casefold()):
                    for o in wantedClass.listOfFields:
                        if o.name.strip().lower() == fieldname.lower().strip():
                            wantedClass.listOfFields.remove(o)
                            
                            print("UML> Field '" + fieldname +"' successfully deleted!")
                            msg = f"{fieldname} successfully deleted!"
                            wantedClass.listOfFields.sort(key = lambda x : x.name)
                        
                
                            return msg    
                                
                    #break
                            
                    # If user enters ALL/all to remove all fields.
                else:
                    if fieldname.casefold().strip() == 'all':
                        wantedClass.listOfFields.clear()
                        print("All Fields successfully deleted! Enter 'q' to exit!")
                        msg = f"All fields sucessfully deleted!"
                        return msg
                        
                             
                    else:
                        print("Field " + fieldname + " not found! Try again!")
                        msg =f"{fieldname} not found! Try again!"
                        return msg
                                      
                
        else: 
            print("No fields for class " + classname  + "! Enter 'q' to exit!")
            msg = f"No fields for {classname}"
            return msg
            
                   
    else:
        print("Class " + classname + " not existed! Enter a valid class!")
        msg = f"{classname} not existed! Enter a valid class!"
        return msg
        
      

###############################################################################


def renField (classname: str, fieldname: str, newname: str):
    """
    The renField renames an existing field(s) for a given existing
    class in the system. The newly-created name must be unique within the class. 
    It calls check_name method to verify the validity of the renamed field
    prior to updating the field name for the class.

    User can continue renaming the selected field or stop at any time by
    pressing 'quit'

    When either the selected class or field(s) is not existed, it prompts
    user for a valid name.

    """

    msg: str = ""
    
    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)
    if wantedClass:
        
        if wantedClass.listOfFields:
            while True:
                fieldObj = searchField(classname, fieldname.strip().casefold())
                if fieldObj:
                    if fieldObj.name.casefold() == fieldname.casefold():
                        # validate the fieldname and its status in the system prior to updating.
                        if not searchField(classname,newname):
                            if (checkName(wantedClass, newname)):
                                fieldObj.name = newname
                                print("UML> Field " +fieldname + " successfully renamed to " + newname +"!")
                                msg = f"{fieldname} successfully renamed to {newname}!"
                                return msg

                        else:
                            print("Field " + newname + " existed! No duplicates allowed!")  
                            msg = f"{newname} existed! No duplicates allowed!"  
                            return msg                        
                               
                else:
                    print("Field " + fieldname + " not found!")
                    msg = f"{fieldname} not found!"
                    return msg
                    
                
                
                        
                
        else: 
            print("No fields for class " + classname + "! Enter 'q' to exit")
            msg = f"No fields for class {classname}"
            return msg
    else:
        print("Class " + classname + " not found! Try again!")
        msg = f"class {classname} not found! Try again!" 
        return msg
    
###############################################################################

def addMethod(classname: str, methodname: str, methtype: str,  paramlist: list()):
    
    """
    The addMethod adds a method(s) for a selected, existing class
    in the system provided that the method has unique identifiers within 
    the class.
    
    This function allows user to continue adding methods untill user
    presses 'quit'.

    Given the class is not existed, it prompts user for a valid class name. 
    
    Notes: 
        1. 'Uppercase' words will systematically convert to converted to 
            'propercase' words.
        2. Case-insensitive when searching for method(s).

    """
    
    msg: str =""
    # search for the class in the system
    wantedClass = ClassSearch(classname, listOfClasses)
    if wantedClass:
        # verify the validity of the methodname
        if  checkMethName(wantedClass, methodname.title().strip()) and checkMethName(wantedClass, methtype.title().strip()):    
            
            # check if the method object already existed in the listOfMethods
            if not searchMethod(classname, methodname.strip().title()):
                
                newMethObj = MethodClass(methodname.strip().title(), methtype.strip())
                wantedClass.listOfMethods.append(newMethObj)
                print("Method " + methodname + " successfully added!")
                msg = f"{methodname} successfully added!"
                
                print(newMethObj.name)
                print("Class " + classname + "'s listOfMethods:")
                
                wantedClass.listOfMethods.sort(key = lambda x : x.name)
                for o in wantedClass.listOfMethods:
                    print(o.name)
                
                return msg
                                        
            else:
                print("Method " + methodname + " existed! No duplicates allowed!") 
                msg = f"{methodname} existed! No duplicated allowed!"   
                return msg 
 
          
    else:
        print("Class " + classname + " not existed! Enter a valid class!")
        msg = f"Class {classname} not existed! Enter a valid class!"
        return msg
    

###############################################################################

def renMethod (classname: str, methodname: str, newmethod: str):
    """
    The renMethod renames an existing method(s) for a given existing
    class in the system. The newly-created name must be unique within the class. 
    It calls searchName method to verify the validity of the renamed method
    prior to updating the method name for the class.

    User can continue renaming the selected method or stop at any time by
    pressing 'quit'

    When either the selected class or method(s) is not existed, it prompts
    user for a valid name.

    """
    
    msg:str = ""
    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)
    if wantedClass:
       
        if wantedClass.listOfMethods:
            while True:
                #call searchMethod to search for the given method.
                mObj = searchMethod(classname, methodname.strip().title()) 
                
                if mObj:
                    if mObj.name.strip() == methodname.strip().title():
                   
                        if not searchMethod(classname, newmethod.casefold()):
                            if checkMethName(wantedClass, newmethod.strip().title()):
                                
                                mObj.name = newmethod
                                print("UML> Method " + methodname + " successfully renamed!")
                            
                                # sort the list of method objects   
                                wantedClass.listOfMethods.sort(key = lambda x : x.name)
                                for o in wantedClass.listOfMethods:
                                    print(o.name)

                                msg = f"Method {methodname} successfully renamed to {newmethod}!"
                                return msg

                        else:
                            print("method "+ newmethod + " existed! No duplicates allowed!")
                            return f'method {newmethod} existed! No duplicates allowed!'
                                          
                else:
                    print("Method " + methodname + " not found!")
                    msg = f"Method {methodname} not found!"
                    return msg

        else: 
            print("No methods found for class " + classname  + " ! Enter 'q' to exit!")
            msg = f"No methods found for class {classname}"
            return msg
              
    else:
        print("Class " + classname + " not found! Try again!") 
        msg = f"Class {classname} not found! Try again!"
        return msg
         
###############################################################################              

def delMethod (classname: str, methodname: str):
    """
    The delMethod deletes a method(s) for a given class provided
    that the class & the method must exist in the system. It provides 
    user with the following choices:
        
        1. Delete a selected method(s) one-by-one.
        2. Delete ALL methods of a class at once.
        3. Opt out. 
    
    When either the selected class or method(s) is not existed, it prompts
    user for a valid name.

    """

    msg:str = ""
    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)

    if wantedClass:
        #while True:
            if wantedClass.listOfMethods:
                
                    while True:
                        # call searchMethod to search for the specified method.
                        if searchMethod( classname, methodname.casefold()):     
                            for o in wantedClass.listOfMethods:
                                if o.name.strip().title() == methodname.strip().title():
                                    wantedClass.listOfMethods.remove(o)
                                    print("UML> Method " + methodname + " of class " + classname + " deleted!")
                                    msg = f"{methodname} of {classname} deleted!"
                                    
                                    
                                    # remove the parameter list of the method.
                                    if o.listOfParams:
                                        o.listOfParams.clear()
                                        print("Parameter(s) deleted!")
                            
                                    # sort & print the list of method objects
                                    wantedClass.listOfMethods.sort(key = lambda x : x.name)
                                    for o in wantedClass.listOfMethods:
                                        print(o.name)
                                        
                                    return msg
                                
                            #break    
                           
                        # If user enters ALL/all to remove all methods.
                        else:
                            if methodname.casefold().strip() == 'all':
                                wantedClass.listOfMethods.clear()
                                print("All methods of " + classname +" successfully" 
                                + " deleted!. Enter 'q' to exit!")
                                
                                msg = f"All methods of {classname} successfully deleted!"
                   
                                # remove the parameter lists of the methods.
                                for o in wantedClass.listOfMethods:
                                    for p in o.listOfParams:
                                        o.listOfParams.clear()
                                        print("All parameters of the methods deleted!")
                                    
                                # sort & print the list of method objects
                                wantedClass.listOfMethods.sort(key = lambda x : x.name)
                                for o in wantedClass.listOfMethods:
                                    print(o.name)
                             
                                return msg
                            
                            else:
                                print("Method " + methodname + " not found! Try again!")
                                msg = f"{methodname} not found! Try again!"
                                return msg
                                break
                    
                        #break 
                        
            else: 
                print("No methods for class " + classname  + "! Enter 'q' to exit!")
                msg = f"No methods for {classname}"
                return msg
                
                
###############################################################################              

def delParam (classname: str, methodname: str, paramname: str):
    """
    The delMethod deletes a method(s) for a given class provided
    that the class & the method must exist in the system. It provides 
    user with the following choices:
        
        1. Delete a selected method(s) one-by-one.
        2. Delete ALL methods of a class at once.
        3. Opt out. 
    
    When either the selected class or method(s) is not existed, it prompts
    user for a valid name.

    """

    msg: str = ""
    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)

    if wantedClass:
        #while True:
            if wantedClass.listOfMethods:
                # call searchMethod to search for the specified method.
                wantedMethod = searchMethod( classname, methodname)
                if wantedMethod:    
                    wantedParam = searchParam(wantedMethod, paramname.casefold()) 
                    if wantedParam:  
                        for o in wantedMethod.listOfParams:
                            if o.name.strip().lower() == paramname.strip().lower():
                                wantedMethod.listOfParams.remove(o)
                                print("UML> Parameter " + paramname + " of class " + classname + " deleted!")

                                msg = f"{paramname} of {classname} deleted!"
                                
                                
                                
                                # sort & print the list of param objects
                                wantedMethod.listOfParams.sort(key = lambda x : x.name)
                                for o in wantedMethod.listOfParams:
                                    print(o.name)
                                
                                return msg        
                                
                            # If user enters ALL/all to remove all methods.
                    else:
                        if paramname.casefold().strip() == 'all':
                            wantedMethod.listOfParams.clear()
                            print("All parameters of " + classname +" successfully" 
                                    + " deleted! Enter 'q' to exit!")
                            
                            msg = f"All parameters of {classname} successfully deleted!"       
                            # sort & print the list of param objects
                            wantedMethod.listOfParams.sort(key = lambda x : x.name)
                            # for o in wantedMethod.listOfParams:
                            #     print(o.name)
                        
                            return msg
                        
                        else:
                            print("Parameter " + paramname + " not found!") 
                            msg = f"{paramname} not found!" 
                            return msg             
                
                
                else:
                    print("Method " + methodname + " not found! Try again!")
                    msg = f"{methodname} not found! Try again!"
                    return msg              
                        
            else: 
                print("No methods for class " + classname  + "! Enter 'q' to exit!")
                msg = f"No methods for {classname}!"
                return msg
               
###############################################################################

def renameParam(classname: str, methodname: str, param: str, newname: str):
    """
        The renameParam renames a method's param for a given class provided
        that the class & the method must exist in the system. It provides 
        user with the following choices:
        
        1. Rename a selected param(s) one-by-one.
        2. Opt out. 
    
    When either the selected class or method(s) is not existed, it prompts
    user for a valid name.
    
    """
    msg:str =""
    
    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)
    if wantedClass:
            if wantedClass.listOfMethods:
                #while True:
               
            # Access to the given method's parameter list of a specified
            # class to find the indicated param
                    thisMeth = searchMethod(classname, methodname)
                    if thisMeth:
                        if thisMeth.listOfParams:
                            thisParam = searchParam(thisMeth, param.strip().lower())
                            if thisParam:
                                if thisParam.name.strip().lower() == param.strip().lower():    
                                    if not searchParam(thisMeth, newname.casefold()):    
                                        if checkParamName(thisMeth, newname.strip().casefold()):
                                
                                            thisParam.name = newname
                                            print("UML> Parameter "+ param +" successfully renamed to " + newname + "!")
                                            msg = f"{param} successfully renamed to {newname}!"
                                    
                                        
                                        for o in thisMeth.listOfParams:
                                            print(o.name)
                                        
                                            break

                                        return msg

                                    else:
                                        print(newname+ " existed! No duplicates allowed!") 
                                        msg = f"{newname} existed! No duplicates allowed!" 
                                        return msg                                
                            else:
                                print("Parameter " + param + " not found! Try again!")
                                msg = f"{param} not found! Try again!"
                                return msg
                        
                        else: 
                            print("No parameters for method " + methodname  + "! Enter 'q' to exit!")
                            msg = f"No parameters for {methodname}"
                            return msg
                                                    
                    else:
                        print("Method " + methodname + " not found! Try again!")
                        msg = f"{methodname} not found! Try again!"
                        return msg
                                       
            else: 
                print("No methods existed for class " + classname  + "! Select a valid class!")
                msg = f"No methods existed for {classname}! Select a valid class"
                return msg
                
    else:
        print("Class " + classname + " not found! Try again!")
        msg = f"{classname} not found! Try again!"
        return msg

###################################################################################################
# Helper functions

def checkName(wantedClass: str, name: str):
    """"
    
    The function checkName verifies the validity of a field's name and its type
    input by user by checking whether it is blank, non-alphanumeric, 
    reserved keyword, or preceded by an special character(s), an integer(s),
    or non-existing within a class prior to adding the identifier 
    in the system. 
    
    It prompts user if multi-word field name with spaces entered.

    """
    
    msg:str =""
    if not name.strip() :  
        print("UML> name and type cannot be blank!")
        msg = f"name and type cannot be blank!"
        return False
            
    #elif len(name.strip()) < 2 or len(name.strip()) > 16:
    #    print("UML> Attribute must be 3-15 characters long!")
            
    elif regex.search(name.strip()) != None:
        print("UML> No special characters allowed!")
        msg = f"No special characters allowed!"
        return False
            
    elif name[:1].strip().isnumeric(): 
        print("UML> Field Name and/or its type cannot be preceded by an integer(s)!")
        msg = f"Fieldname and/or its type cannot be preceded by an integer(s)"
        return False
            
    elif name[:3].strip() == "___":     
        print("UML> Leading underscores (> 2) are not allowed!")
        msg = f"Leading underscore >2 are not allowed!"
        return False
            
    #elif name[-3].strip() == "_":     
    #    print("UML> Trailing underscores (> 2) are not allowed!")
            
    elif keyword.iskeyword(name.strip()):      
        print("UML> Keywords are not allowed!")
        msg = f"Keywords are not allowed!"
        return False

    else:
        if (match.search(name)) != None:
            print("UML> No space allowed! Use an underscore!")
            msg = f"No space allowed! Use an underscore!"
        
            return False

        return True
##########################################################################################

def checkMethName(wantedClass, name: str):
    
    """"
    
    The function checkMethName verifies the validity of a method's name and its type
    input by user by checking whether it is blank, non-alphanumeric, 
    reserved keyword, or preceded by an special character(s), an integer(s),
    or non-existing within a class prior to adding the identifier 
    in the system. 
    
    It prompts user if multi-word method name with spaces entered.

    """
    
    if not name.strip():  
        print("UML> Name and/or type cannot be blank!")
        return False
            
            
    elif (regexMeth.search(name.strip().title()) != None):
        print("UML> No special characters allowed!")
        return False
            
    elif name[:1].strip().isnumeric(): 
        print("UML> Method cannot be preceded by an integer(s)!")
        return False
            
    elif name[:3].strip() == "___":     
        print("UML> Leading underscores (> 2) are not allowed!")
        return False
            
    
    elif keyword.iskeyword(name.strip()):      
        print("UML> Keywords are not allowed!")
        return False

    else: 
        if (match.search(name) != None):
            print("UML> No space allowed! Use an underscore!")
            msg = f"No space allowed! Use an underscore!"
            return not bool(msg)#False
        
        return True
##############################################################################################      

def checkParamName(wantedMethod, paramname: str):
    
    """"
    
    The function checkParamName verifies the validity of a parameter's name
    & type input by user by checking whether it is blank, non-alphanumeric, 
    reserved keyword, or preceded by an special character(s), an integer(s),
    or non-existing within a class prior to adding the identifier 
    in the system. 
    
    It prompts user if multi-word method name with spaces entered.

    """
    
    if not paramname.strip():  
        print("UML> Name and/or type cannot be blank!")
        return False
            
            
    elif (regexMeth.search(paramname.strip().title()) != None):
        print("UML> No special characters allowed!")
        return False
            
    elif paramname[:1].strip().isnumeric(): 
        print("UML> Parameter and/or type cannot be preceded by an integer(s)!")
        return False
            
    
    elif keyword.iskeyword(paramname.strip()):      
        print("UML> Keywords are not allowed!")
        return False

    elif match.search(paramname.strip().title()) != None:
        print("UML> No space allowed! Use an underscore!")
        return False
    
    else:
        for o in wantedMethod.listOfParams:
            if o.name.lower().strip() == paramname.lower().strip():
                print("UML> No duplicates allowed! Parameter(s) must be unique!")
                return False
        
        return True
    
##############################################################################################  
# search for a method
def searchMethod(classname: str, methname: str) :
    # loop through the list of methods of a given class to search for a 
    # existing method in the system.
    wantedClass = ClassSearch(classname, listOfClasses)
    
    if wantedClass:
        for mObj in wantedClass.listOfMethods:
            if (mObj.name.title() == methname.title().strip()):
                return mObj
    elif wantedClass is None: 
        return None
            
######################################################################################     
   
# search for fields
def searchField(classname: str, name: str):
    # loop through the list of fields of a given class to search for a 
    # existing method in the system.
    wantedClass = ClassSearch(classname, listOfClasses)
    
    if wantedClass:
        for o in wantedClass.listOfFields:
            if (o.name.casefold().strip() == name.casefold().strip()):
                return o
    
    elif wantedClass is None: 
        return None
#########################################################################################    
# search for a parameter    
def searchParam( methObj: object, param: str):
    
    for x in methObj.listOfParams:
        if x.name.strip().casefold() == param.casefold().strip():
            return x
    return None
    


#########################################################################################
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





