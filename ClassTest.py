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
from AClass import *

#To mock user inputs I will be importing methods from tud_test_base.
from tud_test_base import *

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

def ClassAdd_Test_Case_1():
    set_keyboard_input(["hi"])
    ClassAdd()
    output = get_display_output()
    print("PRINT MESSAGE LKJGLSDKJGLSDKJGHLSDKJGKLSDHJ" + output[0])
    
    assert len(listOfClasses) != 0,"The list length should have changed after ClassAdd was called."
    print("Test Case 1: Successful")

ClassAdd_Test_Case_1()

