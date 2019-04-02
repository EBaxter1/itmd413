'''
File Name:ebaxter_hw8.py
Made by: Erin Baxter
This program save user data as dictionary and then output it to a file.
'''

#import regularr expressions
import re
import json

print("Hello and welcome to the Email Dictionary Generator 18,000!")

def main():
    # vairbale to to program running
    dic = {}
    noStop = "y"
    fileName = ("userEmails.txt")
      
    while noStop == "y":
        try:
            menuOption = int(input(f'''\nWhat would you like to do?\n1. Look up email address(enter 1)\n2. Add new name and email address(enter 2)\n3. Update existing email address(enter 3)\n4. Delete existing name and email address(enter 4)\n5. Exit program (enter any key other then 1-4)\nEnter option: '''))
            if menuOption == 1:
                lookUpValue(fileName)
            elif menuOption == 2:
                addValue(dic, fileName)
            elif menuOption == 3:
                updateValue()
            elif menuOption == 4:
                delValue()
            else:
                #writeValue()
                file.close()
                noStop = "n"
        except ValueError:
            #writeValue()
            noStop = "n"
                      

def lookUpValue(file):
    nfile = open(file, "r")
    '''email = input("Please enter the email address to search for: ")
    realEmail = r"^\w+@+\w+\.\w"
    if re.match(realEmail, email):
        for line in file:
            if email 
    else:
        print("Invalid email format! Please try again real email format(contains @ and .)")'''
    #print(file.read())
    d = {1:2}
    for line in nfile:
        #print(line)
        d.update(json.loads(line))
    print(d)
    

def addValue(stuff,file):
    file = open(file, "a+")
    '''name = input("Please enter new name: ")
    email = input("Please enter new eamil: ")
    newData = {name:email}
    stuff.update(newData)'''
    stuff.update({'a':'a1', 'b':'b2'})
    print(stuff)
    length = len(stuff)
    for x in stuff.items():
        file.write(str(x) + "\n")
    
    
    
'''
def updateValue():

def delValue():
      
def writeFile():
'''
      
#calls main
main()

print("Program ending, goodbye!")
