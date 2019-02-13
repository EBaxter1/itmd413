'''
File Name: hw4_question1
Made by: Erin Baxter
This program will take some basic informaiton about the user and then it wil create a html file based on it
'''

print("Hello and welcome to the Personal Web Page Generator!\n")

# variables
filePath = ("C:\\Users\\erinf\\School_Work\\spring2019\\itmd413\\hw4\\webPages\\")


#get information from user
name = input("Enter your name: ")
yourself = input("Describe yourself(Only press enter once you are down typing): ")




def main():
    createFile()

def createFile():
    global name
    global filePath
    
    name = name.replace(" ", "")

    fileName = filePath + name + ".html"

    writeFile(fileName)

def writeFile(fName):
    

#def outputFIle():

    
main()
