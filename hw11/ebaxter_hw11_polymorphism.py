'''
File Name: ebaxter_hw11_polymorphism.py
Made by: Erin Baxter
This program will have the classes Ship, CruiseShip, CargoShip and their members
'''

# parent class that has name of ship, built year, accessers, mutators and print function
class Ship(object):
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def getName(self):
        return self.__name

    def getYear(self):
        return self.year

    def setName(self, name):
        self.__name = name

    def setYear(self, year):
        self.year = year
        
    def displayData(self):
        print("Ship name:", self.name)
        print("Ship built in:", self.year)


class CruiseShip(Ship):
    def __init__(self, name, year, peeps):
        super(CruiseShip, self).__init__(name, year)
        self.peeps = peeps

    def getPeeps(self):
        return self.peeps

    def setPeeps(self, peeps):
        self.peeps = peeps

    def displayData(self):
        print("Ship name:", self.name)
        print("Maximum number of passengers:", self.peeps)


class CargoShip(Ship):
    def __init__(self, name, year, cargo):
        super(CargoShip, self).__init__(name, year)
        self.cargo = cargo

    def getCargo(self):
        return self.cargo

    def setCargo(self, peeps):
        self.cargo = cargo

    def displayData(self):
        print("Ship name:", self.name)
        print(f"Ship cargo capacity: {self.cargo} tons")


        


