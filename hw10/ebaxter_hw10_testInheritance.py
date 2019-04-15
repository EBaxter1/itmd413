'''
File Name: ebaxter_hw10_testInheritance.py
Made by: Erin Baxter
This program will test the Employee and ProductionWorker classes by interacting with them using user input
'''
# get class information from other file
from ebaxter_hw10_inheritance import ProductionWorker

# make new global object of class 
newWorker = ProductionWorker("", 0, 0, 0)

print("Hello and welcome to the New Worker Generator 20,000!")

# main method gets user input and calls function to set input and then displays input
def main():
    # variable to run while loop
    noStop = "y"

    # while loop to keep it running if there is an error
    while noStop == "y":
        # get user input
        newName = input("\nPlease enter new worker's name: ")
        try:  
            newId = int(input("Please enter new id number using only whole numbers: "))
            newShift = int(input("Please enter shift for new worker(1 for day shift, 2 for night shift): "))
            if newShift > 2 or newShift < 1: # make sure only day or night shift 
                print("Error, Shift can only be 1 or 2! Please try again")
                continue # make loop start over if error 
        except ValueError:
            print("Error! Please enter a whole number!")
            continue # make loop start over if error 
        newRate =  input("Please enter hourly pay rate: ")
        try:
            newRate = float(newRate) # check and make sure input is a number and convert if it is
            # call function to add input to created objects 
            createPerson(newName, newId, newShift, newRate)
            
            # output data
            print("\nNew Worker Created! Information is as follows:")
            newWorker.displayData() # call method from parent class
            newWorker.displayOtherData() # call method from child class
            break # end while loop
        except ValueError:
            print("Error! Please enter a number for rate!")
            continue # make loop start over if error 
                    
                       
# this function updates the created object attributes with new worker information
def createPerson(name, Id, shift, rate):
    newWorker.setName(name) # update name attibute ob object 
    newWorker.setNumber(Id) # update number attribute of object
    newWorker.setShift(shift) # update shift attribute of object
    newWorker.setRate(rate) # update rate attribute of object


# call main method
main()

print("\nThank you. Goodbye!")
