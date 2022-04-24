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

#from copy import deepcopy
from classModel import *
from sharedItems import *

"""
An attribute is named property of a class that describes the object
being modeled. Generally, the attributes' characteristics depict their
visibility & accessiblity within a given class.

The four types of attribute visibility include Public, Private, Protected
and Package denoted by +, _, #, or ~  signs respectively.

"""


# Create a character set to check for special characters
regex = re.compile('[@!$%^&*()<>?/\\\|}{:\[\]\']')

regexMeth = re.compile('[@!$%^&*<>?/\\\|}{\[\]\']')
# Create a set of blank spaces to check for spaces between words
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
    '''
    The addField adds a field(s) for a selected, existing class
    in the system provided that the field is unique within the class.
    
    This function allows user to continue adding fields untill user
    presses 'quit'.

    Given the class is not existed, it prompts user for a valid class name. 
    
    Notes: 
        1. 'Uppercase' words will systematically convert to converted to 
            'lowercase' words.
        2. Case-insensitive when searching for field(s).

    '''
    if not redoClass.redoCaller and redoClass.redoable:
        redoClass.redoable = False
    redoClass.redoCaller = False

    #call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)
    
    if wantedClass:
        # validate the fieldname and fieldtype.
        if checkName(wantedClass, fieldname.strip().casefold()) and checkName(wantedClass, fieldtype.casefold().strip()):
            newField = FieldClass(fieldname, fieldtype)
            wantedClass.listOfFields.append(newField)
            print("UML> Field " + fieldname + " successfully added!")
            if(undoListInsertable.bool):
                undoList.insert(0,(delField,(classname, fieldname, fieldtype)))
            wantedClass.listOfFields.sort(key = lambda x : x.name)
            for o in wantedClass.listOfFields:
                print(o.name)
            return "Field " + fieldname + " successfully added!"
                    
          
    else:
        print("Class " + classname + " does not exist! Enter a valid class!")
        return "Class " + classname + " does not exist! Enter a valid class!"
        
   

###############################################################################


def delField (classname: str, fieldname:str, fieldtype = 0):
    '''
    The delField deletes a field(s) for a given class provided
    that the class & the field must exist in the system. It provides user 
    with the following choices:
        
        1. Deleting a selected field(s) one-by-one.
        2. Delete ALL fields of a class at once.
        3. Opt out. 
    
    When either the selected class or field(s) is not existed, it prompts
    user for a valid name.

    '''
    if not redoClass.redoCaller and redoClass.redoable:
        redoClass.redoable = False
    redoClass.redoCaller = False

    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)

    if wantedClass:
        if wantedClass.listOfFields:
            while True:
                if searchField(classname, fieldname):
                    for o in wantedClass.listOfFields:
                        print(o.name)
                        print(fieldname)
                        if o.name == fieldname:
                            if(undoListInsertable.bool):
                                undoList.insert(0,(addField,(classname, fieldname, o.type)))
                            wantedClass.listOfFields.remove(o)
                            
                            print("UML> Field " + fieldname +" successfully deleted!")
                            wantedClass.listOfFields.sort(key = lambda x : x.name)            
                            return "Field " + fieldname + " successfully deleted!"
                                
                    break
                            
                    # If user enters ALL/all to remove all fields.
                else:
                    if fieldname.casefold().strip() == 'all':
                        if(undoListInsertable.bool):
                            oldListOfFields = list(wantedClass.listOfFields)
                            reverseList = list()
                            for everyField in oldListOfFields:
                                reverseList.insert(0,(addField,(classname, everyField.name, everyField.type)))
                            undoList.insert(0,reverseList)
                        wantedClass.listOfFields.clear()
                        print("All Fields successfully deleted! Enter 'q' to exit!")
                        
                        return "All Fields successfully deleted!"
                             
                    else:
                        print("Field " + fieldname + " not found! Try again!")
                        return "Field " + fieldname + " not found! Try again!"
                        
                break              
                
        else: 
            print("No fields for class " + classname  + "! Enter 'q' to exit!")
            return "No fields for class " + classname + "!"
            
                   
    else:
        print("Class " + classname + " not existed! Enter a valid class!")
        return "Class " + classname + " not existed! Enter a valid class!"
        
      

###############################################################################


def renField (classname: str, fieldname: str, newname: str):
    '''
    The renField renames an existing field(s) for a given existing
    class in the system. The newly-created name must be unique within the class. 
    It calls check_name method to verify the validity of the renamed field
    prior to updating the field name for the class.

    User can continue renaming the selected field or stop at any time by
    pressing 'quit'

    When either the selected class or field(s) is not existed, it prompts
    user for a valid name.

    '''
    if not redoClass.redoCaller and redoClass.redoable:
        redoClass.redoable = False
    redoClass.redoCaller = False

    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)
    if wantedClass:
        
        if wantedClass.listOfFields:
            while True:
                fieldObj = searchField(classname, fieldname.strip().casefold())
                if fieldObj:
                    if fieldObj.name.casefold().strip() == fieldname.strip().casefold():
                        # validate the fieldname and its status in the system prior to updating.
                        if (checkName(wantedClass, newname.strip().casefold())):
                                if(undoListInsertable.bool):
                                    undoList.insert(0,(renField,(classname, newname, fieldname)))
                                fieldObj.name = newname.strip()
                                print("UML> Field " +fieldname + " successfully renamed!")
                                return "Field " +fieldname + " successfully renamed!"
                                                    
                               
                else:
                    print("Field " + fieldname + " not found!")
                    return "Field " + fieldname + " not found!"
                
                break
                        
                
        else: 
            print("No fields for class " + classname + "! Enter 'q' to exit")
            return "No fields for class " + classname + "!"
    else:
        print("Class " + classname + " not found! Try again!")
        return "Class " + classname + " not found! Try again!"
               
      
###############################################################################

def addMethod(classname: str, methodname: str, methtype: str):
    
    '''
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

    '''
    if not redoClass.redoCaller and redoClass.redoable:
        redoClass.redoable = False
    redoClass.redoCaller = False

    # search for the class in the system
    wantedClass = ClassSearch(classname, listOfClasses)
    if wantedClass:
        # verify the validity of the methodname
        if  checkMethName(wantedClass, methodname.title().strip()) and checkMethName(wantedClass, methtype.title().strip()):    
            
            # check if the method object already existed in the listOfMethods
            if not searchMethod(classname, methodname.strip().title()):
                
                newMethObj = MethodClass(methodname.strip(), methtype.strip())
                wantedClass.listOfMethods.append(newMethObj)
                print("Method " + methodname + " successfully added!")
                if(undoListInsertable.bool):
                    undoList.insert(0,(delMethod,(classname, methodname, methtype)))
                print(newMethObj.name)
                print("Class " + classname + "'s listOfMethods:")
                
                wantedClass.listOfMethods.sort(key = lambda x : x.name)
                for o in wantedClass.listOfMethods:
                    print(o.name)
                return "Method " + methodname + " successfully added!"

            else:
                print("Method " + methodname + " already exists! No duplicates allowed!")    
                return "Method " + methodname + " already exists! No duplicates allowed!" 
        else:
            return "Invalid method name or type! No empty inputs, no spaces, no special\n characters aside from non-leading underscores, no leading numbers, and no\n programming keywords!"
          
    else:
        print("Class " + classname + " does not exist! Enter a valid class!")
        return "Class " + classname + " does not exist! Enter a valid class!"
    

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
    if not redoClass.redoCaller and redoClass.redoable:
        redoClass.redoable = False
    redoClass.redoCaller = False

    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)
    if wantedClass:
       
        if wantedClass.listOfMethods:
            while True:
                #call searchMethod to search for the given method.
                mObj = searchMethod(classname, methodname.strip().title()) 
                
                if mObj:
                    #if mObj.name.strip() != methodname.strip().title():
                    if checkMethName(wantedClass, newmethod.strip().title()):
                            
                        mObj.name = newmethod.strip()
                        print("UML> Method " + methodname + " successfully renamed!")
                        #This adds undo functionality to the function.
                        if(undoListInsertable.bool):
                            undoList.insert(0,(renMethod,(classname, newmethod, methodname)))
                        # sort the list of method objects   
                        wantedClass.listOfMethods.sort(key = lambda x : x.name)
                        for o in wantedClass.listOfMethods:
                            print(o.name)
                        return "Method " + methodname + " successfully renamed!"
                    else:
                        return "Invalid method name! No empty inputs, no spaces, no special\n characters aside from non-leading underscores, no leading numbers, and no\n programming keywords!"                  
                else:
                    print("Method " + methodname + " not found!")
                    return "Method " + methodname + " not found!"
                break
               
        else: 
            print("No Methods found for class " + classname  + " ! Enter 'q' to exit!")
            return "No Methods found for class " + classname  + " ! Enter 'q' to exit!"
              
    else:
        print("Class " + classname + " not found! Try again!") 
        return "Class " + classname + " not found! Try again!"
         
###############################################################################              

def delMethod (classname: str, methodname: str, methtype = 0):
    from parametersModel import ParamAdd
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
    if not redoClass.redoCaller and redoClass.redoable:
        redoClass.redoable = False
    redoClass.redoCaller = False

    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)

    if wantedClass:
        #while True:
            if wantedClass.listOfMethods:
                
                    while True:
                        # call searchMethod to search for the specified method.
                        if searchMethod( classname, methodname):   
                            for o in wantedClass.listOfMethods:
                                if o.name.strip().title() == methodname.strip().title():
                                    if(undoListInsertable.bool):
                                        reverseList = list()
                                        for p in o.listOfParams:
                                            reverseList.insert(0,(ParamAdd,(classname, methodname, p.name, p.type))) 
                                        reverseList.insert(0,(addMethod,(classname, methodname, o.type)))
                                        undoList.insert(0,reverseList)
                                    wantedClass.listOfMethods.remove(o)
                                    print("UML> Method " + methodname + " of class " + classname + " deleted!")

                                    # remove the parameter list of the method.
                                    if o.listOfParams: 
                                        o.listOfParams.clear()
                                        print("Parameter(s) deleted!")
                            
                                    # sort & print the list of method objects
                                    wantedClass.listOfMethods.sort(key = lambda x : x.name)
                                    for o in wantedClass.listOfMethods:
                                        print(o.name)
                                    
                                    return "Method " + methodname + " and parameter(s) of class " + classname + " deleted!"
                                
                            break    
                           
                        # If user enters ALL/all to remove all methods.
                        else:
                            if methodname.casefold().strip() == 'all':
                                """
                                Following if statement allows us to undo all 
                                the method deletions at once.
                                """
                                if(undoListInsertable.bool):
                                    oldListOfMethods = list(wantedClass.listOfMethods)
                                    reverseList = list()
                                    
                                    for everyMethod in oldListOfMethods:
                                        """
                                        Following for loop is to regain all the 
                                        parameters attached to each of the 
                                        methods deleted.
                                        """
                                        for everyParam in everyMethod.listOfParams:
                                            reverseList.insert(0,(ParamAdd,(classname, everyMethod.name, everyParam.name, everyParam.type)))
                                        reverseList.insert(0,(addMethod,(classname, everyMethod.name, everyMethod.type)))
                                    undoList.insert(0,reverseList)
                                wantedClass.listOfMethods.clear()
                                print("All methods of " + classname +" successfully" 
                                + " deleted! Enter 'q' to exit!")
                   
                                # remove the parameter lists of the methods.
                                for o in wantedClass.listOfMethods:
                                    for p in o.listOfParams:
                                        o.listOfParams.clear()
                                        print("All parameters of the methods deleted!")
                                    
                                # sort & print the list of method objects
                                wantedClass.listOfMethods.sort(key = lambda x : x.name)
                                for o in wantedClass.listOfMethods:
                                    print(o.name)
                                return "All methods and parameter(s) of " + classname + " successfully" + " deleted!"
                            else:
                                print("Method " + methodname + " not found! Try again!")
                                return "Method " + methodname + " not found! Try again!"
                    
                        break 
                        
            else: 
                print("No methods for class " + classname  + "! Enter 'q' to exit!")
                return "No methods for class " + classname + "!"
                
                
###############################################################################              

def delParam (classname: str, methodname: str, paramname: str):
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
    from parametersModel import ParamAdd

    if not redoClass.redoCaller and redoClass.redoable:
        redoClass.redoable = False
    redoClass.redoCaller = False

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
                            if(o.name.strip().lower() == paramname.strip().lower() and o.name.strip().lower() != 'all'):
                                if(undoListInsertable.bool):
                                    undoList.insert(0,(ParamAdd,(classname,methodname, paramname, wantedParam.type)))
                                wantedMethod.listOfParams.remove(o)
                                print("UML> Parameter " + paramname + " of class " + classname + " deleted!")
                            
                                # sort & print the list of param objects
                                wantedMethod.listOfParams.sort(key = lambda x : x.name)
                                for o in wantedMethod.listOfParams:
                                    print(o.name)
                                return "Parameter " + paramname + " of class " + classname + " deleted!"        
                                
                            # If user enters ALL/all to remove all methods.
                    else:
                        if paramname.casefold().strip() == 'all':
                            if(undoListInsertable.bool):
                                reverseList = list()
                                oldParamList = list(wantedMethod.listOfParams)
                                for everyParam in oldParamList:    
                                    reverseList.insert(0,(ParamAdd,(classname,methodname, everyParam.name, wantedParam.type)))
                                undoList.insert(0,reverseList)
                            wantedMethod.listOfParams.clear()
                            print("All parameters of " + classname +" successfully" 
                                    + " deleted! Enter 'q' to exit!")
                            
                                   
                            # sort & print the list of param objects
                            wantedMethod.listOfParams.sort(key = lambda x : x.name)
                            for o in wantedMethod.listOfParams:
                                print(o.name)
                            return "All parameters of " + classname + " successfully deleted!"
                        else:
                            print("Parameter " + paramname + " not found!")
                            return "Parameter " + paramname + " not found!"
                else:
                    print("Method " + methodname + " not found! Try again!")
                    return "Method " + methodname + " not found! Try again!"
                                                         
            else: 
                print("No methods for class " + classname  + "! Enter 'q' to exit!")
                return "No methods for class " + classname  + "!"
               
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
    
    if not redoClass.redoCaller and redoClass.redoable:
        redoClass.redoable = False
    redoClass.redoCaller = False

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
                            thisParam = searchParam(thisMeth, param)
                            if thisParam:
                                if thisParam.name.strip().lower() == param.strip().lower():    
                                    if checkParamName(thisMeth, newname.strip().casefold()):
                                        if(undoListInsertable.bool):
                                            undoList.insert(0,(renameParam,(classname,methodname,newname,param)))
                                        thisParam.name = newname
                                        print("UML> Parameter "+ param +" successfully renamed!")
                                    for o in thisMeth.listOfParams:
                                        print(o.name)
                                        
                                    return "Parameter "+ param +" successfully renamed!"
                                                                      
                            else:
                                print("Parameter " + param + " not found! Try again!")
                                return "Parameter " + param + " not found! Try again!"
                        
                        else: 
                            print("No parameters for method " + methodname  + "! Enter 'q' to exit!")
                            return "No parameters for method " + methodname  + "!"
                                                    
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
    
    The function checkName verifies the validity of a field's name and its type
    input by user by checking whether it is blank, non-alphanumeric, 
    reserved keyword, or preceded by an special character(s), an integer(s),
    or non-existing within a class prior to adding the identifier 
    in the system. 
    
    It prompts user if multi-word field name with spaces entered.

    """
    
    if not name.strip() :  
        print("UML> name and type cannot be blank!")
        return False
            
    #elif len(name.strip()) < 2 or len(name.strip()) > 16:
    #    print("UML> Attribute must be 3-15 characters long!")
            
    elif regex.search(name.strip()) != None:
        print("UML> No special characters allowed!")
        return False
            
    elif name[:1].strip().isnumeric(): 
        print("UML> Field Name and/or its type cannot be preceded by an integer(s)!")
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
     
    else:
        for o in wantedClass.listOfFields:
            if o.name.casefold().strip() == name.casefold().strip():
                print("UML> No duplicates allowed! field(s) must be unique!")
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

    elif match.search(name.strip().title()) != None:
        print("UML> No space allowed! Use an underscore!")
        return False
    
    else:
        for o in wantedClass.listOfMethods:
            if o.name.title().strip() == name.title().strip():
                print("UML> No duplicates allowed! Method(s) must be unique!")
                return False
        
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
    
    else: 
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
    
    else: 
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





