#Python 3.7 Anaconda.
#Prepares a C# Solution and project in specified folder.
#Will not work on Python 2.

import subprocess

#INSTRUCTIONS.
print("\nINSTRUCTIONS:")
print(".Write names without the file type.")
print(".Use CMD format for typing in a directory.")
print(".Make sure that the names you choose don't have any invalid characters.\n")

#Examples.
print("Example directory input: C:/users/ian/desktop")
print("Example name input: main\n")

#Receiving directory and names.
folder = input("In what directory do you want your project?\nC:/Users/")
confolder = input("How do you wish to name you container folder? ")
mainfolder = input("What name do you want for your main folder? ")
classesfolder = input("What name do you want for your classes folder? ")
slname = input("What do you want to name your sln? ")

print("Starting process...")
print("This might take a while")

#If you used Bash you could link projects to solutions more easily,
#dotnet sln <solutionName>.sln add **/*.csproj,
#Linking all projects at once.

subprocess.run(["cd", "/", "&", #CD to the beginning.
  "cd", f"C:/Users/{folder}", "&", #CD to specified directory.
  "mkdir", confolder, "&", #Making container folder.
  "cd", confolder, "&", #CD to container folder.
  "dotnet", "new", "console", "-o", mainfolder, "&", #Making main folder.
  "dotnet", "new", "classlib", "-n", f'{classesfolder}', "&", #Creating class folder.
  "dotnet", "new", "sln", "-n", f'{slname}', "&", #Creating SLN.
  "dotnet", "sln", f"{slname}.sln", "add", f"{mainfolder}/{mainfolder}.csproj", "&", #Linking SLN to main.
  "dotnet", "sln", f"{slname}.sln", "add", f"{classesfolder}/{classesfolder}.csproj", "&", #Linking SLN to classes.
  "dotnet", "add", f"{mainfolder}/{mainfolder}.csproj", "reference", f"{classesfolder}/{classesfolder}.csproj", "&", #Adding a reference to the classes csproj.
  "code","."],shell=True) #Opening VScode.

print("Code was run successfully.")

#The reason why everything is in one line is because everytime .run() is used, a new shell is used.
#I needed all commands to run on the same terminal.
