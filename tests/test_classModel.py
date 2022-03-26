"""
---------------------------
Last edited: 03/06/22
Editor: Andy Pham
Summary of edit:

Complete refactoring of the code to fit the new format the functions in 
classModel had. Also created test code for ClassRename and ClassDelete.

Description of program:
A test file used to test all the methods in classModel.
---------------------------
"""

#To test class methods, I have to import them all and the global class list.
from classModel import *

#This will be used to test ClassRename and how it impacts relationships.
from relationshipsModel import *

#The following 2 imports are to silence prints from AClass.
import sys
import io

#This will import the functions I'll be using to unit test
from unittest import *

#The following import is to help color code tests for ease of viewing.
from colorama import *

def test_classAdd_ValidName():
    listOfInputs = ['hi','HI','Hi','Hi1','h2o','Hello_World','Trailing__']
    print("\n\n--------------TESTING ACCEPTED CLASS ADDS--------------------")
    index = 0
    numOfFailure = 0
    while(index < len(listOfInputs)):
        print("Testing \""+ listOfInputs[index] + "\"")
        #The following two lines will suppress the text from ClassAdd()
        suppress_text = io.StringIO()
        sys.stdout = suppress_text 
        
        ClassAdd(listOfInputs[index])
        #This here will release the text so I can continue to use print().
        sys.stdout = sys.__stdout__
        result = len(listOfClasses)
        try:
            assert result == 1
            print("Class \""+listOfInputs[index]+"\" was added " + Back.GREEN + Fore.BLACK +"successfully" + Style.RESET_ALL +"!")
            listOfClasses.remove(ClassSearch(listOfInputs[index], listOfClasses))
        except:
            print("Class \""+listOfInputs[index]+"\" was " + Back.RED + Fore.BLACK + "NOT" + Style.RESET_ALL + " added successfully! Size should have changed!")
            numOfFailure = numOfFailure + 1
        index = index + 1
    return numOfFailure

def test_classAdd_InvalidName():
    print("\n\n--------------TESTING REJECTIONS--------------------")
    duplicate = AClass('duplicate')
    listOfClasses.append(duplicate)
    listOfInputs = ['duplicate','1NumberFirst','','    Spaces','Hello World','Hello~','Hello`','Hello_World!','@twitter','#Hashtag','HollarHollarGet$','Hundred%','Super^Script','D&D','*_*','I8(','I8)','__Leading','Fire-Emblem','New_Game+','=3','W[','WOh]','NO{','SDF}','SEMI;','COLON:','SINGLEQUOTE\'','DOUBLEQUOTE\"','VER|TICAL','BACKSLASH\\','C,OMMA','LESSER<','PER.IOD','>GREENTEXT','/FORWARDSLASH','QUE?','if','class','else','while','elif','def','for']
    
    index = 0
    numOfFailure = 0
    while(index < len(listOfInputs)):
        print("Testing \""+listOfInputs[index]+"\"")
        #The following two lines will suppress the text from classAdd()
        suppress_text = io.StringIO()
        sys.stdout = suppress_text
        ClassAdd(listOfInputs[index])
        #This here will release the text so I can continue to use print().
        sys.stdout = sys.__stdout__
        result = len(listOfClasses)
        #We will try the assert, if it fails we go to except.
        try:
            if result != 1:
                print("\""+listOfInputs[index]+"\" was rejected "+ Back.GREEN + Fore.BLACK + "successfully" + Style.RESET_ALL + "!")
        except:
            print("\""+listOfInputs[index]+"\" was " + Back.RED + Fore.BLACK + "NOT" + Style.RESET_ALL +" rejected!")
            listOfClasses.remove(ClassSearch(listOfInputs[index], listOfClasses))
            numOfFailure = numOfFailure + 1
        index = index + 1
    listOfClasses.remove(duplicate)
    return numOfFailure

def test_classRename_validRename():
    print("Rename Test - Due to rename sharing the name checker function \nwith ClassAdd(), it stands to reason that we do not need to \ncheck name validity and instead check only if it can rename and \nchange the appropriate listOfRelationships to match the new name.")
    
    print("Running test on 2 classes titled \"class1\" and \"class2\" respectively. \nclass1 has a relationship with class2.")
    
    class1 = AClass("class1")
    class2 = AClass("class2")
    listOfClasses.append(class1)
    listOfClasses.append(class2)
    relation = relationship("Aggregation", class2.name)
    listOfClasses[0].listOfRelationships.append(relation)
    print("\nTesting if class2 can be renamed into RenamedClass2 and if class1's \nrelationship destination name changes to reflect that.\n")
    
    #The following two lines will suppress the text from classAdd()
    suppress_text = io.StringIO()
    sys.stdout = suppress_text
    ClassRename("class2","RenamedClass2")
    
    #This here will release the text so I can continue to use print().
    sys.stdout = sys.__stdout__
    result1 = listOfClasses[1].name
    result2 = listOfClasses[0].listOfRelationships[0].dest
    try:
        assert result1 == 'RenamedClass2'
        print("\'class2\' was "+Back.GREEN+Fore.BLACK+"successfully"+Style.RESET_ALL+" renamed to be \'RenamedClass2\'!")
        try:
            assert result2 == 'RenamedClass2'
            print("class1's relationship destination was "+Back.GREEN+Fore.BLACK+"successfully"+Style.RESET_ALL+" renamed to be \'RenamedClass2\'!")
        except:
            print("class1's relationship destination was "+Back.RED+Fore.BLACK+"NOT"+Style.RESET_ALL+" successfully renamed to be \'RenamedClass2\'!")
    except:
        print("\'class2\' was "+Back.RED+Fore.BLACK+"NOT"+Style.RESET_ALL+" renamed to be \'RenamedClass2\'!")
    listOfClasses.clear()

def test_classDelete_validDelete():
    print("Running test on listOfClasses when it only has 1 class, titled \"dontDeleteMePlz\"")
    class1 = AClass("dontDeleteMePlz")
    listOfClasses.append(class1)
    #The following two lines will suppress the text from classAdd()
    suppress_text = io.StringIO()
    sys.stdout = suppress_text
    ClassDelete("dontDeleteMePlz")
    #This here will release the text so I can continue to use print().
    sys.stdout = sys.__stdout__
    try:
        assert len(listOfClasses) == 0
        print("ClassDelete "+Back.GREEN+Fore.BLACK+"successfully"+Style.RESET_ALL+" deleted the requested delete target.")
    except:
        print("ClassDelete did "+Back.RED+Fore.BLACK+"NOT"+Style.RESET_ALL+" delete the requested delete target.")
    
#input("Press enter to run tests on ClassAdd...\n")
totalNumOfFailure = test_classAdd_ValidName()
totalNumOfFailure += test_classAdd_InvalidName()
if(totalNumOfFailure == 0):
    print("\n\n---------------------------------\nAll tests for ClassAdd ran "+ Back.YELLOW + Fore.BLACK + "successfully" + Style.RESET_ALL + "!")
else:
    print("\n\n---------------------------------\n"+Back.RED + Fore.BLACK + "NOT" + Style.RESET_ALL + " all tests for ClassAdd ran successfully.\n\nTests failed: " + str(totalNumOfFailure))
#input("Press enter to run a test on ClassRename...\n")
test_classRename_validRename()
#input("Press enter to run a test on ClassDelete...\n")
test_classDelete_validDelete()


