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
    createFile(name)

def createFile(userName):
    global filePath
    
    name = userName.replace(" ", "")

    fileName = filePath + name + ".html"

    writeFile(fileName)

def writeFile(fPath):
    global name
    global yourself

    
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
    

def outputFile(fPath):
    
    print("Your file can be found at:" , fPath)

    print("The file created is as follows:")

    

    
main()
