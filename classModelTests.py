"""
---------------------------
Last edited: 02/13/22
Editor: Andy Pham
Summary of edit:

Tried making tests for ClassRename. Ran into some complications due
to having to manually enter classes and mock inputting. Currently
only tests ClassAdd()

Description of program:
A test file used to test all the methods in AClass with assertions.
---------------------------
"""

#To test class methods, I have to import them all and the global class list.
from classModelController import *

#The following 2 imports are to silence prints from AClass.
import sys
import io

#The following import is to help color code tests for ease of viewing.
from colorama import *

#I use the following to mock user inputs and test AClass.
from unittest import mock
from unittest import TestCase

"""
This tests the valid types of inputs for ClassAdd.
"""
class mockClassAdd_Valid_Name(TestCase):
    @mock.patch('AClass.input', create=True)
    def Valid_ClassAdd_Test(self, mocked_input):
        print("\n\n--------------TESTING ACCEPTED CLASS ADDS--------------------")
        listOfInputs = ['hi','HI','Hi','Hi1','h2o','Hello_World','Trailing__']
        mocked_input.side_effect = ['hi','HI','Hi','Hi1','h2o','Hello_World','Trailing__']
        index = 0
        numOfFailure = 0
        while(index < len(listOfInputs)):
            print("Testing \"hi\"")
        
            #The following two lines will suppress the text from ClassAdd()
            suppress_text = io.StringIO()
            sys.stdout = suppress_text 
            
            ClassAdd()
            
            #This here will release the text so I can continue to use print().
            sys.stdout = sys.__stdout__
            
            result = len(listOfClasses)
            try:
                self.assertEqual(result, 1)
                print("Class \""+listOfInputs[index]+"\" was added " + Back.GREEN + Fore.BLACK +"successfully" + Style.RESET_ALL +"!")
                """
                By removing the added input, I can then if all the other inputs 
                were added correctly. Otherwise, I will see EVERY test 
                afterwards marked as not being added.
                """
                listOfClasses.remove(ClassSearch(listOfInputs[index], listOfClasses))
            except:
                print("Class \""+listOfInputs[index]+"\" was " + Back.RED + Fore.BLACK + "NOT" + Style.RESET_ALL + " added successfully! Size should have changed!")
                numOfFailure = numOfFailure + 1
            index = index + 1
        return numOfFailure
    
    
"""
This tests the invalid types of inputs for ClassAdd.
"""
class mockClassAdd_Invalid_Name(TestCase):
    @mock.patch('AClass.input', create=True)
    def Bad_ClassAdd_Test(self, mocked_input):
        print("\n\n--------------TESTING REJECTIONS--------------------")
        duplicate = AClass('duplicate')
        listOfClasses.append(duplicate)
        listOfInputs = ['duplicate','1NumberFirst','','    Spaces','Hello World','Hello~','Hello`','Hello_World!','@twitter','#Hashtag','HollarHollarGet$','Hundred%','Super^Script','D&D','*_*','I8(','I8)','__Leading','Fire-Emblem','New_Game+','=3','W[','WOh]','NO{','SDF}','SEMI;','COLON:','SINGLEQUOTE\'','DOUBLEQUOTE\"','VER|TICAL','BACKSLASH\\','C,OMMA','LESSER<','PER.IOD','>GREENTEXT','/FORWARDSLASH','QUE?','if','class','else','while','elif','def','for']
        mocked_input.side_effect = ['duplicate','1NumberFirst','','    Spaces','Hello World','Hello~','Hello`','Hello_World!','@twitter','#Hashtag','HollarHollarGet$','Hundred%','Super^Script','D&D','*_*','I8(','I8)','__Leading','Fire-Emblem','New_Game+','=3','W[','WOh]','NO{','SDF}','SEMI;','COLON:','SINGLEQUOTE\'','DOUBLEQUOTE\"','VER|TICAL','BACKSLASH\\','C,OMMA','LESSER<','PER.IOD','>GREENTEXT','/FORWARDSLASH','QUE?','if','class','else','while','elif','def','for']
        index = 0
        numOfFailure = 0
        while(index < len(listOfInputs)):
            print("Testing \""+listOfInputs[index]+"\"")
            #The following two lines will suppress the text from ClassRename()
            suppress_text = io.StringIO()
            sys.stdout = suppress_text
            ClassAdd()
            #This here will release the text so I can continue to use print().
            sys.stdout = sys.__stdout__
            result = len(listOfClasses)
            try:
                self.assertEqual(result, 1)
                print("\""+listOfInputs[index]+"\" was rejected "+ Back.GREEN + Fore.BLACK + "successfully" + Style.RESET_ALL + "!")
            except:
                print("\""+listOfInputs[index]+"\" was " + Back.RED + Fore.BLACK + "NOT" + Style.RESET_ALL +" rejected!")
                """
                By removing the wrongfully added input, I can then see all the 
                other wrongfully added inputs. Otherwise, I will see EVERY test 
                afterwards marked as not being rejected.
                """
                listOfClasses.remove(ClassSearch(listOfInputs[index], listOfClasses))
                numOfFailure = numOfFailure + 1
            index = index + 1
        return numOfFailure

class mockClassReName_Valid_Name(TestCase):
    @mock.patch('AClass.input', create=True)
    def Valid_Rename(self, mocked_input):
        mocked_input.side_effects = ['class3','RenamedClass3']
        print("\n\nRename Test - Due to rename sharing the name checker function \nwith ClassAdd(), it stands to reason that we do not need to \ncheck name validity and instead check only if it can rename and \nchange the appropriate listOfRelationships to match the new name.")
        
        print("\nTesting if class3 can be renamed into RenamedClass3 and if class1's relationship changes to reflect that.")
        #suppress_text = io.StringIO()
        #sys.stdout = suppress_text
        ClassRename()
        #This here will release the text so I can continue to use print().
        #sys.stdout = sys.__stdout__
        result1 = listOfClasses[2].name
        result2 = listOfClasses[0].listOfRelationships[0]
        try:
            print(result1)
            self.assertEqual(result1, 'RenamedClass3')
            print("\'class3\' was "+Back.GREEN+Fore.BLACK+"successfully"+Style.RESET_ALL+" renamed to be \'RenamedClass3\'!")
            try:
                self.assertEqual(result2, 'RenamedClass3')
                print("class1's relationship name was "+Back.GREEN+Fore.BLACK+"successfully"+Style.RESET_ALL+" renamed to be \'RenamedClass3\'!")
            except:
                print("class1's relationship name was "+Back.RED+Fore.BLACK+"NOT"+Style.RESET_ALL+" successfully renamed to be \'RenamedClass3\'!")
        except:
            print("\'class3\' was "+Back.RED+Fore.BLACK+"NOT"+Style.RESET_ALL+" renamed to be \'RenamedClass3\'!")
            
#Tests run here.
totalNumOfFailure = 0
test = mockClassAdd_Valid_Name() 
totalNumOfFailure = test.Valid_ClassAdd_Test() 
test = mockClassAdd_Invalid_Name() #Sets the test object to have different tests
totalNumOfFailure = totalNumOfFailure + test.Bad_ClassAdd_Test()      
if(totalNumOfFailure == 0):
    print("\n\n---------------------------------\nAll tests run "+ Back.YELLOW + Fore.BLACK + "successfully" + Style.RESET_ALL + "!")
else:
    print("\n\n---------------------------------\n"+Back.RED + Fore.BLACK + "NOT" + Style.RESET_ALL + " all tests run succesffuly.\n\nTests failed: " + str(totalNumOfFailure))



