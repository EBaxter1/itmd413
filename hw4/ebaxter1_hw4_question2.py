'''
File Name: hw4_question2
Made by: Erin Baxter
This program will let a user create a student's grade report
'''

print("Hello and welcome to the Grade Report Generator!\n")

filePath = ("studentReports\\")

try:
    sId = int(input("Enter student id of the student you would like a report for: "))
except ValueError:
    print("\nInvaild input. Please try again with the students 7 digit id number. Program ending")
    quit()

def main():
    global sId
    stringId = str(sId)
    
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
  

def searchFile(studentId):

    getFile = open("student_data.txt", "r")

    studentInfo = []

    for line in getFile:
       if studentId in line:
           studentInfo.append(line)

    getFile.close()
     
    if studentInfo == []:
        return False
    else:
        return studentInfo


def createFile(studentId):
    global filePath
    fileName = filePath + studentId + ".txt"
    return fileName

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
    for w in allCredits:
        # convert grades to number
        for z in allGrades:
            if z == 'A':
                z = 4
            elif z == 'B':
                z = 3
            elif z == 'C':
                z = 2
            elif z == 'D':
                z = 1
            else:
                z = 0
            # times grade value * that class credit 
            product = z * int(w)
        # add up all courses
        productSum += product

    # calculate gpa 
    gpaTotal = 0
    gpaTotal = productSum / creditSum 
  
    # last couple strings of report 
    totalCredits = (f"\nTotal Semester Course Credits Completed: {creditSum}")
    calcGPA = (f"\nSemester GPA: {gpaTotal}")

    # add last strings to report
    reportFormat += totalCredits
    reportFormat += calcGPA 
      
    return reportFormat

def writeFile(fName, content):
    newFile = open(fName, "w+")
    newFile.write(content)
    newFile.close()

    print("\nStudent report created! The report was named using the student id\n")

    outputFile(fName)

def outputFile(fPath):
  print("Your report can be found in the studentReports folder:", fPath)
  print("An example of your report is as follows:")

  getFile = open(fPath, "r")
  print(getFile.read())
  getFile.close()
    

main()

print("\nProgram Endding, goodbye!")
