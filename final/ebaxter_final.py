'''
File Name: ebaxter_final.py
Made by: Erin Baxter
This program will have the classes PatientAccount, Surgery and Pharmacy
which are accessed and changed in order to calculate a patients hospital bill
'''

class PatientAccount(object):
    def __init___(self, drugCharge, cutCharge, days, rate = 100):
        self.drugCharge = drugCharge
        self.cutCharge = cutCharge
        self.days = days
        self.__rate = rate

    # getters 
    def getDrugCharge(self):
        return self.drugCharge

    def getCutCharge(self):
        return self.cutCharge
    
    def getDays(self):
        return self.days

    def getRate(self, rate):
        return self.__rate

    #setters
    def setDrugCharge(self, drugCharge):
        self.drugCharge = drugCharge

    def setCutCharge(self, cutCharge):
        self.cutCharge = cutCharge

    def setDays(self, days):
        self.days = days

    def setRate(self, rate):
        self.__rate = rate

class Surgery:
    def __init__(self, appendectomy = 2000, c_Section = 3000, cataract = 10000, skinGraft = 5600, prostatectomy = 2500):
        self.__appendectomy = appendectomy
        self.__c_Section = c_Section
        self.__cataract = cataract
        self.__skinGraft = skinGraft
        self.__prostatectomy = prostatectomy

    def getAppend(self, appendectomy):
        return self.__appendectomy

    def getCSection(self, c_Section):
        return self.__c_Section

    def getSGraft(self, skinGraft):
        return self.__skinGraft

    def getCat(self, cataract):
        return self.__cataract

    def getProst(self, prostatectomy):
        return self.__prostatectomy

     def setAppend(self, appendectomy):
        self.__appendectomy = appendectomy

    def setCSection(self, c_Section):
        self.__c_Section = c_Section

    def setSGraft(self, skinGraft):
        self.__skinGraft = skinGraft

    def setCat(self, cataract):
        self.__cataract = cataract

    def setProst(self, prostatectomy):
        self.__prostatectomy = prostatectomy


class Pharmacy:
    def __init__(self, vicodin = 100, simvastatin = 50, lipitor = 120, metformin = 75, amlodipine = 87):
        self.__vicodin = vicodin
        self.__simvastation = simvastation
        self.__lipitor = lipitor
        self.__metfomin = metfomin
        self.__amlodipine = amlodipine

def main():

# call main
main()

print("Thank you for staying. Goodbye!")
