import os
num_Files = len(os.listdir())

def intro():

    print("This program will rename all the files in the directory to a desired naming scheme\n")
    print("For the 'Existing Naming Scheme', enter the full name or partial name of the existing naming scheme\n")
    print("If you leave this blank, the program will rename all the files in the directory!\n ")
    print("")

def renamer():
    old_name = str(input("Enter existing naming scheme(Leave Blank if you want to rename all the files in the Directory): "))
    new_name = str(input("Enter new Naming Scheme: "))
    extension = str(input("Enter the desired File Extension (e.g. - jpg, ,mp4, exe): "))

    n = 1
    while n < num_Files:
        for filename in os.listdir("."):
            if filename.startswith(old_name) and not filename.startswith("Mass Renamer"):
                os.rename(filename, new_name + " " + str(n) + "." + extension)
                n +=1
    print("Rename Completed \n")
    input("Press Enter to Exit...")



intro()
renamer()
