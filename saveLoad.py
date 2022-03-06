"""
This file is a class used to implement a save and load function by reading and writing
to JSON files 
"""

# Imports
import json
import os.path

from textwrap import indent
from classModel import *
from json import JSONEncoder
from os.path import exists



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
Save to a JSON format file, make sure to save a valid name
"""

def save (filename):

    # Search to see if filename already exists
    if os.path.exists(filename):
        print('File already exists. Overwrite? (y/n)')
        overwrite = input()
        if overwrite == 'N' or overwrite == 'n':
            print('Choose a different filename.')
            return

    # Create a list where we'll put the dictionary objects for all classes into
    myClasses = list()
    
    # Loop through classes to encode each class with its respective attributes and relationships
    with open (filename, "w") as myFile:
        for x in listOfClasses:
            # Encode each class and its contents into the format that json needs to write to and add it to the list
            # TODO: potentially fix what goes in the dictObj

            # Lists so that we can add any number needed of attributes or relationships to each class
            myFields = list()
            myMethods = list()
            myRelationships = list()

            # Step through each type of attribute and relationship and encode it so we can save it
            for y in x.listOfFields:
                fieldObj = {'name' : y.name , 'type' : y.type}
                myFields.append(fieldObj)
            
            for z in x.listOfMethods:
                methodObj = {'name' : z.name , 'return_type' : z.returnType , 'params': z.listOfParams}
                myMethods.append(methodObj)

            for c in x.listOfRelationships:
                relationshipObj = {'source' : c.source , 'destination' : c.dest , 'type' : c.type}
                myRelationships.append(relationshipObj)

            # Put together all of the lists and class name, encode it, and add it to the list
            classObj = {'class' : x.name , 'fields' : myFields , 'methods' : myMethods, 'relationships' : x.listOfRelationships}
            myClasses.append(classObj)
        
        # Writes to file
        jsonFile = json.dumps (myClasses, indent = 4, cls = ClassEncoder)
        myFile.write (jsonFile)
    return
    


"""
Load a JSON format file, only if one has already been saved
"""
def load (filename):
    if not os.path.exists(filename):
        print("File Not Found\n")
        return

    # Open the file by the filename given
    myFile = open (filename)

    # Load the data from the file
    data = json.load(myFile)
    
    # Because the data from the file is in a list, step through it
    for x in data:
        # Create an AClass object for each item in the list
        i = AClass (x['class'])
        listOfClasses.append(i)

        # Extend the lists of attributes and relationships with their respective values
        i.listOfAttributes.extend(x['attributes'])
        i.listOfRelationships.extend(x['relationships'])

    # A way to print all of the classes and their lists, for testing purposes
    """
    for y in listOfClasses:
        print (y.name)
        for a in y.listOfAttributes:
            print (a)
        for r in y.listOfRelationships:
            print (r)
    """

    myFile.close()
    return