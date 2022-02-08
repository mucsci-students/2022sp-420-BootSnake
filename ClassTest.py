"""
---------------------------
Last edited: 02/07/22
Editor: Andy Pham
Summary of edit:

Created this test file to test the class functions

Description of program:
A test file used to test all the methods in AClass with assertions.
---------------------------
"""

#To test class methods, I have to import them all and the global class list.
from msilib.schema import Class
from AClass import *

#To mock user inputs I will be importing methods from tud_test_base.
from tud_test_base import *

"""
Alternatively I think that using these imports might be better for testing. As 
tud_test_base seems to disallow prints after setting keyboard inputs.
"""
from unittest import mock
from unittest import TestCase

def testCase():
    test = input("Input \"hello\":")
    print("You inputed: " + test)

def CorrectMockInputTest():
    set_keyboard_input(["hello"])
    testCase()
    output = get_display_output()
    assert output == ["Input \"hello\":","You inputed: hello"], "You should have inputed hello."

def IncorrectMockInputTest():
    set_keyboard_input(["hi"])
    testCase()
    output = get_display_output()
    assert output == ["Input \"hello\":","You inputed: hello"]

def ClassAdd_Tud_Test_Case_1():
    set_keyboard_input(["hi"])
    ClassAdd()
    output = get_display_output()
    assert output == ["""Input a valid unique class name. 
          A valid class name is made up of alpha-numeric characters. 
          The first character must not be a number or underscore. 
          The class name should also not be a programming keyword.""","Class name: ","Class added to the list of classes. Use the list class command to display its contents."]
    
    assert len(listOfClasses) != 0,"The list length should have changed after ClassAdd was called."
    
class mockClassAdd_Valid_Name(TestCase):
    @mock.patch('AClass.input', create=True)
    def ClassAdd_Test_1(self, mocked_input):
        mocked_input.side_effect = ['hi']
        print("This test will see if a valid class name is added to the list successfully.")
        print("PRIOR TO TEST: SIZE OF LIST OF CLASSES = " + str(len(listOfClasses)))
        print("---------------STARTING TEST-------------------")
        print("TEST INPUT: hi")
        ClassAdd()
        result = len(listOfClasses)
        print("----------------END OF TEST-------------------")
        print("POST TEST: SIZE OF LIST OF CLASSES = " + str(result))
        try:
            self.assertEqual(result, 1)
            print("The length of the list has been increased successfully!")
        except:
            print("The length of the list should have changed!")
    
    def ClassAdd_Test_2(self, mocked_input):
        mocked_input.side_effect = ['hello_world']
        print("This test will see if a valid class name is added to the list successfully.")
        print("PRIOR TO TEST: SIZE OF LIST OF CLASSES = " + str(len(listOfClasses)))
        print("---------------STARTING TEST-------------------")
        print("TEST INPUT: hello_world")
        ClassAdd()
        result = len(listOfClasses)
        print("----------------END OF TEST-------------------")
        print("POST TEST: SIZE OF LIST OF CLASSES = " + str(result))
        try:
            self.assertEqual(result, 1)
            print("The length of the list has been increased successfully!")
        except:
            print("The length of the list should have changed! This function fails adding a normal class name with no numbers or underscores!")
            
        

#ClassAdd_Tud_Test_Case_1()
test = mockClassAdd_Valid_Name()
#test.ClassAdd_Test_1()
test.ClassAdd_Test_2()

