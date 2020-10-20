# Quick-CSharp-Setup-VScode
**Short description**

The purpose of this short script is to allow the user to quickly set up a C# project for VScode, complete with a solution file, and folders for the main project and for classes and tests.

The script asks for input to the user. It asks for a directory in which a container folder will be created. That folder will contain another two folders, one for the main C# script and one for classes. The solution file (.sln) is also contained in that folder. References are added.

Test files are also added and linked, and the user may choose to create any amount of class files.

This is primarily meant for people who wish to use C# with Visual Studio Code and not Visual Studio. Of course, this code is not REALLY exclusive to VScode, only the last line of the script, which opens the app.

You will see the instructions once you run the script.

**Requisites:**

  .The user must have Python 3 installed.
  
  .The user must have VScode installed. (Not really)
  
  .The user must have .NET installed.
  
  .Windows only.
  
  .Python libraries: shutil, subprocess, os.

Download Python (You may use Anaconda if you wish), then open the command line and type "pip install os" then "pip install shutil" and then "pip install subprocess"
To run the script, open your cmd. then go to the directory where the script is located using CD. then type python "C# maker.py".

Do let me know if you have any suggestions! 

**TIPS:**

  .Avoid naming the classes folder "class"
  
  .As soon as VSCode opens, a window will pop up on the bottom right. Accept it so that you run and debug.
  
  .Be careful when choosing your directory, since typos will not throw an error.
  
  **.READ THE PREVIEW OF THE OPTIONS YOU SELECTED CAREFULLY.**
  
  .If you are running an older version of Python, you could try to replace subprocess.run with subprocess.popen
  

