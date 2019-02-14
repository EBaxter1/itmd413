'''
File Name: hw4_question1
Made by: Erin Baxter
This program will take some basic informaiton about the user and then it wil create a html file based on it
'''

print("Hello and welcome to the Personal Web Page Generator!\n")

# variables
filePath = ("webPages\\")


#get information from user
name = input("Enter your name: ")
yourself = input("Describe yourself(Only press enter once you are done typing): ")


# main function that starts out calls 
def main():
    global name
    global yourself
    
    if (name != "" and name != None):
        if(yourself != "" and yourself != None):
            createFile(name)
        else:
            print("\nDescription input blank, please try again with a value. Program closing")
    else:
        print("\nName input blank, please try again with a value. Program closing")
        

# function that creates a name for new file and makes a path 
def createFile(userName):
    global filePath
    
    name = userName.replace(" ", "")
    fileName = filePath + name + ".html"
    writeFile(fileName)

# function that writes the new html page to the created file 
def writeFile(fPath):
    # call variables that were inputed 
    global name
    global yourself

    # new html code 
    htmlString = (f'''
    <html>
    <head>
    </head>
    <body>
        <center>
            <h1>{name}</h1>
        </center>
        <hr />
        {yourself}
        <hr />
    </body>
    </html>''')

    newFile = open(fPath, "w+")
    newFile.write(htmlString)
    newFile.close()

    print("\nYour personal html file has been created using your name!")

    outputFile(fPath)
    

#function that outputs the content of new files made 
def outputFile(fPath):
    
    print("Your file can be found in the webPages folder:" , fPath)
    print("The file created is as follows:")

    getFile = open(fPath, "r")
    print(getFile.read())
    getFile.close()
    

# call main    
main()

print("\nGoodbye!")
