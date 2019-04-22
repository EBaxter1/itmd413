'''
File Name: ebaxter_hw11_testPolymorphism.py
Made by: Erin Baxter
This program will go through the classes created in th epolumorphism file and call the print function and test them using issinstance
'''
# get class information from other file 
from ebaxter_hw11_polymorphism import Ship
from ebaxter_hw11_polymorphism import CruiseShip
from ebaxter_hw11_polymorphism import CargoShip

print("Hello and welcome to the Ship info displayer 25,000!\n")

# main function that has a remade list of ships and a menu which items will call different functions 
def main():
    #make some different ship objects
    newShipOne = Ship("Sally", 1917)
    newShipTwo = CruiseShip("Titanic", 1911, 35)
    newShipThree = CargoShip("Big Blue", 2011, 800)
    
    #make list of ship objects
    allShips = [newShipOne, newShipTwo, newShipThree]

    # while loop for menu
    while 1 == 1: # since using break and continue can make loop just something always true
        # try catch for non ints
        try:
            menuOption = int(input(f'''What would you like to do?\n1. List current ships(enter 1)\n2. Add new ship(enter 2)\n3. Exit program (enter any key other then 1 or 2)\nEnter option: '''))
            # option 1
            if menuOption == 1:
                # calls function and passes list
                displayInfo(allShips)
                continue # keeps loop going after function returns 
            elif menuOption == 2:
                # calls function and updates list with returned value
                allShips = addShip(allShips)
                continue # keeps loop going after funciton returns
            else:
                break # ends loop and exits main
        except ValueError:
            break # ends loop and exits main
    
# this function will create a new ship object and add it to the ships list
def addShip(currentList):
    # while loop for creation 
    while 1 == 1: # since using break and continue can make loop just something always true
        # try catch for options
        try:
            #get ship type to know what type of object 
            shipType = int(input("\nWhat kind of ship is it? 1)Normal Ship, 2)Cruise Ship, 3)Cargo Ship: "))
            shipName = input("What is the name of the ship? ")
            try: # try for numbers
                shipYear = int(input("What year was the ship made?: "))
                if shipYear < 1000 or shipYear > 9999: # make sure valid year 
                    print("Error! Please enter a 4 digit year!")
                    continue
                if shipType == 1:
                    # makes new Ship object 
                    newItem = Ship(shipName, shipYear) 
                    break # ends loop
                elif shipType == 2:
                    # extra information for Cruise Ship object 
                    shipSize = int(input("What is the max number of passengers for this ship?: "))
                    newItem = CruiseShip(shipName, shipYear, shipSize)
                    break # ends loop 
                elif shipType == 3:
                    # extra info for Cargo Ship object 
                    shipCargo = float(input("What is the ship's cargo capacity in tons?: "))
                    newItem = CargoShip(shipName, shipYear, shipCargo)                 
                    break # end loop 
            except ValueError:
                print("Error! Please enter a whole number!")
                continue # make loop keep going for mistakes    
        except ValueError:
            print("Error! Please enter either 1, 2 or 3")
            continue # keep it going s

    # add need object to list
    currentList.append(newItem) 
    print("New ship element has successfully been created!\n")

    #return updated list 
    return currentList

# this function will display the print function of all the ship objects and test what type they are  
def displayInfo(newList):
    print("\nCurrently stored ships:")
    # for loop to go through all objects
    for ship in newList:
        #call function 
        ship.displayData()
        #checks each object to see what kind of ship class it was made from
        if isinstance(ship, CruiseShip):
            print("This here is a Cruise ship!\n")
        elif isinstance(ship, CargoShip):
            print("This here is a Cargo ship!\n")
        elif isinstance(ship, Ship):
            print("This here is just a normal ship!\n")
   
# call main
main()

print("Thank you and goodbye!")
