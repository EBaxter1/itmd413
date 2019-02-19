'''
File Name: hw4_question2
Made by: Erin Baxter
This program will let a user create a student's grade report
'''

print("Hello and welcome to the Grade Report Generator!\n")

# variable to folder
filePath = ("studentReports\\")

# get user input 
try:
    sId = int(input("Enter student id of the student you would like a report for: "))
except ValueError:
    print("\nInvaild input. Please try again with the student's 7 digit id number. Program ending")
    quit()
    

# main function that starts calls and test if vaild id entered 
def main():
    global sId
    stringId = str(sId)

    #test id length to be 7 
    if len(stringId) != 7:
        print("Invaild id number entered. Please enter a 7 digit id number")
    else:
        testId = searchFile(stringId)
        if testId == False:
            print("Student id not found.")
        else:
            fileName = createFile(stringId)
            reportContent = createReport(testId)
            writeFile(fileName,reportContent)
  

#function will search data file for student id and will return if found or reutrn false if not found 
def searchFile(studentId):
    getFile = open("student_data.txt", "r")

    studentInfo = []
    
    # go through each line and try and match id 
    for line in getFile:
       if studentId in line:
            # add line to list if matches id
           studentInfo.append(line)

    getFile.close()
     
    if studentInfo == []:
        return False
    else:
        return studentInfo


#function will create a file name/path based on student id 
def createFile(studentId):
    global filePath
    
    fileName = filePath + studentId + ".txt"

    return fileName


#function will create the content of the student report 
def createReport(studentInfo):
    # lists and variables for all the class info
    allCodes = []
    allCredits = []
    allGrades = []
    stringId = ""
    name = ""

    #take each part of a single class's info and place them into variables
    for classInfo in studentInfo:
        stringId, name, courseCode, credit, grade = classInfo.split(":")
        allCodes.append(courseCode)
        allCredits.append(credit)
        allGrades.append(grade[0])

    # basic format for report 
    reportFormat = (
    f'''Student Name: {name}\nStudent ID Number: {stringId}\n\nCourse Code    Course Credits   Course Grade\n--------------------------------------------\n''')

    #get length of how many classes there are for student 
    length = len(allCodes)

    #add each course and it's info to report 
    courseStrings = ""
    for x in range(length):
        courseString = (f'{allCodes[x]}                {allCredits[x]}               {allGrades[x]}')
        reportFormat += courseString + "\n"
        

    creditSum = 0
    product = 0
    productSum = 0

    #get total course credit hours 
    for y in allCredits:
            creditSum += int(y)

    #figure out GPA 
    for w in range(length):
        num1 = int(allCredits[w])
        g = allGrades[w]
        if g == 'A':
            num2 = 4
        elif g == 'B':
            num2 = 3
        elif g == 'C':
            num2 = 2
        elif g == 'D':
            num2 = 1
        else:
            num2 = 0
        # times grade value * that class credit
        product = num1 * num2
        # add up all courses
        productSum += product
        
    # calculate gpa 
    gpaTotal = 0
    gpaTotal = productSum / creditSum
    gpaTotal = round(float(gpaTotal), 1)
  
    # last couple strings of report to be added 
    totalCredits = (f"\nTotal Semester Course Credits Completed: {creditSum}")
    calcGPA = (f"\nSemester GPA: {gpaTotal}")
    # add last strings to report
    reportFormat += totalCredits
    reportFormat += calcGPA 
      
    return reportFormat


# function creates new file based on created name and writes to it
def writeFile(fName, content):
    # open new file and create if not exists
    newFile = open(fName, "w+")
    newFile.write(content)
    newFile.close()

    print("\nStudent report created! The report was named using the student id\n")

    outputFile(fName)


# ouputs created file 
def outputFile(fPath):
  print("Your report can be found in the studentReports folder:", fPath)
  print("An example of your report is as follows:\n")

  getFile = open(fPath, "r")
  print(getFile.read())
  getFile.close()
    
# calls main 
main()

print("\nProgram Endding, goodbye!")
