'''
File Name: ebaxter_final.py
Made by: Erin Baxter
This program will have the classes PatientAccount, Surgery and Pharmacy
which are accessed and changed in order to calculate a patients hospital bill
'''

class PatientAccount(object):
    def __init__(self, drugCharge = 0, cutCharge = 0, days = 10, rate = 100, total = 0):
        self.drugCharge = drugCharge
        self.cutCharge = cutCharge
        self.days = days
        self.__rate = rate
        self.total = total

    # getters 
    def getDrugCharge(self):
        return self.drugCharge

    def getCutCharge(self):
        return self.cutCharge
    
    def getDays(self):
        return self.days

    def getRate(self, rate):
        return self.__rate

    def getTotal(self):
        return (self.__rate * self.days) + self.drugCharge + self.cutCharge

    #setters
    def setDrugCharge(self, drugCharge):
        self.drugCharge = drugCharge

    def setCutCharge(self, cutCharge):
        self.cutCharge = cutCharge

    def setDays(self, days):
        self.days = days

    def setRate(self, rate):
        self.__rate = rate
        
bill = PatientAccount()

class Surgery(PatientAccount):
    def __init__(self, appendectomy = 2000, c_Section = 3000, cataract = 10000, skinGraft = 5600, prostatectomy = 2500):
        self.__appendectomy = appendectomy
        self.__c_Section = c_Section
        self.__cataract = cataract
        self.__skinGraft = skinGraft
        self.__prostatectomy = prostatectomy

    def getAppend(self):
        return self.__appendectomy

    def getCSection(self):
        return self.__c_Section

    def getSGraft(self):
        return self.__skinGraft

    def getCat(self):
        return self.__cataract

    def getProst(self):
        return self.__prostatectomy

    def setAppend(self):
        PatientAccount.cutCharge = self.__appendectomy

    def setCSection(self):
        PatientAccount.cutCharge = self.__c_Section

    def setSGraft(self):
        PatientAccount.cutCharge = self.__skinGraft

    def setCat(self):
        bill.cutCharge = self.__cataract

    def setProst(self):
        PatientAccount.cutCharge = self.__prostatectomy


class Pharmacy(PatientAccount):
    def __init__(self, vicodin = 100, simvastatin = 50, lipitor = 120, metformin = 97, amlodipine = 225):
        self.__vicodin = vicodin
        self.__simvastatin = simvastatin
        self.__lipitor = lipitor
        self.__metformin = metformin
        self.__amlodipine = amlodipine

    def getVicodin(self):
        return self.__vicodin

    def getSimvastatin(self):
        return self.__simvastatin

    def getLipitor(self):
        return self.__lipitor

    def getMetformin(self):
        return self.__metformin

    def getAmlodipines(self):
        return self.__amlodipines

    def setVicodin(self):
        bill.drugCharge = self.__vicodin

    def setSimvastatin(self):
        PatientAccount.drugCharge = self.__simvastatin

    def setLipitor(self):
        PatientAccount.drugCharge = self.__lipitor

    def setMetformin(self):
        PatientAccount.drugCharge = self.__metformin

    def setAmlodipine(self):
        PatientAccount.drugCharge = self.__amlodipine

def main():
    new = Pharmacy()
    print(new.getVicodin())
    new.setVicodin()
    print(bill.getDrugCharge())
    nextNew = Surgery()
    print(nextNew.getCat())
    nextNew.setCat()
    print(bill.getCutCharge())
    print(bill.getTotal())
    

# call main
main()

print("Thank you for staying. Goodbye!")
