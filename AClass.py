"""
There are two imports for the class file (as of now).
One of the imports just saves us some coding work while the other is for 
testing purposes.

keyword: A module that has the iskeyword() function. This function is useful
         for finding if someone inputted a keyword as a class name. Which is 
         not allowed.

"""
from asyncio.windows_events import NULL
import keyword
import re
from io import StringIO


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
    listOfAttributes = list()
    listOfRelationships = list()
    

"""
The function that adds classes to the global list of classes. It does not allow for duplicates, leading numbers/underscores, or special characters. With exception to non first character underscores. It also prevents you from naming a class an empty string.
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
    
    #len() returns the size of the parameter. This checks if the name is empty.
    if len(name) == 0:
        print("You must type a name!")
    
    #keyword.iskeyword() checks to see if the parameter is a keyword.     
    elif keyword.iskeyword(name):
        print("You cannot name a class a programming keyword!")
    
    #"name[:1]" checks the first character.
    #We'll use this to check for invalid leading characters.
    elif name[:1] == "_" or name[:1].isdigit():     
        print("Underscores and numbers cannot be used for the first character!")
    
    #This checks for any special characters in the input at all.
    elif "!" or "@" or "#" or "$" or "%" or "^" or "&" or "*" or "(" or ")" or "-" or "+" or "=" or " " in name:
        print("No special characters allowed!")
    
    #The final check is to see if it's already in the list of classes.
    elif name in listOfClasses:
        print("No duplicates allowed! Every class name is unique.")
    
    #If it gets to this final else then it is a valid class name.
    else:
        newClass = AClass(name) #We create a new object with the given name.
        listOfClasses.append(newClass) #We append the object into the list.
        print("Class added to the list of classes. Use the list class command to display its contents.")

"""
    Search through class list and return given name.
"""      
def ClassSearch(name, listOfClasses):
    listLength = len(listOfClasses)
    
    if (listLength == 0):
        print("There are no classes in the list.")
        return NULL

    for x in listOfClasses:
        print(name +": was found.\n")
        return x
    
    print (name + ": was not found.\n")
    return NULL
    
    
    