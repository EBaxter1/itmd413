'''
File Name: ebaxter_hw10_inheritance.py
Made by: Erin Baxter
This program will have the classes Employee and ProductionWorker and their attributes 
'''

#parent class that has employee name and number, can that print info
class Employee(object):
    #constructor for name and number
    def __init__(self, name, eNumber):
        self.name = name
        self.eNumber = eNumber

    # method to display information 
    def displayData(self):
        print("Employee name:", self.name)
        print("Employee Number:", self.eNumber)

# child class that takes name and number from parent and also makes shift and rate 
class ProductionWorker(Employee):
    # constructor for name, number, shift and rate for a worker
    def __init__(self, name, eNumber, shift, rate):
        # constructor to get __init__ from parent class
        super(ProductionWorker, self).__init__(name, eNumber)
        self.shift = shift
        self.rate = rate
        
    # method to display information 
    def displayOtherData(self):
        print("Worker shift:", self.shift)
        print("Hourly pay rate:", "${:.2f}".format(self.rate))

    # method to get current shirt for worker
    def getShift(self):
        return self.shift

    # method to get current pay rate for worker 
    def getRate(self):
        return self.rate
    
    # method to set new shift for worker 
    def setShift(self, shift):
        self.shift = shift

    # method to set new pay rate for worker
    def setRate(self, rate):
        self.rate = rate

    # method to set new name of worker 
    def setName(self, name):
        self.name = name

    # method to set new number of worker
    def setNumber(self, eNumber):
        self.eNumber = eNumber

    
