'''
File Name:ebaxter_hw8.py
Made by: Erin Baxter
This program save user data as dictionary and then output it to a file.
'''

#import regularr expressions
import re

print("Hello and welcome to the Email Dictionary Generator 18,000!")

#main method calls other methods 
def main():
    # varable to keep program running
    noStop = "y"
    # file path location
    fileName = ("userEmails.txt")
    # dictionary created from file 
    newDic = readFile(fileName)

    # while loop to keep program running 
    while noStop == "y":
        # try catch to have menu options 
        try:
            # menu option input 
            menuOption = int(input(f'''\nWhat would you like to do?\n1. Look up email address(enter 1)\n2. Add new name and email address(enter 2)\n3. Update existing email address(enter 3)\n4. Delete existing name and email address(enter 4)\n5. Exit program (enter any key other then 1-4)\nEnter option: '''))
            # menu options 
            if menuOption == 1:
                lookUpValue(newDic)
            elif menuOption == 2:
                # reassign new updated dictionary 
                newDic = addValue(newDic, fileName)
            elif menuOption == 3:
                # reassign new updated dictionary 
                newDic = updateValue(newDic)
            elif menuOption == 4:
                # reassign new updated dictionary 
                newDic = delValue(newDic)
            else:
                # write file
                writeFile(fileName, newDic)
                # stop while loop
                noStop = "n"
        except ValueError:
            @ write file 
            writeFile(fileName, newDic)
            # stop while loop
            noStop = "n"

# function opens and reads file to create recreate dictionary 
def readFile(file):
    # variable for new dictionary 
    dic = {}
    #try to open file 
    try:
        # open file
        getFile = open(file, "r")
        # for loop to go though each line of file and make it key, value pair 
        for line in getFile:
            # make each part of line into key and value 
            key, val = line.strip().split(":")
            # assgin value to ket 
            dic[key] = val
        # close file 
        getFile.close()
        # return new dictionary
        return(dic)
    # if file can't be found
    except FileNotFoundError:
        # make new file 
        getFile = open(file, "a+")
        # close file 
        getFile.close()
        # return empty dictionary 
        return(dic)

# function to search dictionary for email   
def lookUpValue(newDic):
    # regular expression for standard email 
    realEmail = r"^\w+@+\w+\.\w"
    email = input("Please enter the email address to search for: ")
    # compare input and realEmail
    if re.match(realEmail, email):
        # search for email in dictionary 
        if email in newDic.keys():
            print("Email found!")
            print(f"Name with email, {email}, is {newDic[email]}")
        else:
            print("Email not found!")
    else:
        print("Invalid email format! Please try again real email format(contains @ and .)")
      
# function to add new email and name 
def addValue(dic, file):
    # regular expression for standard email 
    realEmail = r"^\w+@+\w+\.\w"
    email = input("Please enter new eamil: ")
    # compare input and realEmail
    if re.match(realEmail, email):
        name = input("Please enter new name: ")
        newData = {email: name}
        # update dictionary for new email 
        dic.update(newData)
        print("New user info added!")
        return(dic)
    else:
        print("Invalid email format! Please try again real email format(contains @ and .)")
   
# function to update email    
def updateValue(dic):
    print("Warning! In order to update email, the user profile will have to be deleted and recreated")
    # regular expression for standard email 
    realEmail = r"^\w+@+\w+\.\w"
    email = input("Please enter the email address to update: ")
    # compare input and realEmail
    if re.match(realEmail, email):
        # search for email 
        if email in dic.keys():
            # same name 
            sameName = dic.get(email)
            newEmail = input("Please enter new email address: ")
            if re.match(realEmail, newEmail):
                # delete email set 
                del(dic[email])
                newData = {newEmail: sameName}
                # update dictionary 
                dic.update(newData)
                print("Email updated!")
                return(dic)
            else:
                print("Invalid email format! Please try again real email format(contains @ and .)")
        else:
            print("Email not found!")
    else:
        print("Invalid email format! Please try again real email format(contains @ and .)")

# function to delete a key value pair 
def delValue(dic):
    # regular expression for standard email 
    realEmail = r"^\w+@+\w+\.\w"
    email = input("Please enter the email address to delete: ")
    # compare input and realEmail
    if re.match(realEmail, email):
        # search for email
        if email in dic.keys():
                # delete email set 
                del(dic[email])
                print("Email set deleted!")
                # return new dictionary without set 
                return(dic)
        else:
            print("Email not found!")
    else:
        print("Invalid email format! Please try again real email format(contains @ and .)")

# function to write dictionary to file 
def writeFile(file, dic):
    # open file
    getFile = open(file, "w+")
    for x, y in dic.items():
        # divide ky value pairs with colon 
        getFile.write(str(x) + ":" + str(y) + "\n")
    # close file 
    getFile.close()
      
#calls main
main()

print("Program ending, goodbye!")
