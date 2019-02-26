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
        if tOneLen == tTwoLen:
            #try and convert to float
            try:
                #make 3x3 tuples
                t1 = tuple(map(float, tupleOne.split(" ")))
                t2 = tuple(map(float, tupleTwo.split(" ")))
                newTupleOne = (t1[:3], t1[3:6], t1[6:])
                newTupleTwo = (t2[:3], t2[3:6], t2[6:])

                #call other method 
                multiplyMatrix(newTupleOne, newTupleTwo)
            except ValueError:
                print("Invaild input, both matrices must only contain numbers. Please try again")
        else:
            print("Invaild input, matrix 1 has to same number of rows as columns in matrix 2. Please try again")
    elif tupleOne == " ":
        print("Invaild input, no elements were found in matrix 1. Please try again")
    elif tupleTwo == " ":
        print("Invaild input, no elements were found in matrix 2. Please try again")
    elif tupleOne == "":
        print("Invaild input, no spaces were found in matrix 1. Please try again")
    elif tupleTwo == "":
        print("Invaild input, no spaces were found in matrix 2. Please try again")
    else:
        print("Invaild input, Please try again with list of number elements seperated by a space.")

    
# this functions multiplies two 3x3 matrices    
def multiplyMatrix(a, b):
    #get len of tuples
    lenA = len(a)
    lenB = len(b)
    #make empty result matrix
    c = ([[0 for row in range(lenB)] for col in range(lenA)])
    lenC = len(c)
    
    #multiply matices rows and columns
    for x in range(lenA):
        for y in range(lenB):
            for z in range(lenA):
                c[x][y] += round(a[x][z] * b[z][y], 1)   
    
    #output info
    print("\nThe multiplication of the matrices is")
    for w in range(lenA):
        if w == ((lenA - 1)/2):
             print(f'''{a[w]} * {b[w]} = {c[w]}''')
        else:
            print(f'''{a[w]}   {b[w]}   {c[w]}''')
   
   
#call main
main()

print("\nProgram now ending!")
