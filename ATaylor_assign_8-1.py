#Alexander Taylor
#Intro to Programming
#Assignemnt 8.1

import os

print("Create a directory and file!")

#Create Directory
dirname = input("Enter dir name: ")
os.mkdir(dirname)

#Path
path = f"C:/Users/Alexander/Google Drive/School/Intro to Programming/Python/Week_8/{dirname}/"

#check for specified path
isdir = os.path.isdir(path)

#Create file, enter data, and check for directory
if isdir == True:
    filename = input("Enter file name: ")
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    address = input("Enter your address: ")
    phonenum = input("Enter your phone number: ")
    with open(f"C:/Users/Alexander/Google Drive/School/Intro to Programming/Python/Week_8/{dirname}/{filename}.txt", 'w') as f:
        f.write(f"{fname.title()} {lname.title()}, {address}, {phonenum}")
else:
    print("You need to create a directory!")