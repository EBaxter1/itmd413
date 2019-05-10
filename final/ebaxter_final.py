'''
File Name: ebaxter_final.py
Made by: Erin Baxter
This program will have the classes PatientAccount, Surgery and Pharmacy
which are accessed and changed in order to calculate a patients hospital bill
'''

class PatientAccount(object):
    def __init__(self, drugCharge = 0, cutCharge = 0, days = 0, rate = 100, total = 0):
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
        bill.cutCharge = self.__appendectomy

    def setCSection(self):
        bill.cutCharge = self.__c_Section

    def setSGraft(self):
        bill.cutCharge = self.__skinGraft

    def setCat(self):
        bill.cutCharge = self.__cataract

    def setProst(self):
        bill.cutCharge = self.__prostatectomy


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
        bill.drugCharge = self.__simvastatin

    def setLipitor(self):
        bill.drugCharge = self.__lipitor

    def setMetformin(self):
        bill.drugCharge = self.__metformin

    def setAmlodipine(self):
        bill.drugCharge = self.__amlodipine

def main():
    newCut = Surgery()
    newDrug = Pharmacy()
    
    print("Hello! Welcome to the Patient Bill Calculator final edition!\n")
    while 1 == 1:
        try:
            days = int(input("How many days has the patient been in the hospital?: "))
            bill.setDays(days)
        except ValueError:
            print("Error! Please only use whole numbers!")
            continue
        try:
            cut = int(input(f'''\nWhich surgery did they have?\n1. Appendectomy(enter 1)\n2. A Cesarean Section(enter 2)\n3. Cataract Surgery(enter 3)\n4. A Skin Graft(enter 4)\n5. A Prostatectomy(enter 5)\nEnter option: '''))
            if cut == 1:
                newCut.setAppend()
            elif cut == 2:
                newCut.setCSection()
            elif cut == 3:
                newCut.setCat()
            elif cut == 4:
                newCut.setSGraft()
            elif cut == 5:
                newCut.setProst()
            else:
                print("Please choose an option between 1 and 5!")
                continue

            drug = int(input(f'''\nWhich medicatiuon did they get prescribed?\n1. Vicodin(enter 1)\n2. Simvastatin(enter 2)\n3. Lipitor(enter 3)\n4. Metformin(enter 4)\n5. Amlodipine(enter 5)\nEnter option: '''))
            if drug == 1:
                newDrug.setVicodin()
                break
            elif drug == 2:
                newDrug.setSimvastatin()
                break
            elif drug == 3:
                newDrug.setLipitor()
                break
            elif drug == 4:
                newDrug.setMetformin()
                break
            elif drug == 5:
                newDrug.setAmlodipine()
                break
            else:
                print("Please choose an option between 1 and 5!")
                continue
            
        except ValueError:
            print("Error! Put choose an option betwen numbers 1 and 5!")
            continue
        
    print("\nPatient total hospital bill is: " + "${:,.2f}".format(bill.getTotal()))
        
                
    

# call main
main()

print("\nGoodbye!")
