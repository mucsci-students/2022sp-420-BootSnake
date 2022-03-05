"""
Last Edit: 02/09/2022
Edited by: Amelia Spanier and Ben Moran
"""

import sys



from pydoc import classname
from AClass import *
from relationships import *
from attributes import *
from parameters import *
from interface import *
from saveLoad import *

"""
Main method in which user will be redirected to the proper method based
upon input.

In Python, 3 ways to read command line args: sys.argv, getopt, argparse
modules. sys.argv is the list of commandline arguments passed to the 
Python program, where sys.argv[0] is the name of the program invoked 
and sys.argv[1] is the 1st argument passed in the program.

SYNTAX:
    import sys
    
    sys.argv[0]         -> the name of the program
    len(sys.argv)       -> number of elements including the program's name
    (len(sys.argv)-1)   -> number of elemnts excluding the program's name
    str(sys.argv)       -> argument list


"""

def Main(args: list):
    """
    Main function for the UML program
    args: list -> a list of command line arguments 
    
    """
    
    if len(args) == 2:
        # execute the program in cli
        if args[1] == "--cli":
            umlCliController()
        else: 
            print("Invalid input!")
    
        # run gui
    else:
        print("execute guiMain!")
    
def umlCliController() -> None:

    while True:
        print("""
                ==========================================
                |            WELCOME TO BOOTSNAKE!       |
                ==========================================
                
        """)
    
        print("Here are available elements:\n[1] Class\n[2] Fields\n[3] Methods")
        print("[4] Relationships\n[5] Save/Load\n[6] Lists\n[7] Help\n[8] Quit")

    
        userIn = input("\nUML:> ")       # Prompt user for input
        
        if "1" in userIn:
            while "1":
                print("Class:")
                print("[1] Add\n[2] Rename\n[3] Delete")
                userIn = input("UML:> ")
                   
                while userIn != 'q':
                    if "1" in userIn:
                        
                        name = input("Enter a Class name or q to 'quit': ")
                        while name.strip().casefold() != 'q':
                            ClassAdd(name)
                            break
                        
                        # if user enter 'q' to exit adding class, then exit
                        else:
                            break
                       
                        
                    elif "2" in userIn:
                        
                        # print a listOfClasses, if any.
                        for obj in listOfClasses:
                            print(obj.name) 
                        OldName = input("Enter a Class to rename or q to 'quit': ")
                        while OldName.strip().casefold() != 'q':
                        
                            # call ClassSearch to look for the provided class.
                            # display a list of available fields
                            classObj = ClassSearch(OldName, listOfClasses)
                            
                            if classObj:
                                # prompt users for the class to be renamed.
                                NewName = input("Enter the new name: ")
                                while NewName.strip().casefold() != 'q':
                                    ClassRename(OldName, NewName)
                                    break
                                break
                                
                            else:
                                print("There's no class named that!")
                                break
                        else:
                            break
                            

                    elif "3" in userIn:
                        
                        # print a listOfClasses, if any.
                        for obj in listOfClasses:
                            print(obj.name) 
                    
                        deleteTarget = input("Enter a Class to delete or q to 'quit': ") 
                        while deleteTarget.casefold().strip() != 'q':
                            ClassDelete(deleteTarget)
                            break
                            
                        else:
                            break
        
                # user opts out of class menu
                break        

        elif "2" in userIn:
            while 2:
                print("Fields:")
                print("[1] Add\n[2] Rename\n[3] Delete")
            
                userIn = input("UML:> ") 
                while userIn != 'q':
                    if "1" in userIn:
                        # print a listOfClasses, if any.
                        for obj in listOfClasses:
                            print(obj.name)
                        # prompt for a specific class field(s) will be added.
                        clsname = input("To which class is field(s) added? or enter q to 'quit': ")
                        while clsname.strip().casefold() != 'q':
                            wantedClass = ClassSearch(clsname, listOfClasses)
                            if wantedClass:
                                # Ask the user for a field's name.
                                fieldname = input("UML> Enter field(s) or q to 'quit': ")
                                # Start a loop that will run until user quits.
                                while fieldname.strip().casefold() != 'q':
                                    type = input("UML> Enter a field's type or 'q' to quit: ")
                                    while type != 'q':
                                        
                                        # Add fields to a list of fields, if it is valid,
                                        #  & continue untill user quits.
                                   
                                        addField(clsname, fieldname.strip(), type.strip())
                                        break
                                     
                                    break
                               
                                else:
                                    break
                            
                            else:
                                print("Class " + clsname + " not existed! Enter a valid class!")
                                break 
                        else:
                            break          

                    elif "2" in userIn:
                        # print a listOfClasses, if any.
                        for obj in listOfClasses:
                            print(obj.name)
                        
                        # prompt users for the class to which field is renamed 
                        clsname = input("To which class is field(s) renamed? or enter q to 'quit': ")
                        while clsname.strip().casefold() != 'q':

                            # call ClassSearch to look for the provided class.
                            # display a list of available fields
                            wantedClass = ClassSearch(clsname, listOfClasses) 
                            if wantedClass:
                                print( "\nField List for " + clsname + " Class: ")
                                for o in wantedClass.listOfFields:
                                    print(o.name)
                                # prompt users for the field to be renamed.
                                fieldname = input("UML> Enter field(s) to rename or q to 'quit': ")    
                                while fieldname.strip().casefold() != 'q': 
                                    # prompt user for the new field's name
                                    newname = input("UML> Enter a new name, or enter 'quit':")  
                                    while newname.strip().casefold() != 'q':
                                        renField (clsname, fieldname.strip(), newname.strip())       
                                        break
                                                
                                    break
                                
                                # allow user to continue to rename fields
                                else: 
                                    break    
                            
                            else:
                                print("Class " + clsname + " not found! Try again!")
                                break

                        else:
                           break        
                       

                    elif "3" in userIn:
                        # print a listOfClasses, if any.
                        for obj in listOfClasses:
                            print(obj.name)
                        
                        # prompt users for the class to which field is deleted 
                        clsname = input("To which class is field(s) deleted? or enter q to 'quit': ")
                        while clsname.strip().casefold() != 'q':
                            # call ClassSearch to look for the provided class.
                            # display a list of available fields
                            wantedClass = ClassSearch(clsname, listOfClasses)
                            if wantedClass:
                                
                                #display a list of available fields
                                print( "\nField List for class: " + clsname)
                                for o in wantedClass.listOfFields:
                                    print(o.name)
                                
                                # prompt users for the field' to delete or q to 'quit'
                                fieldname = input("UML> Enter a field /'All' to delete, or enter 'quit': ") 
                                
                                #if len(wantedClass.listOfFields) > 0 :  
                                while fieldname.strip().casefold() != 'q':
                                    #print(wantedClass.listOfFields) 
                                    delField (clsname, fieldname)       
                                    break
                                    #if fieldname.strip().casefold() == 'All':
                                    #    del_attr (clsname, fieldname)
                                    #    break
                                    
                                    #else:
                                        #break
                                # allow user to continue to delete fields    
                                else:
                                    #print("No fields existed for class " + clsname + "!")
                                    break
                            else: 
                                print("class " + clsname +" not existed! Enter a valid class!")
                                break 
                                     
                        # allow users to continue stay in a given class     
                        else:
                            break
                        
                # user opts out of deletion
                break
            
        elif "3" in userIn:
            while "3":
                print("Methods:")
                print("[1] Add\n[2] Rename\n[3] Delete")
                print("Parameters:")
                print("[4] Add\n[5] Delete\n[6] Change\n[7] Rename")
                userIn = input("UML:> ")
                while userIn != 'q':
                    if "1" in userIn:
                        # print a listOfClasses, if any.
                        print("list of classes: ")
                        for obj in listOfClasses:
                            print(obj.name)
                        
                        # prompt for a specific class method(s) will be added.
                        clsname = input("To which class is method(s) added? or enter q to 'quit': ")
                        while clsname.strip().casefold() != 'q':
                            # call ClassSearch to look for the provided class.
                            # display a list of available fields
                            wantedClass = ClassSearch(clsname, listOfClasses)
                            if wantedClass:
                                # prompt users for the field to be renamed.
                                methodname = input("UML> Enter a method(s) to add or q to 'quit': ")    
                                while methodname.strip().casefold() != 'q': 
                                    methtype = input("UML > Enter a method's type or 'q' to quit: ")
                                    while methtype !='q':
                                    # prompt user for the list of params 
                                    #    param = input("UML> Optional: Add a parameter(s)?, or enter 'quit': ")  
                                    #    while param.strip().casefold() != 'q':
                                    
                                        paramList = list() #an empty parameter list
                                        
                                        addMethod (clsname, methodname, methtype, paramList)
                                        break 
                                        #break
                                    break
                                
                                # let user continue adding methods.
                                else: 
                                    break
                            
                            else:
                                print("class " + clsname +" not existed! Enter a valid class!")
                                break 
                                    
                        else:
                            break
                          
                        
                    elif "2" in userIn:
                        # print a listOfClasses, if any.
                        for obj in listOfClasses:
                            print(obj.name)
                        
                        # prompt users for the class to which method is renamed 
                        clsname = input("To which class is method(s) renamed? or enter q to 'quit': ")
                        while clsname.strip().casefold() != 'q':

                            # call ClassSearch to look for the provided class.
                            # display a list of available methods
                            wantedClass = ClassSearch(clsname, listOfClasses) 
                            if wantedClass:
                                print( "\nMethod List for class " + clsname + ":")
                                for obj in wantedClass.listOfMethods:
                                    print (obj.name)

                                # prompt users for the field to be renamed.
                                methodname = input("UML> Enter Method(s) to rename or q to 'quit': ")    
                                while methodname.strip().casefold() != 'q': 
                                    # prompt user for the new method's name
                                    newmethod = input("UML> Enter a new name, or enter 'quit':")  
                                    while newmethod.strip().casefold() != 'q':
                                        renMethod (clsname, methodname, newmethod)       
                                        break
                                                
                                    break
                                
                                # allow user to continue to rename method
                                else: 
                                    break    
                            
                            else:
                                print("Class " + clsname + " not found! Try again!")
                                break

                        else:
                            break        
                        
                    elif "3" in userIn: 
                        # print a listOfClasses, if any.
                        for obj in listOfClasses:
                            print(obj.name)
                        
                        # prompt users for the class to which method is deleted 
                        clsname = input("To which class is method(s) deleted? or enter q to 'quit': ")
                        while clsname.strip().casefold() != 'q':
                            # call ClassSearch to look for the provided class.
                            # display a list of available methods
                            wantedClass = ClassSearch(clsname, listOfClasses)
                            if wantedClass:
                                
                                #display a list of available methods
                                print( "\nMethod List for class: " + clsname)
                                for obj in wantedClass.listOfMethods:
                                    print (obj.name)
                                
                                # prompt users for the method to delete or q to 'quit'
                                methname = input("UML> Enter a method " +
                                                "or 'All' to delete, or enter 'q' to 'quit': ") 
                                
                                while methname.strip().casefold() != 'q':
                                   
                                    delMethod (clsname, methname)       
                                    break
                                else:    
                                    break
                                
                                
                                # allow user to continue to delete methods    
                                #else:
                                    #print("No methods existed for class " + clsname + "!")
                                    #break
                            else: 
                                print("class " + clsname +" not existed! Enter a valid class!")
                                break 
                                     
                        # allow users to continue stay in a given class     
                        else:
                            break
                  
                    elif "4" in userIn: 
                        # print a listOfClasses, if any.
                        for obj in listOfClasses:
                            print(obj.name)
                        
                        
                        #display a list of available methods
                        print( "\nMethod List for available classes: ")
                        for obj in listOfClasses:
                            for o in obj.listOfMethods:
                                print (o.name)
                        
                        # prompt users for the class to which method is deleted 
                        clsname = input("To which class is method's parameter(s) added? or enter q to 'quit': ")
                        while clsname.strip().casefold() != 'q':
                            # call ClassSearch to look for the provided class.
                            # display a list of available methods
                            wantedClass = ClassSearch(clsname, listOfClasses)
                            if wantedClass:
                                
                                
                                # prompt users for the method to add param or q to 'quit'
                                methname = input("UML> To which method is parameter(s) added? " +
                                                "or  enter 'q' to 'quit': ") 
                               
                                while methname.strip().casefold() != 'q':
                                    wantedMethod = searchMethod(clsname, methname)
                                    if wantedMethod:
                                        paramName = input("UML> Enter a parameter(s): ")
                                        while paramName.strip().casefold() != 'q':
                                            paramType = input("UML> Enter a parameter type: ")
                                            while paramType.strip().casefold() !='q':
                                                ParamAdd(clsname, methname.title(), paramName, paramType) 
                                                break
                                            break
                                        else:
                                            break
                                
                                
                                    # allow user to continue to add parameters for the method    
                                    
                                    else:
              
                                        print("Could not find method with name " + methname +"! Please input an existing method!")
                                        break
                                
                                break    
                                
                            else: 
                                print("class " + clsname +" not existed! Enter a valid class!")
                                break 
                                     
                        # allow users to continue stay in a given class     
                        else:
                            break
                        
                    elif "5" in userIn: 
                        # print a listOfClasses, if any.
                        for obj in listOfClasses:
                            print(obj.name)
                        
                        
                        #display a list of available methods
                        print( "\nMethod List for available classes: ")
                        for obj in listOfClasses:
                            for o in obj.listOfMethods:
                                print (o.name)
                        
                        # prompt users for the class to which method is deleted 
                        clsname = input("To which class is method's parameter(s) deleted? or enter q to 'quit': ")
                        while clsname.strip().casefold() != 'q':
                            # call ClassSearch to look for the provided class.
                            # display a list of available methods
                            wantedClass = ClassSearch(clsname, listOfClasses)
                            if wantedClass:
                                
                                
                                # prompt users for the method to add param or q to 'quit'
                                methname = input("UML> To which method is parameter(s) deleted? " +
                                                "or  enter 'q' to 'quit': ") 
                               
                                while methname.strip().casefold() != 'q':
                                    wantedMethod = searchMethod(clsname, methname)
                                    if wantedMethod:
                                        paramName =''
                                        delAmnt = input("UML> Delete 'one' parameter or 'all' parameters?: ")
                                        if delAmnt == 'one':
                                            paramName = input("Which parameter do you want to delete?: ")
                                            
                                        elif (delAmnt != 'one') or (delAmnt != 'all'):
                                            break
                                            
                                        ParamDelete(wantedMethod, delAmnt, paramName)
                                        
                                    else:
              
                                        print("Could not find method with name " + methname +"! Please input an existing method!")
                                        break
                                #else:
                                break    
                                
                            else: 
                                print("class " + clsname +" not existed! Enter a valid class!")
                                break 
                                     
                        # allow users to continue stay in a given class     
                        else:
                            break


                    elif "6" in userIn: 
                        # print a listOfClasses, if any.
                        for obj in listOfClasses:
                            print(obj.name)
                        
                        
                        #display a list of available methods
                        print( "\nMethod List for available classes: ")
                        for obj in listOfClasses:
                            for o in obj.listOfMethods:
                                for x in o.listOfParams:
                                    print (o.name  + ": [" + x.name +"]")
                        
                        # prompt users for the class to which method is deleted 
                        clsname = input("To which class is method's parameter(s) changed? or enter q to 'quit': ")
                        while clsname.strip().casefold() != 'q':
                            # call ClassSearch to look for the provided class.
                            # display a list of available methods
                            wantedClass = ClassSearch(clsname, listOfClasses)
                            if wantedClass:
                                
                                
                                # prompt users for the method to add param or q to 'quit'
                                methname = input("UML> To which method is parameter(s) changed? " +
                                                "or  enter 'q' to 'quit': ") 
                               
                                while methname.strip().casefold() != 'q':
                                    wantedMethod = searchMethod(clsname, methname)
                                    if wantedMethod:
                                        # prompt users for the method to delete or q to 'quit'
                                        parname = input("UML> Enter a parameter " +
                                                "or 'All' to change, or 'q' to 'quit': ") 
                                
                                        #while 
                                        if parname.strip().casefold() != 'q':
                                   
                                            delParam (clsname, methname, parname)       
                                            
                                            #if
                                            while delParam:
                                                paramChange = input("UML> Add/enter a parameter(s) or 'q' to quit: ")
                                                while paramChange.strip().casefold() != 'q':
                                                    changeType = input("UML> Enter a parameter's type: ")
                                                    while changeType.strip().casefold() != 'q':
                                                        ParamAdd(clsname, methname.title(), paramChange, changeType) 
                                                        break
                                                    
                                                    break
                                                else:
                                                    break
                                            else:
                                                break
                                        else:
                                            break
                                                
                                        
                                    else:
              
                                        print("Could not find method with name " + methname +"! Please input an existing method!")
                                        break
                                #else:
                                break    
                                
                            else: 
                                print("class " + clsname +" not existed! Enter a valid class!")
                                break 
                                     
                        # allow users to continue stay in a given class     
                        else:
                            break
                    
                    elif "7" in userIn: 
                        # print a listOfClasses, if any.
                        
                        print( "\nList of all classes: ")
                        for obj in listOfClasses:
                            print (obj.name)
                        
                        
                        # prompt users for the class to which method is deleted 
                        clsname = input("To which class is method's parameter renamed? or enter q to 'quit': ")
                        while clsname.strip().casefold() != 'q':
                            # call ClassSearch to look for the provided class.
                            # display a list of available fields
                            wantedClass = ClassSearch(clsname, listOfClasses)
                           
                            if wantedClass:
                                #display a list of available params
                                print( "\nParameter List for all methods: ")
                                for obj in wantedClass.listOfMethods: 
                                    for x in obj.listOfParams:
                                        print (obj.name + x.name + " : " + x.type)
                                # prompt users for the method to update param or q to 'quit'
                                methname = input("UML> Which method's paramater(s) is renamed or enter 'quit': ") 
                                  
                                while methname.strip().casefold() != 'q':
                                    if wantedClass.listOfMethods:
                                        if searchMethod(clsname, methname):
                                            parname = input("UML> Enter the Parameter(s)" +
                                                    " to rename or 'q' to quit!")
                                            while parname.strip().casefold() != 'q':
                                                newparam = input("UML> Enter a new parameter's name: ")
                                                while newparam.strip().casefold() != 'q':
                                                    renameParam (clsname, methname, parname, newparam)
                                                    break
                                            
                                                break
                                            else:
                                                break
                                                       
                                        else:
                                            print("Method " + methname +" not found!. Try again!")    
                                            break
                                    else:
                                        print("No Method "  + " existed for class " + clsname + "!")
                                        break
                                
                                break 
                            else: 
                                print("class " + clsname +" not existed! Enter a valid class!")
                                break 
                                     
                        # allow users to continue stay in a given class     
                        else:
                            break
                # user opts out of Methods
                break        
                      
                        
        elif "4" in userIn:
            while 4:
                print("Relationship:")
                print("[1] Add\n[2] Delete")

                userIn = input("UML:> ")
                while userIn != 'q':
                    if "1" in userIn:
                    
                        for obj in listOfClasses:
                            print(obj.name)
                        src = input("Source class name: ")
                        while src.strip().casefold() != 'q':
                            dest = input("Destination class name: ")
                            while dest.strip().casefold() != 'q':
                                reltype = input("Relationship type: ")
                                while reltype.strip().lower() != 'q':
                                    RelationshipAdd(src, dest,reltype)
                                    break
                                
                                break
                            
                            break
                        
                        break
                    
                        
                    elif "2" in userIn:
                        for obj in listOfClasses:
                            print(obj.name)
                        src = input("Source class name: ")
                        while src.strip().casefold() != 'q':
                            dest = input("Destination class name: ")
                            while dest.strip().casefold() != 'q':
                                RelationshipDelete(src, dest)
                                break
                                
                            
                            break
                        
                        break
                        
                break
             
        elif "5" in userIn:
            print("[1] Save\n[2] Load")
            userIn = input("UML:> ")
            filename = input("Enter filename: ")
            if "1" in userIn:
                save(filename)
                continue
            elif "2" in userIn:
                load(filename)
                continue

        elif "6" in userIn:
            print("List:")
            print("[1] Class\n[2] Classes\n[3] Relationships")
            userIn = input("UML:> ")
            if "1" in userIn:
                name = input("Class name: ")
                ListClass(name)
            elif "2" in userIn:
                ListClasses()
            #continue
            elif "3" in userIn: 
                ListRelationships()
                #continue 

        elif "7" in userIn:
            Help()
            #continue
        
        elif "8" in userIn:
            Exit()

            #print()

#########################################################################################

"""
The __name__ variable has double underscores on both sides called dunder name that 
stands for double underscores.

The __name__ is a special variable in Python that assigns a different value to it
depending on how a script is executed directly or imported as a module. When importing
a module, Python executes the file associated with the module.

When running the script directly, Python sets the __name__ variable to '__main__'.

However, if a script is imported a file as a module, Python sets the module name to 
the __name__ variable

"""  

if __name__ == "__main__":
    Main(sys.argv)
    
    
    
                 





    
