
import re # checks if the string contains any special characters
import keyword


listOfAttributes = list()
# Define the actions for each choice.
def attr_add():
    
    # Set newAttr to something other than 'quit'.
    newAttr = ''
    # Start a loop that will run until the user enters 'quit'.
    while newAttr.strip() != 'quit':
        # Ask the user for an attribute's name.
        newAttr = input("UML> Enter an attribute, or enter 'quit': ")
        # Add the new name to list of attributes
        if newAttr.strip() != 'quit':
            # Make own character set and pass this as argument in compile method
            regex = re.compile('[@!$%^&*()<>?/\\\|}{:\[\]]')
            #if len(newAttr) == 0:    
            if not newAttr.strip() :  
                print("UML> Name cannot be blank!")
            #string is either empty, blank, or space-filled
            #elif not newAttr or re.search("^\s*$", newAttr):
                #print("UML> Name cannot be blank!")
            elif len(newAttr.strip()) > 10 or len(newAttr.strip()) < 3:
                print("UML> Attribute must be 3-10 characters long!")
            elif  (regex.search(newAttr.strip()) != None):
                print("UML> No special characters allowed for an attribute!")
            elif newAttr[:1].strip().isnumeric(): 
                print("UML> Attribute name cannot be preceded by an integer(s)!")
            #elif not re.match("^[_ a-z]+$", newAttr): 
            #    print("UML> Attribute name all must be lowercase!")
            elif newAttr[:3].strip() == "___":     
                print("UML> Leading underscores (> 2) are not allowed!")
            elif newAttr[-1].strip() == "_":     
                print("UML> Trailing underscores are not allowed!")
            elif keyword.iskeyword(newAttr.strip()):     
                print("UML> Keywords are not allowed!")
            elif newAttr.casefold().strip() in listOfAttributes:
                print("UML> No duplicates allowed! Attribute must be unique.")
            else:
                #newAttr.lower()
                listOfAttributes.append(newAttr.strip().lower())
                print("UML> Attribute added!")
    
    listOfAttributes.sort()
    print(listOfAttributes)


def display_list ():
    if not listOfAttributes:
        print("No attributes found!")
    else:
        print(listOfAttributes)

def attr_del ():
    if not listOfAttributes:
        print("No attributes found!")
    else:
        print(listOfAttributes)
        prompt =''
        while prompt.strip() != 'quit':
            prompt = input("UML> Enter an attribute to delete: ")
            if prompt.strip() != 'quit':
                for elemen in listOfAttributes:
                    if elemen.casefold() == prompt.casefold():
                        listOfAttributes.remove(prompt.casefold())
                        print("UML> Attribute deleted!")
                        break
                else: 
                    print("Attribute not found!")
            ##delete all attributes
            elif prompt.strip() == 'all':
                listOfAttributes.clear()
                break
            else:
                print(listOfAttributes)


# Give the user some context.
print("\nWelcome to the BootSnake Geeks camp. What would you like to do?")

# Set an initial value for choice other than the value for 'quit'.
command = ''

# Start a loop that runs until the user enters the value for 'quit'.
while command != 'q':
    
    # Give all the choices in a series of print statements.
    print("\n[1] Enter 1 to input attributes.")
    print("[2] Enter 2 to display a list of all attributes.")
    print("[3] Enter 3 to select an attribute to delete.")
    print("[q] Enter q to quit.")
    
    # Ask for the user's choice.
    command = input("\nUML> What would you like to do? ")

# Respond to the user's choice.
    if command == '1':
        attr_add()
    elif command == '2':
        display_list ()
    elif command == '3':
        attr_del()
    elif command == 'q':
        print("\nSee you later.\n")
    else:
        print("\nPlease try again.\n")




