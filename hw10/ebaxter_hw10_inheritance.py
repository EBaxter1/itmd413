'''
File Name: ebaxter_hw10_inheritance.py
Made by: Erin Baxter
This program will have the classes Employee and ProductionWorker and their attributes 
'''

class Employee():
    def __init__(self, name, eNumber):
        self.name = name
        self.eNumber = eNumber

    def displayData(self):
        print(self.name)
        print(self.eNumber)

class ProductionWorker(Employee):

    def __init__(self, name, eNumber, shift, rate):
        self.shift = shift
        self.rate = rate

        Employee__init___(self, name, eNumber)


    def getShift(self):
        return self.shift

    def getRate(self):
        return self.rate

    def setShift(self):
        self.shift = shift

    def setRate(self):
        self.rate = rate

    def setName(self):
        self.name = name

    def setNumber(self):
        self.eNumber = eNumber

    