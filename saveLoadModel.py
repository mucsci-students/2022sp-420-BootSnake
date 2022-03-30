"""
This file is a class used to implement a save and load function by reading and writing
to JSON files 
"""

# Imports
import json
import os.path

from textwrap import indent
from json import JSONEncoder
from os.path import exists

# Imports from other classes
from classModel import *
from relationshipsModel import *
from attributesModel import *
from parametersModel import *




"""
    Write a custom JSONEncoder to make class JSON serializable.
    Use JSON module"s JSONEncoder class, extend it for customized
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
    # Create a list where we"ll put the dictionary objects for all classes into
    myClasses = list()
    myRelations = list()
    
    # Loop through classes to encode each class with its respective attributes and relationships
    with open (filename, "w") as myFile:
        for x in listOfClasses:
            # Encode each class and its contents into the format that json needs to write to and add it to the list
            # TODO: potentially fix what goes in the dictObj

            # Lists so that we can add any number needed of attributes or relationships to each class
            myFields = list()
            myMethods = list()
            myParams = list()
            myRelationships = list()

            # Step through each type of attribute and relationship and encode it so we can save it
            for y in x.listOfFields:
                fieldObj = {"name": y.name , "type": y.type}
                myFields.append(fieldObj)
            
            # Step through the list of methods after fields
            for z in x.listOfMethods:
                # For each method, add the list of parameters
                for q in z.listOfParams:
                    paramObj = {"name": q.name , "type": q.type}
                    myParams.append(paramObj)
                methodObj = {"name" : z.name , "return_type": z.type , "params": myParams}
                myMethods.append(methodObj)

            for c in x.listOfRelationships:
                relationshipObj = {"source": x.name , "destination": c.dest , "type": c.type}
                myRelations.append(relationshipObj)

            # Put together all of the lists and class name, encode it, and add it to the list
            classObj = {"name": x.name , "fields": myFields , "methods": myMethods}
            myClasses.append(classObj)
        
        # Put classes and relationships together
        globalDict = {"classes": myClasses , "relationships": myRelations}

        # Writes to file
        jsonFile = json.dumps (globalDict, indent = 2, cls = ClassEncoder)
        myFile.write (jsonFile)
    return
    
 

"""
Load a JSON format file, only if one has already been saved
"""
def load (filename):
    # Open the file by the filename given
    myFile = open (filename)

    # Load the data from the file
    data = json.load(myFile)
    
    # Get list of classes
    classList = data["classes"]
    # Because the data from the file is in a list, step through it
    for x in classList:
        # Create an AClass object for each item in the list
        i = AClass (x["name"])
        listOfClasses.append(i)

        # Create list for fields, and then step through the list and add each of them to the class
        fieldList = x["fields"]
        for y in fieldList:
            addField(x["name"], y["name"], y["type"])

        # Create list for methods
        methodList = x["methods"]
        for z in methodList:
            paramList = list() #an empty parameter list
            addMethod(x["name"], z["name"], z["return_type"], paramList)
            # List for parameters
            paramList = z["params"]
            for q in paramList:
                ParamAdd(x["name"], z["name"], q["name"], q["type"])

    # Get list of relationships
    relationList = data["relationships"]
    for r in relationList:
        RelationshipAdd(r["source"], r["destination"], r["type"])

    myFile.close()
    return