'''
File Name: hw4_question2
Made by: Erin Baxter
This program will let a user create a student's grade report
'''

print("Hello and welcome to the Grade Report Generator!\n")

try:
    sId = int(input("Enter student id of the student you would like a report for: "))
except ValueError:
    print("\nInvaild input. Please try again with the students 7 digit id number. Program ending")
    quit()

def main():
    searchFile()

def searchFile():
    global sId
    stringId = str(sId)

    if len(stringId) != 7:
        print("Not a real id")
        quit()

    getFile = open("student_data.txt", "r")

    studentInfo = []

    for line in getFile:
       if stringId in line:
           studentInfo.append(line)

    if studentInfo == []:
        print("Student not found")
        quit()

    code = []
    creditAll = []
    gradeAll = []

    for sClass in studentInfo:
        stringId, name, courseCode, credit, grade = sClass.split(":")
        code.append(courseCode)
        creditAll.append(credit)
        gradeAll.append(grade[0])

    #test = print("\n".join(map(str,{code}))


    reportFormat = (f'''
    Student Name: {name}
    Student ID Number: {stringId}

    Course Code    Course Credits   Course Grade
    --------------------------------------------
                   {creditAll[0]}                {gradeAll[0]}
    ''')

    print(test)

      


main()
