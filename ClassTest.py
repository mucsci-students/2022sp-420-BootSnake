"""
---------------------------
Last edited: 02/12/22
Editor: Andy Pham
Summary of edit:

Used mock patch to create two test classes designed to loop through most valid 
and invalid types of input. I can't possibly test to see if every single kind of keyword is recognized so I can't say all invalid types of input.

Description of program:
A test file used to test all the methods in AClass with assertions.
---------------------------
"""

#To test class methods, I have to import them all and the global class list.
from AClass import *

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
        print("\n\n--------------TESTING ACCEPTIONS--------------------")
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
                print("Class \""+listOfInputs[index]+"\" was " + Back.RED + Fore.WHITE + "NOT" + Style.RESET_ALL + " added successfully! Size should have changed!")
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
            #The following two lines will suppress the text from ClassAdd()
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
                print("\""+listOfInputs[index]+"\" was " + Back.RED + Fore.WHITE + "NOT" + Style.RESET_ALL +" rejected!")
                """
                By removing the wrongfully added input, I can then see all the 
                other wrongfully added inputs. Otherwise, I will see EVERY test 
                afterwards marked as not being rejected.
                """
                listOfClasses.remove(ClassSearch(listOfInputs[index], listOfClasses))
                numOfFailure = numOfFailure + 1
            index = index + 1
        return numOfFailure


#Tests run here.
totalNumOfFailure = 0
test = mockClassAdd_Valid_Name()
totalNumOfFailure = test.Valid_ClassAdd_Test() 
test = mockClassAdd_Invalid_Name()
totalNumOfFailure = totalNumOfFailure + test.Bad_ClassAdd_Test()      
if(totalNumOfFailure == 0):
    print("\n\n---------------------------------\nAll tests run "+ Back.YELLOW + Fore.BLACK + "successfully" + Style.RESET_ALL + "!")
else:
    print("\n\n---------------------------------\n"+Back.RED + Fore.WHITE + "NOT" + Style.RESET_ALL + " all tests run succesffuly.\n\nTests failed: " + str(totalNumOfFailure))



