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
    
 
"""
addField
Description: Adds a field(s) for a selected, existing class in the system provided that
the field is unique within the class.
Parameter(s): name of class to be added to, field's name, field's type
Return: message to indicate success or failure to add field 
    
Notes: 
    1. 'Uppercase' words will systematically convert to converted to 
        'lowercase' words.
    2. Case-insensitive when searching for field(s).
"""
def addField(classname : str, fieldname : str, fieldtype: str):

    #call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)
    
    if wantedClass:
        # validate the fieldname and fieldtype.
        if checkName(wantedClass, fieldname.strip().casefold()) and checkName(wantedClass, fieldtype.casefold().strip()):
                        
            newField = FieldClass(fieldname, fieldtype)
            wantedClass.listOfFields.append(newField)
            print("UML> Field " + fieldname + " successfully added!")
            
            wantedClass.listOfFields.sort(key = lambda x : x.name)
            for o in wantedClass.listOfFields:
                print(o.name)
            return "Field " + fieldname + " successfully added!"
                    
          
    else:
        print("Class " + classname + " does not exist! Enter a valid class!")
        return "Class " + classname + " does not exist! Enter a valid class!"
        
   

###############################################################################

"""
delField
Description: Deletes a field(s) for a given class provided that the class & the 
field exist in the system.
Parameter(s): name of class to be deleted from, name of field to be deleted
Return: message to indicate success or failure to delete field
"""
def delField (classname: str, fieldname:str):

    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)

    if wantedClass:
        
        if wantedClass.listOfFields:
                
            while True:
                if searchField(classname, fieldname):
                    for o in wantedClass.listOfFields:
                        if o.name.strip().lower() == fieldname.lower().strip():
                            wantedClass.listOfFields.remove(o)
                            
                            print("UML> Field " + fieldname +" successfully deleted!")
                            wantedClass.listOfFields.sort(key = lambda x : x.name)            
                        return "Field " + fieldname + " successfully deleted!"
                                
                    break
                            
                    # If user enters ALL/all to remove all fields.
                else:
                    if fieldname.casefold().strip() == 'all':
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

"""
renField
Description: Renames an existing field(s) for a given existing class in the
system.
Parameter(s): name of class containing field, field's current name, field's
new name
Return: message indicating success or failure to rename field
"""
def renField (classname: str, fieldname: str, newname: str):

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

"""
addMethod
Description: Adds a method(s) for a selected, existing class in the system
provided that the method has unique identifiers within the class
Parameter(s): name of class to be added to, method's name, method's type,
list of parameters
Return: message to indicate success or failure to add method

Notes: 
    1. 'Uppercase' words will systematically convert to converted to 
        'propercase' words.
    2. Case-insensitive when searching for method(s).
"""
def addMethod(classname: str, methodname: str, methtype: str,  paramlist: list()):
    
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

"""
renMethod
Description: Renames an existing method(s) for a given existing class in the
system.
Parameter(s): name of class containing method, method's current name, method's
new name
Return: message to indicate success or failure to rename method
"""
def renMethod (classname: str, methodname: str, newmethod: str):
    
    # call ClassSearch to search for the provided class in the system.
    wantedClass = ClassSearch(classname, listOfClasses)
    if wantedClass:
       
        if wantedClass.listOfMethods:
            while True:
                #call searchMethod to search for the given method.
                mObj = searchMethod(classname, methodname.strip().title()) 
                
                if mObj:
                    if mObj.name.strip() != methodname.strip().title():
                        if checkMethName(wantedClass, newmethod.strip().title()):
                                
                            mObj.name = newmethod.strip()
                            print("UML> Method " + methodname + " successfully renamed!")
                            
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

"""
delMethod
Description: Deletes a method(s) for a given class provided that the class &
the method exists in the system
Parameter(s): name of class to be deleted from, name of method to be deleted
Return: message indicating success or failure to delete method
"""
def delMethod (classname: str, methodname: str):

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
                            if o.name.strip().lower() == paramname.strip().lower():
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
                                    if checkParamName(thisMeth, newname.strip().casefold()):
                                
                                        thisParam.name = newname.lower().strip()
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

"""
checkName
Description: Verifies the validity of a field's name and its type.
Parameter(s): class expecting field addition, name to be checked for validity
Return: bool indicating whether or not given name is valid
"""
def checkName(wantedClass: str, name: str):
    
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

"""
checkMethName
Description: Verifies the validity of a method's name and its type.
Parameter(s): class expecting method addition, name to be checked for validity
Return: bool indicating whether or not given name is valid
"""
def checkMethName(wantedClass, name: str):
    
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

"""
searchMethod
Description: Searches for a method with a given name in a class
Parameter(s): name of class containing method, name of method
Return: method object with name attribute matching given name
"""
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
   
"""
searchField
Description: Searches for a field with a given name in a class
Parameter(s): name of class containing field, name of field
Return: field object with name attribute matching given name
"""
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

"""
searchParam
Description: Searches for a parameter with a given name in a method
Parameter(s): method object containing parameter, name of parameter
Return: parameter object with name attribute matching given name
"""
def searchParam( methObj: object, param: str):
    
    for x in methObj.listOfParams:
        if x.name.strip().casefold() == param.casefold().strip():
            return x
    return None
    
#########################################################################################