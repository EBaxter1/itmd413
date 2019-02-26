'''
File name: ebaxter1_hw5_question2
Made by: Erin Baxter
This program will multiple matrix
'''
print("Hello and welcome to the Matrix Multiplier 10,000!\n")

# this is the main functions that takes in user input and test it 
def main():
    # get input from user
    tupleOne = (input("Please enter 3x3 matrix1 with each number seperated by a space: "))
    tupleTwo = (input("Please enter 3x3 matrix2 with each number seperated by a space: "))
    #get number of elements from inputs 
    tOneLen = len(tupleOne.split(" "))
    tTwoLen = len(tupleTwo.split(" "))
    
    #check if inputs have spaces and aren't empty
    if " " in tupleOne and tupleOne != " " and " " in tupleTwo and tupleTwo != " ":
        #check and see if there are 9 numbers in both matrices 
        if tOneLen == 9 and tTwoLen == 9:
            #try and convert to float
            try:
                t1 = tuple(map(float, tupleOne.split(" ")))
                t2 = tuple(map(float, tupleTwo.split(" ")))
                #call other method 
                multiplyMatrix(t1, t2)
            except ValueError:
                print("Invaild input, both matrices must only contain numbers. Please try again")
        else:
            print("Invaild input, both matrices must be 3x3. Please try again")
    elif tupleOne == " ":
        print("Invaild input, no elements were found in matrix 1. Please try again")
    elif tupleTwo == " ":
        print("Invaild input, no elements were found in matrix 2. Please try again")
    elif tupleOne == "":
        print("Invaild input, no spaces were found in matrix 1. Please try again")
    elif tupleTwo == "":
        print("Invaild input, no spaces were found in matrix 2. Please try again")
    else:
        print("Invaild input, Please try again with list of 9 elements seperated by a space.")

    
# this functions multiplies two 3x3 matrices    
def multiplyMatrix(a, b):
    #multiply matices rows and columns
    num1 = round(a[0]*b[0]+a[1]*b[3]+a[2]*b[6], 1)
    num2 = round(a[0]*b[1]+a[1]*b[4]+a[2]*b[7], 1)
    num3 = round(a[0]*b[2]+a[1]*b[5]+a[2]*b[8], 1)

    num4 = round(a[3]*b[0]+a[4]*b[3]+a[5]*b[6], 1)
    num5 = round(a[3]*b[1]+a[4]*b[4]+a[5]*b[7], 1)
    num6 = round(a[3]*b[2]+a[4]*b[5]+a[5]*b[8], 1)

    num7 = round(a[6]*b[0]+a[7]*b[3]+a[8]*b[6], 1)
    num8 = round(a[6]*b[1]+a[7]*b[4]+a[8]*b[7], 1)
    num9 = round(a[6]*b[2]+a[7]*b[5]+a[8]*b[8], 1)

    #output info
    print("\nThe multiplication of the matrices is")
    print(f"{a[0]} {a[1]} {a[2]}   {b[0]} {b[1]} {b[2]}     {num1} {num2} {num3}")
    print(f"{a[3]} {a[4]} {a[5]} * {b[3]} {b[4]} {b[5]}  =  {num4} {num5} {num6}")
    print(f"{a[6]} {a[7]} {a[8]}   {b[6]} {b[7]} {b[8]}     {num7} {num8} {num9}")
    
   
#call main
main()

print("\nProgram now ending!")
