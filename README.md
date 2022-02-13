# 2022sp-420-BootSnake

Team Name: BootSnake
Team Members: Andy P, Amelia S, Ben M, Tram T, Travis Z

This is the Class Branch. Here we will have the creation of all of the class 
functions before merging back into the development branch along with a test
file that at the moment can only test ClassAdd.

The class branch will be made up of 1 file revolving around a class object.

The class object is made up of 3 class attributes:

1. A name
2. A list of class attributes
3. A list of relationships with other classes

In the file there will be a global list that will be used to contain the class objects.

There are five functions within the file:

1. ClassAdd - A function that adds a class to a global list of classes.
              This function does not allow for duplicates and is particular
              about what characters are in it.
              
              A) No special characters aside from non-leading underscores
              
              B) No leading numbers
              
              C) No spaces in it at all
              
              D) No reserved programming keywords

2. ClassRename - A function that renames an existing class within the global list
                 of classes. Follows the same naming restrictions as ClassAdd.
                 The rename will result in changes within the relationship list of
                 the other class objects if they had a relationship with the renamed
                 class.

3. ClassDelete - A function that removes a class from the class list and all the 
                 relationships other classes had with it.

4. ClassSearch - A function that searches the class list for a requested class object.
                 Upon finding it, it will return the class object.
                 The primary use of this function is for other non class functions to
                 search for class objects.

5.  ClassNameChecker -  A function that is used by both ClassAdd and ClassRename to
                        check if the entered input is a valid class name. It returns
                        "None" in the case that the entered input is invalid.

ClassTest.py can be run by typing "python ClassTest.py" into the terminal. At the moment
it can only run tests on ClassAdd due to complications with how AClass is set up. 
