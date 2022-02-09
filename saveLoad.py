"""
This file is a class used to implement a save and load function by reading and writing
to JSON files
"""

# Imports
from textwrap import indent
from AClass import *
import json 
from json import JSONEncoder

"""
    Write a custom JSONEncoder to make class JSON serializable.
    Use JSON module's JSONEncoder class, extend it for customized
    output. This custom JSONEcoder will override the default()
    method to serialize any additional types (string, dictionary,
    lists, etc....)

    json.dumps() in Python is a method that converts dictionary objects 
    of Python into JSON string data format. It is useful when the objects
    are required to be in string format for the operations like parsing,
    printing, etc.
    syntax:
        json.dumps(object, indent = x, default [cls], sort_keys)
    json.dumps() or json.dump() method has a cls kwarg. Using the 
    "cls" kwarg, enabling passing a custom JSON encoder, which tells 
    json.dumps() or json.dump() how to encode the object into 
    JSON formatted data. This cls argument needs to be specified in
    the json.dumps(), otherwise, the default JSONEncoder is used.

    The default JSONEncoder class has a default() method that only 
    converts basic types into JSON

"""

class ClassEncoder (JSONEncoder):

    def default(self, o):
        return o.__dict__

"""
     This function takes 3 parameters to encode list of Classes,
     list of Attributes & list of Relationships int a JSON and returns a string

"""

def encoder (className: str, attList: list, relList: list):
    dictObj = { 'classes' : className , 'attributes' : attList , 'relationships' : relList}

    return json.dumps (dictObj, indent = 4, cls = ClassEncoder)

"""
Save to a JSON format file, make sure to save a valid name
"""

def save (filename: str):
    myClasses = list()

    myClasses = listOfClasses
    
    # Loop through classes to encode each class with its respective attributes and relationships
    with open (filename, "w") as myFile:
        for x in myClasses:
            # Encode each class and its contents into the format that json needs to write to
            jsonFile = encoder (x.name, x.listOfAttributes, x.listOfRelationships)
            myFile.write (jsonFile)
    


"""
Load a JSON format file, only if one has already been saved
"""
def Load ():
    return

"""
# Tests

class1 = AClass ("class1")
listOfClasses.append (class1)
class1.listOfAttributes.append ("attribute1")
class1.listOfRelationships.append ("relationship1")

class2 = AClass ("class2")
listOfClasses.append (class2)
class2.listOfAttributes.append ("attribute2")
class2.listOfRelationships.append ("relationship2")

save("test")
"""