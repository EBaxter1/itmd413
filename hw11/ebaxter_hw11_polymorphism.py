'''
File Name: ebaxter_hw11_polymorphism.py
Made by: Erin Baxter
This program will have the classes Ship, CruiseShip, CargoShip and their members and a print function that will be overrated 
'''

# parent class that has name of ship, built year, accessers, mutators and print function
class Ship(object):
    # constuctor
    def __init__(self, name, year):
        #member variables 
        self.name = name
        self.year = year

    # getters 
    def getName(self):
        return self.__name

    def getYear(self):
        return self.year

    # setters 
    def setName(self, name):
        self.__name = name

    def setYear(self, year):
        self.year = year

    # print function  
    def displayData(self):
        print("Ship name:", self.name)
        print("Ship built in:", self.year)

# child class that has name of ship, build year and number of passangers it can hold 
class CruiseShip(Ship):
    # constuctor 
    def __init__(self, name, year, peeps):
        # get memebr variables from parent class 
        super(CruiseShip, self).__init__(name, year)
        self.peeps = peeps # member variable 

    # getter 
    def getPeeps(self):
        return self.peeps

    #setter
    def setPeeps(self, peeps):
        self.peeps = peeps

    # print function
    def displayData(self):
        print("Ship name:", self.name)
        print("Maximum number of passengers:", self.peeps)

# child class that has name of ship, build year and cargo capacity 
class CargoShip(Ship):
    # constructor
    def __init__(self, name, year, cargo):
        # get memebr variables from parent class 
        super(CargoShip, self).__init__(name, year)
        self.cargo = cargo # memeber variable 

    # getter 
    def getCargo(self):
        return self.cargo

    # setter
    def setCargo(self, peeps):
        self.cargo = cargo

    # print function 
    def displayData(self):
        print("Ship name:", self.name)
        print(f"Ship cargo capacity: {self.cargo} tons")


        


