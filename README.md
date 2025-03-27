Emulator File Manager

A Desktop Application made in Python to keep track of emulator files and to launch emulators from 

Not Tested On Linux or Mac

Made at the request of a friend

Features
- One Click Directory Scanner to set all Emulator Files paths
- One place to launch all emulators executables
- One Click File Extractor into the Chosen Emulator Game Folder
- Saves Emulator executables and Emulator Game file paths 

Install:
- Download from releases on the right-hand side
- Extract zip file
- Executable Location: dist->main->Emulator_File_Manager (Double Click To Launch)

Usage Manual:
- Find Emulators - Is a one-click button that will scan through your computer and find the emulator .exe file path (may take a few minutes) (may also find the incorrect .exe file)
- Select a Folder Button - Allows you to manually set the file location of the chosen emulators '.exe'.
- Opening an Emulator - To open an emulator from the application, press "Launch" on the right-hand side to open the corresponding emulator
- Setting Game File - Allows you to manually set the location of the corresponding emulators game/rom folder (meant to be used with the File Extract, read further for instruction usage)
- File Extraction - To the right of "Zip/Rar/7z Location" is a button that will by default say "C://". Click on "C://" then find the file you wish to extract. To the right of "Select Emulator" is a drop-down menu to pick the corresponding emulator game/rom folder you wish to extract to. Make sure to set your emulators game folder (see previous instruction). To extract the file, click on the "Extract" button; this will create a new folder with the name of the extracted file within the corresponding game folder; within the new folder will be the extracted contents of the file and the original file.  
- Enjoy!


Notes:
- Sometimes it the find emulator button will find the wrong .exe file, manually adjust will be needed
- Some .exe's will not launch because of specific visual studio packages not being installed on the users computer (Will look into a different file extraction library) 
