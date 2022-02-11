"""
---------------------------
Last edited: 02/08/22
Editor: Andy Pham and Travis Z
Summary of edit:
Created ClassDelete. It is very similar to ClassRename in how it's coded.
It searches for the object to delete, then it searches for the relationships
that also need to be deleted and deletes them both. 

---------------------------

There are two imports for the class file (as of now).

keyword: A module that has the iskeyword() function. This function is useful
         for finding if someone inputted a keyword as a class name. Which is 
         not allowed.

re: A module that will alllow me to use regexes to check for patterns or 
    special characters.

"""
import keyword
#from msilib.schema import Class
import re


#A global list that will be used to keep all the classes.
listOfClasses = list() 

""" 
The class we'll be building our objects off of. It contains a 
initialization function, "def __init__(self,name)" that assigns the name to 
the object. It also contains the two lists we'll be using to keep track of 
attributes and relationships.
"""
class AClass:
    def __init__(self,name):
        self.name = name
        self.listOfAttributes = list()
        self.listOfRelationships = list()
    
    
    
# A helper function used to check the validity of class names. 
# Returns a bool to the function that calls it.
def ClassNameChecker(name):
    """
    The following variable "regex" is a regular expression used to find if 
    there are any special characters aside from an underscore.
    
    The breakdown is "^" means if you see any characters that are not the 
    following characters then it is a match. Then I have character ranges with 
    "-" to describe all the characters from 0 to 9, from lower case a to z and 
    from uppercase A to Z and finally an underscore.
    """
    regex = r"([^0-9a-zA-Z_*]+)"
    
    """
    This returns either a match object or None. We'll use this for an if check 
    later in the code.
    """
    match = re.search(regex, name) 
    
    #len() returns the size of the parameter. This checks if the name is empty.
    if len(name) == 0:
        print("You must type a name!")
        return False
    
    #keyword.iskeyword() checks to see if the parameter is a keyword.     
    elif keyword.iskeyword(name):
        print("You cannot name a class a programming keyword!")
        return False
    
    #"name[:1]" checks the first character.
    #We'll use this to check for invalid leading characters.
    elif name[:1] == "_" or name[:1].isdigit():     
        print("Underscores and numbers cannot be used for the first character!")
        return False
    
    #This checks for any special characters in the input with the regex above.
    elif match != None:
        print("Aside from nonleading underlines, no special characters or spaces allowed!")
        return False
    
    #The final check is to see if it's already in the list of classes.
    else:
        for x in listOfClasses:
            if(name == x.name):
                print("No duplicates allowed! Every class name is unique.")
                return False
        return True
    


"""
The function that adds classes to the global list of classes. It does not allow 
for duplicates, leading numbers/underscores, or special characters. With 
exception to non first character underscores. It also prevents you from naming 
a class an empty string.
"""
def ClassAdd():
    """
    When the function is called a multi-line print detailing what is considered 
    a valid class name is displayed.
    """
    
    print("""Input a valid unique class name. 
          A valid class name is made up of alpha-numeric characters. 
          The first character must not be a number or underscore. 
          The class name should also not be a programming keyword.""")
    
    name = input("Class name: ") #The name variable that'll be ran through ifs.
    
    #If it gets to this final else then it is a valid class name.
    if(ClassNameChecker(name)):
        newClass = AClass(name) #We create a new object with the given name.
        listOfClasses.append(newClass) #We append the object into the list.
        print("Class added to the list of classes. Use the list class command to display its contents.")


#Searches through class list and return given name.    
def ClassSearch(name, listOfClasses):
    #We can use this for loop as a means to check every entry in the list for 
    #the name.
    for x in listOfClasses:
        if(x.name == name):
            return x #We then return the object for the other functions to use.
    
    #If we get to this point then that means we couldn't find the class so 
    #we'll return None.
    return None

"""
    A function used to rename classes within the global class list.
    It will also search through the list and rename any relationships to fit 
    the new name. 
"""
def ClassRename():
    # You can't rename things if there's nothing to rename.
    if(len(listOfClasses)==0):
        print("There's nothing here to rename.")
    else:
        #Asks for the rename target.
        OldName = input("Class to rename: ")
        #Grabs the object by feeding the name to the Class Search function.
        classObject = ClassSearch(OldName, listOfClasses)
        #ClassSearch returns None if it can't find it.
        if(classObject == None):
            print("There's no class named that!")
        else:
            #Asks for the new name.
            NewName = input("Enter the new name: ")
            
            """
            Checks to see if the new name is valid by feeding it into the 
            ClassNameChecker function. It returns either true or false.
            """
            if(ClassNameChecker(NewName)):
                classObject.name = NewName #renames the old name here.
        
                """
                The following nested for loops will iterate through each class 
                object in the global list. Looking through each of their 
                relationship lists for the old class name. If it finds it, it 
                removes it and adds into the relationship list the changed 
                name. We are unable to change the value of the name due to how 
                for loops presumably work. So we will have to remove and add to 
                make up for that inability to change the value directly.
                """
                for c in listOfClasses:
                    for relName in c.listOfRelationships:
                        if relName == OldName:
                            c.listOfRelationships.remove(OldName)
                            c.listOfRelationships.append(NewName)
                
                print (OldName + " has been renamed to: " + NewName + "\n")

def ClassDelete():
    # You can't delete things if there's nothing to rename.
    if(len(listOfClasses)==0):
        print("There's nothing here to delete.")
    else:
        #Asks for the class to delete.
        deleteTarget = input("Class to delete: ")
        #Grabs the object by feeding the name to the Class Search function.
        classObject = ClassSearch(deleteTarget, listOfClasses)
        #ClassSearch returns None if it can't find it.
        if(classObject == None):
            print("There's no class named that!")
        else:
            listOfClasses.remove(classObject)
            print("Class deleted!")
            """
            The following nested for loops will iterate through each class 
            object in the global list. Looking through each of their 
            relationship lists for the deleted class name. If it finds it, it 
            removes it and adds into the relationship list the changed 
            name. We are unable to change the value of the name due to how 
            for loops presumably work. So we will have to remove and add to 
            make up for that inability to change the value directly.
            """
            for c in listOfClasses:
                for relName in c.listOfRelationships:
                    if relName == deleteTarget:
                        print("Deleting " + relName + " relation")
                        c.listOfRelationships.remove(deleteTarget)


# Testing code. To be transported to ClassTest.py on a later 
# date.             
"""
class1 = AClass("class1")
class2 = AClass("class2")
class3 = AClass("class3")
listOfClasses.append(class1)
listOfClasses.append(class2)
listOfClasses.append(class3)
listOfClasses[1].listOfRelationships.append("class1")
listOfClasses[1].listOfRelationships.append("class3")
print("All classes in the list: ")
print("-------------------------")
for x in listOfClasses:
    print(x.name)
print("-------------------------")
print("\nClass2's relationships: ")
print("-------------------------")
for x in listOfClasses[1].listOfRelationships:
    print(x)
print("-------------------------")
print("\nRunning test....")
ClassDelete()
print("\n-------------------------")
print("All classes in the list: ")
print("-------------------------")
for x in listOfClasses:
    print(x.name)
print("-------------------------")
print("\nClass2's relationships: ")
print("-------------------------")
for x in listOfClasses[0].listOfRelationships:
    print(x)
print("-------------------------")
"""
