# BootSnake UML Editor
    Team Members: Andy P, Amelia S, Ben M, Tram T, Travis Z
    
# Steps to run the editor
1. Download the most recent version of Python (Python3 is required for the GUI)

2. Download the files              
              
              A) Click "Code" dropdown box
              
              B) Click "Download ZIP"
              
3. Extract the ZIP
              
              A) Open File Explorer
              
              B) Right Click ZIP folder named: "2022sp-420-BootSnake-develop
              
              C) Extract all and choose where you want the folder
4. Open terminal and navigate to folder

5. Run
              To use PIL import, run the command pip install Pillow as PIL is 
              deprecated and pillow is the successor
              
              A) python bootsnake.py or python .\bootsnake.py depending on your editor
              
              B) By default it runs in GUI mode, to run in command line interface add --cli 
                 (python bootsnake.py --cli)
            
              Notes:
                 On Linux, run the gui with "python3 interfaceGUI.py" and the CLI with "python bootsnake.py" or python3


#  Design Patterns
1. Iterator: Our ClassSearch method iterates through a list of AClass objects to find the class of the given name.
   (Location: classModel.py 146)

2. Facade: The AClass object is a facade that contains subsystems of methods, fields, and relationships.
   (Location: classModel.py 34)

3. Command: Our GUI uses buttons that are linked to commands.
   (Location: interfaceGUIView.py 240)

4. Observer: When a class is renamed, all relationships dependent on the given class are made to set its old name to match 
   the new name.
   (Location: classModel.py 164)
