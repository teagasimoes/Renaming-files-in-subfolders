#Change file names and folder names in a given directory and all its subfolders

#Shell Scripts

#To generate a exe file
#pyinstaller --onefile yourcode.py

#Run as a administrator

import os
import msvcrt as m

def main():
    path = 'C:\\Users\\Usuario\\Downloads\\Marketdata'

    #Count to name the 2nd file and further
    count = 0

    #Loop for your whole folder
    for root, dirs, files in os.walk(path):
        for i in files:

            #Fetch the current Folder in Loop
            cpath = os.path.join(root)
            listfile = os.listdir(cpath)

            #Renaming the 1st file
            if count == 0:
                os.rename(os.path.join(root, i), os.path.join(root, "HDP" + ".pdf"))
                count = 1
                count += 1
            else:
                #If you reach the last file on your current folder, rename and reset the variable count
                if str(count) in str(len(listfile)):
                    os.rename(os.path.join(root, i), os.path.join(root, "HDP " + str(count) + ".pdf"))
                    count = 0
                else:
                    os.rename(os.path.join(root, i), os.path.join(root, "HDP " + str(count) + ".pdf"))
                    count += 1


if __name__ == '__main__':
    main()

