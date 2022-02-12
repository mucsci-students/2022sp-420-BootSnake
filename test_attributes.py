# Project Name  : UML BootSnake
# File Name     : test_attributes.py
# Course        : CSCI 420
# Professor     : Dr. Stephanie Schwartz
# BootSnake Team: Amelia S., Andy P., Ben M., Tram T., Travis Z.


###############################################################################

import pytest

from AClass import *
from UML_attributes import*


'''
    In order to execute pytest in Python, a virtual environment must
    be created and activated. Once the virtual environment is active,
    type the command 'pip install pytest' to install pytest.

    To run pytest, enter the command:    'python -m pytest' 
'''
 

# create a class and set listOfAttributes to empty
def makeClass(name):
    newClass = AClass(name)
    listOfAttributes = list()
    

# initialize listOfAttributes with a private attribute
listOfAttributes.append('___apple')


# test add duplicate attributes to a specific class
def test_add_duplicate():
    makeClass('classFruit')
    check_name('___apple', 'fruitClass')
    assert 'Attribute already existed!'


# test add a private attribute to a given class' list of attributes
def test_add_attr():
    makeClass('fruitClass')
    check_name('___berry ', 'fruitClass')
    listOfAttributes.append('___berry'.lower().strip())
    assert 'Attribute successfully added!'


# test special character attributes to a specific class
def test_special_characters():
    makeClass('classFruit')
    check_name('@!!!apple', 'fruitClass')
    assert 'Special characters are not allowed!'
  

# test add keyword attributes to an existing class
def test_add_keyword():
    makeClass('fruitClass')
    check_name('if', 'fruitClass')
    assert 'Keywords are not allowed!'

# test empty/blank attribute name entered by user
def test_add_blank_name():
    makeClass('fruitClass')
    check_name(' ', 'fruitClass')
    assert ' Name cannot be blank!'

# test non-existing attribute within a given class
def test_non_existing_att():
    makeClass('fruitClass')
    for e in listOfAttributes:
        if 'orange' != listOfAttributes:
            assert ' Attribute not found!'


# test rename a provided attribute within a specific class
def test_ren_attr():
    makeClass('fruitClass')
    for i in range(len(listOfAttributes)):
        if listOfAttributes[i].casefold().strip() == 'orange'.casefold().strip():
            while True:
                if (check_name('pear', 'fruitClass')):
                    listOfAttributes[i] = 'pear'.casefold()
                    assert 'Attribute successfully renamed!'
                    break
            break


# test delete an existing attribute in a specified class
def test_del_attr():
    makeClass('fruitClass')
    for i in listOfAttributes:
        if i.casefold() == 'apple'.casefold().strip():
            listOfAttributes.remove('apple'.casefold().strip())
            assert ' Attribute successfully deleted!'
            break
                            
