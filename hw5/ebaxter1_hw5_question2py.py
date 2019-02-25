'''
File name: ebaxter1_hw5_question2
Made by: Erin Baxter
This program will multiple matrix
'''

#import numbers for testing int and float
import numbers

print("Hello and welcome to the Matrix Multiplier 10,000!\n")

def main():
    tupleOne = (input("Please enter 3x3 matrix1 with each number seperated by a space: "))
    tupleTwo = (input("Please enter 3x3 matrix2 with each number seperated by a space: "))

    tOneLen = len(tupleOne.split(" "))
    tTwoLen = len(tupleTwo.split(" "))

   # print("Matrix 1 does not have same number of columns as rows in matrix 2.")

    if " " in tupleOne and tupleOne != " " and " " in tupleTwo and tupleTwo != " ":
        if tOneLen == 9 and tTwoLen == 9:
            t1 = tuple(map(float, tupleOne.split(" ")))
            t2 = tuple(map(float, tupleTwo.split(" ")))
            multiplyMatrix(t1, t2)
        else:
            print("Invaild input, both matrices must be 3x3. Please try ahain, program now ending")
            quit()
    elif tupleOne == " ":
        print("Invaild input, no elements were found in matrix 1. Please try again, program now ending")
        quit()
    elif tupleTwo == " ":
        print("Invaild input, no elements were found in matrix 2. Please try again, program now ending")
        quit()
    elif tupleOne == "":
        print("Invaild input, no spaces were found in matrix 1. Please try again, program now ending")
        quit()
    elif tupleTwo == "":
        print("Invaild input, no spaces were found in matrix 2. Please try again, program now ending")
        quit()
    else:
        print("Invaild input, Please try again with list of elements seperated by a space. Program now ending")
        quit()
        
        
def multiplyMatrix(a, b):
    for x in range(3):
        sum1 = a[x] * b[x]
        

    print(a)
    print(b)



#call main
main()

print("\nGoodbye! Program now ending")
