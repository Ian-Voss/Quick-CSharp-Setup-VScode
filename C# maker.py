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

#Process:
    #CD to the beginning.
    #CD to specified directory.
    #Making container folder.
    #CD to container folder.
    #Making main folder.
    #Creating class folder.
    #Creating SLN.
    #Linking SLN to main.
    #Linking SLN to classes.
    #Opening VScode.

#Script.
subprocess.run(["cd", "/", "&", "cd", f"C:/Users/{folder}", "&","mkdir", confolder, "&",
  "cd", confolder, "&", "dotnet", "new", "console", "-o", mainfolder, "&",
  "dotnet", "new", "classlib", "-n", f'{classesfolder}', "&",
  "dotnet", "new", "sln", "-n", f'{slname}', "&",
  "dotnet", "sln", f"{slname}.sln", "add", f"{mainfolder}/{mainfolder}.csproj", "&",
  "dotnet", "sln", f"{slname}.sln", "add", f"{classesfolder}/{classesfolder}.csproj", "&",
  "code","."],shell=True)


print("Code was run successfully.")

#The reason why everything is in one line is because everytime .run() is used, a new shell is used.
#I needed all commands to run on the same terminal.
