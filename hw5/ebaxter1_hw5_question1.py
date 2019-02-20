'''
File Name: ebaxter1_hw5_question1
Made By: Erin Baxter
This program will check to see if a list is sorted
'''

print("Hello and welcome to the List Sort Checker 9000!\n")

# get user input and test it 
userList = (input("Please enter a list with each element seperated by a space: "))
if " " in userList and userList != " ":
    print("Testing list now...")
elif userList == " ":
    print("Invaild input, no list found. Please try again with a list with spaces. Program now ending")
    quit()
else:
    print("Invaild input, no spaces found. Please try again with spaces. Program now ending")
    quit()


# main method that returns final output result 
def main():
    global userList
    # make user input a list and make elements ints
    userList = list(map(float, userList.split(" ")))

    # assign and call isSorted method 
    test = isSorted(userList)

    if test == True:
        print("That list is already sorted")
    else:
        print("That list is not sorted")

# method that checks if a list is sorted 
def isSorted(lst):
    newList = sorted(lst)
    
    if lst == newList:
        return True
    else:
        return False

#call main
main()

print("\nGoodbye! Program ending")
