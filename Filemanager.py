import os
import sys
import time
import platform


def filerename():
    usrinput = input(">>> ")
    if usrinput == "exit":
        sys.exit()
    elif usrinput == "clear":
        os.system("clear")
    elif usrinput == "modify file":
        print("Which directory?")
        usrinput = input(">>> ")
        if usrinput != "":
            try:
                os.chdir(f'{usrinput}')
                print("File list:")
                time.sleep(.5)
                file_list = file_list = [f"{file}/" if os.path.isdir(os.path.join(usrinput, file)) else file for file in os.listdir(usrinput)]
                print(*file_list, sep="\n")
                print("What would you like to do?")
                print("Type \"create\" to create a file or folder.")
                print("Type \"delete\" to delete a file or folder.")
                print("Type \"open\" to open the folder in Finder.")
                print("Type \"rename\" to rename a folder or file.")
                print("Type \"change directory\" if you selected the wrong folder.")
                usrinput = input(">>> ")
                if usrinput == "change directory":
                    print("Resetting...")
                    time.sleep(.5)
                    print("Type \"modify file\" to select your new directory.")
                    filerename()
                elif usrinput == "rename":
                    print("Which file?")
                    usrinput = input(">>> ")
                    if usrinput != "":
                        print("Input new name:")
                        newname = input(">>> ")
                        try:
                            os.rename(f"{usrinput}", f"{newname}")
                            print("Success! Resetting to beginning.")
                            filerename()
                        except OSError:
                            print("Invalid file name. Resetting to beinning.")
                            filerename()
                elif usrinput == "open":
                    current_directory = os.getcwd()
                    try:
                        os.system(f"open {current_directory}")
                    except OSError:
                        print("Error - Invalid Directory")
                elif usrinput == "delete":
                    print("Sorry, file deletion is not supported in this program.\nPlease try again and use the \"open\" command to delete your file manually.")
                    #print("Which file?")
                    #usrinput = input(">>> ")
                    #if usrinput != "":
                     #   delete = usrinput
                      #  delinput = input(">>> ")
                       # print("Are you sure?")
                        #if delinput == "yes":
                         #   print("Type \"DELETE\" to confirm.")
                          #  delinput = input(">>> ")
                           # if delinput == "DELETE":
                            #    try:
                             #       os.remove(f"{delete}")
                              #  except OSError:
                               #     print("Invalid file. Resetting to beginning.")
                           # else:
                            #    print("Invalid. Resetting to beginning.")
                       # else:
                        #    print("Resetting to beginning.")
                elif usrinput == "create":
                    print("File or folder?")
                    usrinput = input(">>> ")
                    if usrinput == "file":
                        print("Input the name of the file.")
                        usrinput = input(">>> ")
                        if usrinput != "":
                            print("Creating file...")
                            time.sleep(5)
                            if not os.path.exists(usrinput):
                                with open(usrinput, "x", encoding="utf-8") as file:
                                    pass
                                print("Success!")
                                print("Resetting to beginning.")
                        else:
                            print("Please specify file name!")
                    elif usrinput == "folder":
                        print("Input the name of the folder.")
                        usrinput = input(">>> ")
                        if usrinput != "":
                            print("Creating folder...")
                            time.sleep(5)
                            os.mkdir(f"{usrinput}")
                            print("Success!")
                            print("File list:")
                            file_list = file_list = [f"{file}/" if os.path.isdir(os.path.join(usrinput, file)) else file for file in os.listdir(usrinput)]
                            print(*file_list, sep="\n")
                            print("Resetting to beginning.")
                            filerename()
                        else:
                            print("Please specify a name. Resetting to beginning.")

                    else:
                        print("Invalid command. Resetting to beginning of modification process.")
                        filerename()
                else:
                    print("Invalid- Resetting to beginning")
            
            except OSError:
                print("Invalid directory.")
                filerename()
        else:
            print("Invalid input. Please try again.")
    else:
        print("Invalid input. Please try again.")





if __name__ == "__main__":
    os_name = platform.system()

    if os_name == "Darwin":
        password = input("Please enter the passcode >>> ")
        if password == "1234":
            print("Welcome to the file modifier!")
            print("Type \"exit\" to quit.")
            print("Type \"modify file\" to start the modification process.")
            while True:
                filerename()
        else:
            print("Wrong password.")
            sys.exit()
    else:
        print("Sorry, this tool only works for MacOS.")