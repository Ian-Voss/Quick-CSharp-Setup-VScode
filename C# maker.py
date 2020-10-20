#Python 3.8.3 Anaconda.
#Prepares a C# Solution and project in specified folder.
#Will not work on Python 3.7.

import subprocess, os, shutil

#INSTRUCTIONS.
def instructions():
    print("INSTRUCTIONS:")
    print("\t.Read the README.")
    print("\t.Write names without the file type.")
    print("\t.Use CMD format for typing in a directory.")
    print("\t.Make sure that the names you choose don't have any invalid characters.")

    #Examples.
    print("Example directory input: C:/users/ian/desktop")
    print("Example name input: main\n")

    notdone = True

    while notdone:
      folder = input("In what directory do you want your project?\nC:/Users")
      confolder = input("How do you wish to name you container folder? ")
      mainfolder = input("What name do you want for your main() folder? ")
      classesfolder = input("What name do you want for your classes folder? ")
      slname = input("What do you want to name your sln? ")
      classnum = input("How many class files do you want? ")

      #Checking for errors.
      print("Checking for errors...")
      error = False
      varlist = [folder, confolder, mainfolder, classesfolder, slname]

      #Invalid characters or names.
      for var in varlist:
            if var[0:4] == "con.":
                  print("Files can't be named 'con'")
                  error = True
                  break
                  
            for char in ["<",">",":",'"',"//","\\\\","|","?","*"]:
                  if char in var:
                        print(f"{char} cannot be used in filenames. It is being used in {var}")
                        error = True
                        break

      #Invalid number of classes.
      try:
        int(classnum)
      except:
        print("The number of classes must be an integer!")
        continue

      #Reset if error is found.
      if error == True:
            print("Error found! resetting...")
            continue
      
      print("No errors found!")
                      
      #Confirming instructions
      print("OPTIONS SELECTED:")
      print("Directory for project: C:/users" + folder)
      print("Name of container folder: " + confolder)
      print("Name of main() folder: " + mainfolder)
      print("Name of classes folder: " + classesfolder)
      print("Name of .sln: " + slname)
      print("Amount of classes: " + str(classnum))

      reply = input("Are these options ok for you? Y/N\t")
      if reply == "Y" or reply == "y" or reply == "yes":
            notdone = False
    return varlist + [classnum]

#.Net stuff       
def cmd(folder,confolder,mainfolder,classesfolder,slname):
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
      "mkdir", "tests", "&", #Making tests folder.
      "cd", "tests", "&", #CD to tests folder.
      "dotnet", "new", "xunit", "&", #Making unit test file.
      "cd", "..", "&", #CD back.
      "dotnet", "new", "sln", "-n", f'{slname}', "&", #Creating SLN.
      "dotnet", "sln", f"{slname}.sln", "add", f"{mainfolder}/{mainfolder}.csproj", "&", #Linking SLN to main.
      "dotnet", "sln", f"{slname}.sln", "add", f"tests/tests.csproj", "&", #Linking SLN to tests.
      "dotnet", "sln", f"{slname}.sln", "add", f"{classesfolder}/{classesfolder}.csproj", "&", #Linking SLN to classes.
      "dotnet", "add", f"{mainfolder}/{mainfolder}.csproj", "reference", f"{classesfolder}/{classesfolder}.csproj", "&", #Adding a reference to the classes csproj from main.
      "dotnet", "add", f"tests/tests.csproj", "reference", f"{classesfolder}/{classesfolder}.csproj", "&", #Adding a reference to the classes csproj from tests.
      "cd", "tests", "&", #CD to tests folder.
      "dotnet", "restore", "&", #Restoring tests.
      "cd", "..", "&", #CD back.
      "code","."],shell=True) #Opening VScode.

      #The reason why everything is in one line is because everytime .run() is used, a new shell is used.
      #I needed all commands to run on the same terminal.

#Adding more class files    
#Adding more class files    
def moreclasses(folder,confolder,mainfolder,classesfolder,slname, classnumstr):
    print("Making more class files:")
    classnum = int(classnumstr)
    refolder = ""
    for directory in folder[1:].split("/"):
          refolder += "\\" + directory
    contpath = f"C:\\Users\\{refolder}\\{confolder}"

    classeslist = ["cd", "/", "&", 
      "cd", contpath + f"\\{classesfolder}"]   #REplace backslashes with one single backslash and write "r" before ev'ry stringy

    if classnum > 1:
            for num in range(classnum):
                  classeslist += ["&","copy","Class1.cs", contpath]
                  classeslist += ["&", "rename", contpath + "\\Class1.cs", f"Class{str(num+1)}.cs"]
                  
            subprocess.run(classeslist,shell=True)

            pycontpath = f"C:\\Users\\{folder}\\{confolder}"
            bal = [file for file in os.listdir(pycontpath) if os.path.isfile(pycontpath + "\\" + file) and file[:5] == "Class"]

            #Moving to class folder.
            for file in bal:
                  print(f"Moving {file}...")
                  shutil.move(os.path.join(pycontpath,file), pycontpath + f"\\{classesfolder}")
            
            for num in range(len(bal)):
                  print(f"Writing in {bal[num]}...")
                  with open(os.path.join(pycontpath + f"\\{classesfolder}", bal[num]),mode="w+") as csfile:
                        csfile.write(f"using System; \n\nnamespace {classesfolder} \n{{\n\tpublic class Class{str(num+2)}\n\t{{ \n\t}} \n}}")
                        #Yes I did this

    print("Code run successfully.")


if __name__ == "__main__":
      vars = instructions()
      cmd(vars[0],vars[1],vars[2],vars[3],vars[4])
      moreclasses(vars[0],vars[1],vars[2],vars[3],vars[4],vars[5])

