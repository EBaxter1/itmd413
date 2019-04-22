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

def main():
    #make some different ship objects
    newShipOne = Ship("Sally", 1917)
    newShipTwo = CruiseShip("Titanic", 1911, 35)
    newShipThree = CargoShip("Big Blue", 2011, 800)
    
    #make list of ship objects
    allShips = [newShipOne, newShipTwo, newShipThree]

    
    while 1 == 1:
        try:
            menuOption = int(input(f'''What would you like to do?\n1. List current ships(enter 1)\n2. Add new ship(enter 2)\n3. Exit program (enter any key other then 1 or 2)\nEnter option: '''))
            if menuOption == 1:
                displayInfo(allShips)
                continue
            elif menuOption == 2:
                allShips = addShip(allShips)
                continue
            else:
                break
        except ValueError:
            break

    # call function to display all the ship information
    

def addShip(currentList):
    while 1 == 1:
        try:
            shipType = int(input("What kind of ship is it? 1)Normal Ship, 2)Cruise Ship, 3)Cargo Ship: "))
            shipName = input("What is the name of the ship? ")
            try:
                shipYear = int(input("What year was the ship made?: "))
                if shipYear < 1000 or shipYear > 9999:
                    print("Error! Please enter a 4 digit year!")
                    continue
                if shipType == 1:
                    newItem = Ship(shipName, shipYear)
                    break
                elif shipType == 2:
                    shipSize = int(input("What is the max number of passengers for this ship?: "))
                    newItem = CruiseShip(shipName, shipYear, shipSize)
                    break
                elif shipType == 3:
                    shipCargo = float(input("What is the ship's cargo capacity in tons?: "))
                    newItem = CargoShip(shipName, shipYear, shipCargo)                 
                    break
            except ValueError:
                print("Error! Please enter a number!")
                continue       
        except ValueError:
            print("Error! Please enter either 1, 2 or 3")
            continue
                        
    currentList.append(newItem)

    print("\n")

    return currentList
    
def displayInfo(newList):
    print("\n")
    for ship in newList:
        ship.displayData()
        if isinstance(ship, CruiseShip):
            print("This here is a Cruise ship!")
        elif isinstance(ship, CargoShip):
            print("This here is a Cargo ship!")
        elif isinstance(ship, Ship):
            print("This here is just a normal ship!")
        print("\n")

# call main
main()

print("Thank you and goodbye!")
