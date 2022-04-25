# Project Name  : UML_BootSnake
# File Name     : attributes.py
# Course        : CSCI 420
# Professor     : DrStephanie Schwartz
# BootSnake Team: Amelia S., Andy P., Ben M., Tram T., Travis Z.


###############################################################################

import re # checks if the string contains any special characters
import keyword

# Project Name  : UML_BootSnake
# File Name     : attributes.py 
# Course        : CSCI 420
# Professor     : DrStephanie Schwartz
# BootSnake Team: Amelia S., Andy P., Ben M., Tram T., Travis Z.


###############################################################################

import re # checks if the string contains any special characters
import keyword

from classModel import *
from parametersModel import *
from sharedItems import *



"""
An attribute is named property of a class that describes the object
being modeledGenerally, the attributes' characteristics depict their
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

    Given the class is not existed, it prompts user for a valid class name
    
    Notes: 
        1'Uppercase' words will systematically convert to converted to 
            'lowercase' words.
        2Case-insensitive when searching for field(s).

    """
    
    """ 
        To use formatted string literals, begin a string with f or F before 
        the opening quotation mark or triple quotation markInside the string,
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
            if not searchField(classname,fieldname.strip()):
                        
                newField = FieldClass(fieldname, fieldtype)
                wantedClass.listOfFields.append(newField)
                print("UML> Field " + fieldname + " successfully added!")
                msg = f"{fieldname} successfully added to {classname}."
            
                wantedClass.listOfFields.sort(key = lambda x : x.name)
                #for o in wantedClass.listOfFields:
                #    print(o.name)
                if (undoListInsertable.bool):
                    undoList.insert(0, (delField, (classname, fieldname, fieldtype)))
                return msg
    
            else:
                print("Field " + fieldname + " existed! No duplicates allowed!")
                msg = f"{fieldname} existed! No duplicates allowed!"
    else:
        print("Class " + classname + " not existed! Enter a valid class!")
        msg =f"{classname} not existed! Enter a valid class!"
        return msg
        
   

###############################################################################


def delField (classname: str, fieldname:str, fieldtype = 0):
    """
    The delField deletes a field(s) for a given class provided
    that the class & the field must exist in the systemIt provides user 
    with the following choices:
        
        1Deleting a selected field(s) one-by-one.
        2Delete ALL fields of a class at once.
        3Opt out
    
    When either the selected class or field(s) is not existed, it prompts
    user for a valid name.

    """

    msg: str =""
    
    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)

    if wantedClass:
        
        if wantedClass.listOfFields:
                
            while True:
                if searchField(classname, fieldname):
                    for o in wantedClass.listOfFields:
                        if o.name.strip() == fieldname.strip():
                            if (undoListInsertable.bool):
                                undoList.insert(0, (addField, (classname, fieldname, o.type)))
                            wantedClass.listOfFields.remove(o)
                            
                            print("UML> Field '" + fieldname +"' successfully deleted!")
                            msg = f"{fieldname} successfully deleted!"
                            wantedClass.listOfFields.sort(key = lambda x : x.name)
                        
                
                            return msg    
                                
                    #break
                            
                    # If user enters ALL/all to remove all fields.
                else:
                    if fieldname.strip() == 'all':
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
    class in the systemThe newly-created name must be unique within the class
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
                fieldObj = searchField(classname, fieldname.strip())
                if fieldObj:
                    if fieldObj.name == fieldname:
                        # validate the fieldname and its status in the system prior to updating.
                        if not searchField(classname,newname):
                            if (checkName(wantedClass, newname)):
                                fieldObj.name = newname
                                print("UML> Field " +fieldname + " successfully renamed to " + newname +"!")
                                msg = f"{fieldname} successfully renamed to {newname}!"
                                if (undoListInsertable.bool):
                                    undoList.insert(0, (renField, (classname, newname, fieldname)))
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

def addMethod(classname: str, methodname: str, methtype: str,  paramlist: list() = None):
    
    """
    The addMethod adds a method(s) for a selected, existing class
    in the system provided that the method has unique identifiers within 
    the class.
    
    This function allows user to continue adding methods untill user
    presses 'quit'.

    Given the class is not existed, it prompts user for a valid class name
    
    Notes: 
        1'Uppercase' words will systematically convert to converted to 
            'propercase' words.
        2Case-insensitive when searching for method(s).

    """
    
    msg: str =""
    # search for the class in the system
    wantedClass = ClassSearch(classname, listOfClasses)
    if wantedClass:
        # verify the validity of the methodname
        if  checkMethName(wantedClass, methodname.strip()) and checkMethName(wantedClass, methtype.strip()):    
            
            # check if the method object already existed in the listOfMethods
            if not searchMethod(classname, methodname.strip()):
                
                newMethObj = MethodClass(methodname.strip(), methtype.strip())
                wantedClass.listOfMethods.append(newMethObj)
                print("Method " + methodname + " successfully added!")
                msg = f"{methodname} successfully added!"
                
                if (undoListInsertable.bool):
                    undoList.insert(0, (delMethod, (classname, methodname, methtype)))

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
    class in the systemThe newly-created name must be unique within the class
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
                mObj = searchMethod(classname, methodname.strip()) 
                
                if mObj:
                    if mObj.name.strip() == methodname.strip():
                   
                        if not searchMethod(classname, newmethod):
                            if checkMethName(wantedClass, newmethod.strip()):
                                
                                mObj.name = newmethod
                                print("UML> Method " + methodname + " successfully renamed!")
                            
                                # sort the list of method objects   
                                wantedClass.listOfMethods.sort(key = lambda x : x.name)
                                for o in wantedClass.listOfMethods:
                                    print(o.name)

                                msg = f"Method {methodname} successfully renamed to {newmethod}!"
                                if(undoListInsertable.bool):
                                    undoList.insert(0,(renMethod, (classname, newmethod, methodname)))
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

def delMethod (classname: str, methodname: str, methtype = 0):
    """
    The delMethod deletes a method(s) for a given class provided
    that the class & the method must exist in the systemIt provides 
    user with the following choices:
        
        1Delete a selected method(s) one-by-one.
        2Delete ALL methods of a class at once.
        3Opt out
    
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
                        if searchMethod( classname, methodname):     
                            for o in wantedClass.listOfMethods:
                                if o.name.strip() == methodname.strip():
                                    if(undoListInsertable.bool):
                                        reverseList = list()
                                        meth = searchMethod (classname, methodname)
                                        for param in meth.listOfParams:
                                            reverseList.insert(0, (ParamAdd, (classname, methodname, param.name, param.type)))
                                        reverseList.insert(0, (addMethod, (classname, methodname, meth.type)))
                                        undoList.insert(0, reverseList)
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
                            if methodname.strip() == 'all':
                                wantedClass.listOfMethods.clear()
                                print("All methods of " + classname +" successfully" 
                                + " deleted!Enter 'q' to exit!")
                                
                                msg = f"All methods of {classname} successfully deleted!"
                   
                                # remove the parameter lists of the methods.
                                # for o in wantedClass.listOfMethods:
                                #     for p in o.listOfParams:
                                #         o.listOfParams.clear()
                                #         print("All parameters of the methods deleted!")
                                    
                                # sort & print the list of method objects
                                # wantedClass.listOfMethods.sort(key = lambda x : x.name)
                                # for o in wantedClass.listOfMethods:
                                #     print(o.name)
                             
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
    that the class & the method must exist in the systemIt provides 
    user with the following choices:
        
        1Delete a selected method(s) one-by-one.
        2Delete ALL methods of a class at once.
        3Opt out
    
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
                    wantedParam = searchParam(wantedMethod, paramname) 
                    if wantedParam:  
                        for o in wantedMethod.listOfParams:
                            if o.name.strip() == paramname.strip():
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
                        if paramname.strip() == 'all':
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
        that the class & the method must exist in the systemIt provides 
        user with the following choices:
        
        1Rename a selected param(s) one-by-one.
        2Opt out
    
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
                            thisParam = searchParam(thisMeth, param.strip())
                            if thisParam:
                                if thisParam.name.strip() == param.strip():    
                                    if not searchParam(thisMeth, newname):    
                                        if checkParamName(thisMeth, newname.strip()):
                                
                                            thisParam.name = newname
                                            print("UML> Parameter "+ param +" successfully renamed to " + newname + "!")
                                            if(undoListInsertable.bool):
                                                undoList.insert(0,(renameParam, (classname, methodname, newname, param)))
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
    in the system
    
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
    in the system
    
    It prompts user if multi-word method name with spaces entered.

    """
    
    if not name.strip():  
        print("UML> Name and/or type cannot be blank!")
        return False
            
            
    elif (regexMeth.search(name.strip()) != None):
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
    in the system
    
    It prompts user if multi-word method name with spaces entered.

    """
    
    if not paramname.strip():  
        print("UML> Name and/or type cannot be blank!")
        return False
            
            
    elif (regexMeth.search(paramname.strip()) != None):
        print("UML> No special characters allowed!")
        return False
            
    elif paramname[:1].strip().isnumeric(): 
        print("UML> Parameter and/or type cannot be preceded by an integer(s)!")
        return False
            
    
    elif keyword.iskeyword(paramname.strip()):      
        print("UML> Keywords are not allowed!")
        return False

    elif match.search(paramname.strip()) != None:
        print("UML> No space allowed! Use an underscore!")
        return False
    
    else:
        for o in wantedMethod.listOfParams:
            if o.name.strip() == paramname.strip():
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
            if (mObj.name== methname.strip()):
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
            if (o.name.strip() == name.strip()):
                return o
    
    elif wantedClass is None: 
        return None
#########################################################################################    
# search for a parameter    
def searchParam( methObj: object, param: str):
    
    for x in methObj.listOfParams:
        if x.name.strip() == param.strip():
            return x
    return None
    


#########################################################################################
# # Give the user some context.
# print("\nWelcome to the BootSnake Geeks campWhat would you like to do?")

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





