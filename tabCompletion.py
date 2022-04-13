# Project Name  : UML_BootSnake
# File Name     : tabCompletion.py
# Course        : CSCI 420
# Professor     : Dr. Stephanie Schwartz
# BootSnake Team: Amelia S., Andy P., Ben M., Tram T., Travis Z.


###############################################################################

import sys
from sys import exit
import cmd




from pydoc import classname
from classModel import *
from relationshipsModel import *
from attributesModel import *
from parametersModel import *
from interfaceView import *
from saveLoadModel import *
from bootsnake import *
from undoRedoModel import *
from sharedItems import *




######################################################################################

"""
    Cmd creates line-oriented command processors [interactive shells and other 
    command interpreters] using 'readline' for interactive prompt handling,
    command line editing, and command completion.
    
    Cmd uses a loop to read all lines from its input, parse them, and dispatch
    the command to an appropriate command handler. When the user, for instance,
    enter a command 'foo bar', the program's class includes a method named 
    do_foo() and this method is called with 'bar' as its only argument.
    
    Without the comment section entered below each do_ method, these commands
    will be shown as undocumented when typing 'help'.
    
        SYNTAX
            
            help           -> a built-in command with no argument, listing all
                              available commands in the system.
            
            help <command> -> display a specific help for the specified command.
            
            <tab> <tab>    -> same as the built-in help, listing all available
                              commands in the system.
                              
            exit           -> quit the program.
        
        REFERENCE:          http://pymotw.com/2/cmd/
    
    To run the tab completion on Windows, 
        install:python -m pip install pyreadline ==> It does not work.
        uninstall pyreadline (py -3 -m pip uninstall pyreadline).
        
    """
    

# a List of valid commands that are tab-completed.

cmmands = ['addclass', 'delclass', 'renameclass',
           'addrel', 'delrel','editrel',
           'addfield', 'delfield','renamefield',
           'addmethod', 'delmethod', 'renamemethod',
           'addparam', 'delparam', 'renameparam','changeparam',
           'listclass', 'listrel',
           'save', 'load',
           'undo', 'redo',
           'help',
           'exit',
          ]

classNames = []

<<<<<<< HEAD
methodName = []

paramName = []
=======
methodNames = []

fieldNames =[]

paramNames = []
>>>>>>> attributes

# verify the number of arguments, if any, provided by the user for each given
# command in the system.
def checkArgs(argNum: int, argInput: int) -> None:
    if not argNum == argInput:
        print("Invalid argument number! Expected arg(s): "+ str(argNum) + 
                 ". Received  "+ str(argInput) +
                 ". Type 'help' to display all commands' guide or 'help <command> for a specific guide!")
    for o in listOfClasses:
        classNames.append(o.name)
        for m in o.listOfMethods:
<<<<<<< HEAD
            methodName.append(m.name)
        #paramName = o.listOfParams.copy()
=======
            methodNames.append(m.name)
            for p in m.listOfParams:
                paramNames.append(p.name)
        
    for o in listOfClasses:
        for f in o.listOfFields:
            fieldNames.append(f.name)
>>>>>>> attributes
        


class TabCompletion(cmd.Cmd):
    
    intro = ("""
                    =========================================================                                               
                    |                 WELCOME TO BOOTSNAKE!                 |                                              
                    =========================================================
                        'help' command displays all available commands
                            'exit' command quits the BootSnake program            
       
        """)
    
    doc_header = 'doc_header'
    misc_header = 'misc_header'
    undoc_header = 'undoc_header'
    
    ruler = '-'
    
    prompt = ("UML>: ")
  
    '''
    def do_greet(self, person):
        """greet [person]
        Greet the named person"""
        if person:
            print ("hi,", person)
        else:
            print ('hi')
    
    '''
    
    
    
    # class
    def do_addclass(self, arg: str):
        
        """
        COMMAND:
                addclass
        
        SYNTAX: 
                addclass <class name>
                
        DESCRIPTION:
                Add a new class to the system provided that the classname is 
                valid and unique in the system. 
        
        """
        
        arglist = arg.split()
        if(len(arglist)) == 1:
                ClassAdd(arglist[0])
        
        checkArgs(1, len(arglist))
        
    
    def do_delclass(self, arg: str):
        
        """
        COMMAND:
                delclass
        
        SYNTAX: 
                delclass <class name>
                
        DESCRIPTION:
                Delete a class in the system provided that the classname must
                exist in the system. When a class is deleted, its attributes
                and relationships, if any, are also removed. 
        
        """
        
        arglist = arg.split()
        if(len(arglist)) == 1:
            ClassDelete(arglist[0])
        
        checkArgs(1, len(arglist))
        
    
    def do_renameclass(self, arg: str):
        
        """
        COMMAND:
                renameclass
        
        SYNTAX: 
                renameclass <class name> <new name>
                
        DESCRIPTION:
                Rename an existing class in the system provided that the 
                classname must be valid and unique in the system. When renamed,
                the class' attributes and relationships, if any, remain 
                associated with the class' new name. 
        
        """
        arglist = arg.split()
        if (len(arglist)) == 2:
            classname: str = arglist[0]
            newname: str = arglist[1]
            ClassRename(classname, newname)
            
        checkArgs(2, len(arglist)) 
        
        
        
    # attributes
    def do_addfield(self, arg: str):
        
        """
        COMMAND:
                addfield
        
        SYNTAX: 
                addfield <class name> <fieldname> <fieldtype>
                
        DESCRIPTION:
                Add a new field to a given class provided that the class exists 
                and the fieldname is valid and unique in the system.
        
        """
        arglist = arg.split()
        if (len(arglist)) == 3:
            classname:str = arglist[0]
            fieldname:str = arglist[1]
            fieldtype:str = arglist[2]
            
            addField(classname, fieldname, fieldtype)
            
        checkArgs(3, len(arglist))   
            
    def do_delfield(self, arg: str):
        
        """
        COMMAND:
                delfield
        
        SYNTAX: 
                delfield <class name> <fieldname> 
                
        DESCRIPTION:
                Delete a field from a given class provided that both the class 
                and the field exist in the sytem, and particularly, the field 
                must be in the specified class.
        
        """
        arglist = arg.split()
        if (len(arglist)) == 2:
            classname: str = arglist[0]
            fieldname: str = arglist[1]
            delField(classname, fieldname)
        
        checkArgs(2, len(arglist))
            
            
           
    def do_renamefield(self, arg: str):
        
        """
        COMMAND:
                renamefield
        
        SYNTAX: 
                renamefield <class name> <fieldname> <newname>
                
        DESCRIPTION:
                Rename an existing field from a given class provided that the class
                exists in the sytem, AND particularly, the field must be in the 
                specified class.The field's new name must also be valid and unique 
                in the given class.
        
        """
        
        arglist = arg.split()
        if (len(arglist)) == 3:
            classname: str = arglist[0]
            fieldname: str = arglist[1]
            newname: str = arglist[2]
            renField(classname, fieldname, newname)
            
        checkArgs(3, len(arglist))        
    
    
    # methods        
    def do_addmethod(self, arg: str):
        
        """
        COMMAND:
                addmethod
        
        SYNTAX: 
                addmethod <class name> <methodname> <method returntype>
                
        DESCRIPTION:
                Add a new method to a given class provided that the class must 
                exist in the system AND the method's identifier and/or its  
                return-type must be unique in the class.
        
        """
        arglist = arg.split()
        if (len(arglist)) >=3:
            classname: str = arglist[0]
            methodname: str = arglist[1]
            returntype: str = arglist[2]
            paramlist: list = []
            
            addMethod(classname, methodname, returntype, paramlist)
            
        checkArgs(3, len(arglist)) 
                
    def do_renamemethod(self, arg: str):
        
        """
        COMMAND:
                renamemethod
        
        SYNTAX: 
                renamemethod <class name> <methodname> <newname>
                
        DESCRIPTION:
                Rename an existing method in a given class provided that the 
                class must exist in the system AND the method must be in the
                specified class. The method's new name must also be valid and
                unique in the class.
        
        """
        
        arglist = arg.split()
        if (len(arglist)) == 3:
            classname: str = arglist[0]
            methodname: str = arglist[1]
            #methodtype: str = arglist[2]
            newname: str = arglist[2]
            
            renMethod(classname, methodname, newname)
            
        checkArgs(3, len(arglist)) 
        
    
    
    
    def do_delmethod(self, arg: str):
        
        """
        COMMAND:
                delmethod
        
        SYNTAX: 
                delmethod <class name> <methodname> 
                
        DESCRIPTION:
                Delete an existing method from a given class provided that the 
                class must exist in the system AND the method and/or its 
                return-type must be in the specified class.
        
        """
        arglist = arg.split()
        if (len(arglist)) == 2:
            classname: str = arglist[0]
            methodname: str = arglist[1]
            #methodtype: str = arglist[2]
            
            delMethod(classname, methodname)
            
        checkArgs(2, len(arglist)) 
        
    
    
    # parameters
    def do_addparam(self, arg: str):
        
        """
        COMMAND:
                addparam
        
        SYNTAX: 
                addparam <class name> <methodname> <param name> <param type>
                
        DESCRIPTION:
                Add a new parameter to a given method of a class provided that both the 
                class AND the method must exist in the system. The method must also be 
                in the specified class and the parameter's name is valid.
        
        """
        
        arglist = arg.split()
        if (len(arglist)) == 4:
            classname: str = arglist[0]
            methodname: str = arglist[1]
            #methodtype: str = arglist[2]
            paramname: str = arglist[2]
            paramtype: str = arglist[3]
            
            ParamAdd(classname, methodname, paramname, paramtype)
            
        checkArgs(4, len(arglist))
        
    def do_delparam(self, arg: str):
        
        """
        COMMAND:
                delparam
        
        SYNTAX: 
                delparam <class name> <methodname> <param name> 
                
        DESCRIPTION:
                Delete a parameter from a given method of a class provided that
                both the class AND the method must exist in the system. The method
                must also be in the specified class and contain the specified
                parameter.
        
        """
        
        arglist = arg.split()
        if (len(arglist)) == 3:
            classname: str = arglist[0]
            methodname: str = arglist[1]
            #methodtype: str = arglist[2]
            paramname: str = arglist[2]
            
            delParam(classname, methodname, paramname)
        
        checkArgs(3, len(arglist)) 
        
               
    def do_renameparam(self, arg: str):
        
        """
        COMMAND:
                renameparam
        
        SYNTAX: 
                renameparam <class name> <methodname> <param name> <newname>
                
        DESCRIPTION:
                Rename an existing parameter in a given method of a class provided that
                both the class AND the method must exist in the system. The method
                must also be in the specified class and contain the specified parameter.
                The parameter's new name must be valid and unique.
        
        """
        
        arglist = arg.split()
        if (len(arglist)) == 4:
            classname: str = arglist[0]
            methodname: str = arglist[1]
            #methodtype: str = arglist[2]
            paramname: str = arglist[2]
            newname: str = arglist[3]
            
            renameParam(classname, methodname, paramname, newname)
            
        checkArgs(4, len(arglist))     
               
    
    # relationships
    def do_addrel(self, arg: str):
        
        """
        COMMAND:
                addrel
        
        SYNTAX: 
                addrel <source> <destination> <reltype> 
                
        DESCRIPTION:
                Add a new relationship between two classes provided that both 
                the classes must exist in the sytem AND the relationship type 
                must be one of the followings: "Aggregation", "Composition",
                "Inheritance", and "Realization". 
        
        """
        
        arglist = arg.split()
        if (len(arglist)) == 3:
            src: str = arglist[0]
            dest: str = arglist[1]
            reltype: str = arglist[2]
            
            RelationshipAdd(src, dest, reltype)
                        
        checkArgs(3, len(arglist))     
        
    
    def do_delrel(self, arg: str):
        
        """
        COMMAND:
                delrel
        
        SYNTAX: 
                delrel <source> <destination> 
                
        DESCRIPTION:
                Delete an existing relationship between two classes provided 
                that both the classes must exist in the sytem AND relation-linked. 
        
        """
        
        arglist = arg.split()
        if (len(arglist)) == 2:
            src: str = arglist[0]
            dest: str = arglist[1]
            
            RelationshipDelete(src, dest)
           
        checkArgs(2, len(arglist))     
        
    
    def do_editrel(self, arg: str):
        
        """
        COMMAND:
                editrel
        
        SYNTAX: 
                editrel <source> <destination> < reltype>
                
        DESCRIPTION:
                Modify an existing relationship between two classes provided 
                that both the classes must exist in the sytem AND relation-linked. 
        
        """
        
        arglist = arg.split()
        if (len(arglist)) == 3:
            src: str = arglist[0]
            dest: str = arglist[1]
            reltype:str = arglist[2]
            
            relationshipEdit(src, dest, reltype)
           
        checkArgs(3, len(arglist))     
        
    # list a class/classes
    def do_listclass(self, arg: str):
        
        """
        COMMAND:
                listclass
        
        SYNTAX: 
                listclass <input> 
                
        DESCRIPTION:
                List an existing class and its contents OR all existing classes 
                and their contents in the system based upon the user's selection
                of a specific class OR an input 'all'.
        
        """
        
        arglist = arg.split()
        if (len(arglist)) == 1:
            if arglist[0] == 'all':
                print(ListClasses())
            else:
                print(ListClass(arglist[0]))
           
        else:
            checkArgs(1, len(arglist))   
        
    
    
    # list relationships
    def do_listrel(self, arg: str):
        
        """
        COMMAND:
                listrel
        
        SYNTAX: 
                listrel 
                
        DESCRIPTION:
                List all existing relationships between UML classes in the 
                BootSnake system.
        
        """
        
        ListRelationships() 
            
    # save to a JSON file
    def do_save(self, arg: str):
        
        """
        COMMAND:
                save
        
        SYNTAX: 
                save <filename> 
                
        DESCRIPTION:
                Save the current work to a JSON file with a user-specified name.
        
        """
        
        arglist = arg.split()
        checkArgs(1, len(arglist))
        
    # load a JSON file   
    def do_load(self, arg: str):
        
        """
        COMMAND:
                load
        
        SYNTAX: 
                load <filename> 
                
        DESCRIPTION:
                Load the specified JSON file provided that the file must exist.
        
        """
        
        arglist = arg.split()
        checkArgs(1, len(arglist))
         
    
    
    # undo command
    def do_undo(self, arg: str = ""):
        
        """
        COMMAND:
                undo
        
        SYNTAX: 
                undo 
                
        DESCRIPTION:
                Undo/delete the last committed action, returning the current
                work to its previous state.
        
        """
        
        undo()
        
    
    # redo command
    def do_redo(self, arg: str = ""):
        
        """
        COMMAND:
                redo
        
        SYNTAX: 
                redo 
                
        DESCRIPTION:
                Redo/restore the last committed action that the user did 
                the 'undo' command.
        
        """
        print("Need to implement!")   
             
    
    # exit BootSnake program
    def do_exit(self, arg:str = ""):
        
        """
        COMMAND:
                exit
        
        SYNTAX: 
                exit 
                
        DESCRIPTION:
                Quit the BootSnake program.
        
        """
        answer: str = input("Exiting without saving? (y/n): ")
        if answer.casefold().strip() =='y':
            print("Exiting BootSnake...")
            exit()
        else:
            return
        
        
    
###############################################################################    

    """
    Once the command(s) is known, argument completion is handled by the method(s) 
    prefixed with 'complete_', allowing the programmer to assemble a list of 
    possible completions using one own's defined criteria.
    """
    def complete_addclass(self, text, line, begidx, endidx):
        if not text:
            completions = self.cmmands[:]
        else:
            completions = [f 
                           for f in self.cmmands
                           if f.startswith(text)]
        return completions
    
    
    
    def complete_delclass(self, text, line, begidx, endidx):
        if not text:
            completions = self.cmmands[:]
        else:
            completions = [f 
                           for f in classNames
                           if f.startswith(text)]
        return completions
    
    
    def complete_renameclass(self, text, line, begidx, endidx):
        if not text:
            completions = self.cmmands[:]
        else:
            completions = [f 
                           for f in classNames
                           if f.startswith(text)]
        return completions
    
    def complete_addfield(self, text, line, begidx, endidx):
        if not text:
            completions = self.cmmands[:]
        else:
            completions = [f 
                           for f in classNames
                           if f.startswith(text)]
        return completions
    
    
    def complete_delfield(self, text, line, begidx, endidx):
        
        if not text:
            completions = self.cmmands[:]
        else:
            if begidx ==9:
                completions = [f 
                           for f in classNames
                           if f.startswith(text)]   
            
            else:
                completions = [f 
                           for f in fieldNames
                           if f.startswith(text)]  
        return completions
    
    
    def complete_renamefield(self, text, line, begidx, endidx):
        
        if not text:
            completions = self.cmmands[:]
        else:
            if begidx ==9:
                completions = [f 
                           for f in classNames
                           if f.startswith(text)]
            
            else:
                completions = [f 
                           for f in fieldNames
                           if f.startswith(text)]
         
        return completions
    
    def complete_addmethod(self, text, line, begidx, endidx):
        if not text:
            completions = self.cmmands[:]
        else:
            completions = [f 
                           for f in classNames
                           if f.startswith(text)]
            
        return completions
    
    
    def complete_delmethod(self, text, line, begidx, endidx):
        
        if not text:
            completions = self.cmmands[:]
        else:
            if begidx ==10:
                completions = [f 
                           for f in classNames
                           if f.startswith(text)]
            else:
                completions = [f 
                           for f in methodNames
                           if f.startswith(text)]
        return completions
    
    def complete_renamemethod(self, text, line, begidx, endidx):
        if not text:
            completions = self.cmmands[:]
        else:
            if begidx ==10:
                completions = [f 
                           for f in classNames
                           if f.startswith(text)]
            else:
                completions = [f 
                           for f in methodNames
                           if f.startswith(text)]
        return completions
    
    def complete_addparam(self, text, line, begidx, endidx):
        
        if not text:
            completions = self.cmmands[:]
        else:
<<<<<<< HEAD
            completions = [f 
                           for f in classNames
                           if f.startswith(text)]
            if completions is not []:
                          [f 
                           for f in methodName
=======
            if begidx ==9:
                completions = [f 
                           for f in classNames
>>>>>>> attributes
                           if f.startswith(text)]
            else: 
                completions =  [f 
                           for f in methodNames
                           if f.startswith(text)]
            
        return completions
    
    
    def complete_renameparam(self, text, line, begidx, endidx):
        print(begidx, endidx)
        if not text:
            completions = self.cmmands[:]
        else:
            if begidx ==11:
                completions = [f 
                           for f in classNames
                           if f.startswith(text)]
            elif begidx ==12: 
                completions =  [f 
                           for f in methodNames
                           if f.startswith(text)]
            else: 
                completions =  [f 
                           for f in paramNames
                           if f.startswith(text)]
        return completions
    
    
    
    def complete_delparam(self, text, line, begidx, endidx):
        if not text:
            completions = self.cmmands[:]
        else:
            if begidx ==9:
                completions = [f 
                           for f in classNames
                           if f.startswith(text)]
            elif begidx ==10: 
                completions =  [f 
                           for f in methodNames
                           if f.startswith(text)]
            else: 
                completions =  [f 
                           for f in paramNames
                           if f.startswith(text)]
        return completions
    
    
    
    
    def complete_addrel(self, text, line, begidx, endidx):
        if not text:
            completions = self.cmmands[:]
        else:
            completions = [f 
                           for f in classNames
                           if f.startswith(text)]
        return completions
    
    
    def complete_delrel(self, text, line, begidx, endidx):
        if not text:
            completions = self.cmmands[:]
        else:
            completions = [f 
                           for f in classNames
                           if f.startswith(text)]
        return completions
    
    def complete_editrel(self, text, line, begidx, endidx):
        if not text:
            completions = self.cmmands[:]
        else:
            completions = [f 
                           for f in classNames
                           if f.startswith(text)]
        return completions
    
    
    def complete_listclass(self, text, line, begidx, endidx):
        if not text:
            completions = self.cmmands[:]
        else:
            completions = [f 
                           for f in classNames
                           if f.startswith(text)]
        return completions
    
    
    
    
    def complete_listrel(self, text, line, begidx, endidx):
        if not text:
            completions = self.cmmands[:]
        else:
            completions = [f 
                           for f in classNames
                           if f.startswith(text)]
        return completions
    
    
    
    def complete_save(self, text, line, begidx, endidx):
        if not text:
            completions = self.cmmands[:]
        else:
            completions = [f 
                           for f in self.cmmands
                           if f.startswith(text)]
        return completions
    
    
    
    def complete_load(self, text, line, begidx, endidx):
        if not text:
            completions = self.cmmands[:]
        else:
            completions = [f 
                           for f in self.cmmands
                           if f.startswith(text)]
        return completions
    
    
    
    
    def complete_undo(self, text, line, begidx, endidx):
        if not text:
            completions = self.cmmands[:]
        else:
            completions = [f 
                           for f in self.cmmands
                           if f.startswith(text)]
        return completions
    
    
    def complete_redo(self, text, line, begidx, endidx):
        if not text:
            completions = self.cmmands[:]
        else:
            completions = [f 
                           for f in self.cmmands
                           if f.startswith(text)]
        return completions
    
    
    def postloop(self):
        print
    
    
    
###############################################################################
if __name__ == "__main__":
   TabCompletion().cmdloop()
  
            
    