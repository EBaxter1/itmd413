'''
File Name: ebaxter_hw11_polymorphism.py
Made by: Erin Baxter
This program will have the classes Ship, CruiseShip, CargoShip and their members
'''

# parent class that has name of ship, built year, accessers, mutators and print function
class Ship(object):
    def __init__(self, name, year):
        self.__name = name
        self.__year = year

    def getName(self):
        return self.name

    def getYear(self):
        return self.year

    def setName(self, name):
        self.name = name

    def setYear(self, year):
        self.year = year
        
    # @property
    def displayData(self):
        print("Ship name:", self.__name)
        print("Ship built in:", self.__year)


def CruiseShip(Ship):
    def __init__(self, peeps):
        Ship.__init__(self, name)
        self.peeps = peeps

    def getPeeps(self):
        return self.peeps

    def setPeeps(self, peeps):
        self.peeps = peeps

    # @property
    def displayOData(self):
        print("Ship name:", self.name)
        print("Maximum number of passengers:", self.peeps)


        


