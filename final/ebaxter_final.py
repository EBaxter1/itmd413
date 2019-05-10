'''
File Name: ebaxter_final.py
Made by: Erin Baxter
This program will have the classes PatientAccount, Surgery and Pharmacy
which are accessed and changed in order to calculate a patients hospital bill
'''

#this class holds the charge data for a bill and the rate price 
class PatientAccount(object):
    #constructor
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

#new object of Patient class so other classes can change it variables
bill = PatientAccount()

# this class has multipl surgerys and their cost. The setters of this class change the cutCharge variablein PatientAccount
class Surgery(PatientAccount):
    def __init__(self, appendectomy = 2000, c_Section = 3000, cataract = 10000, skinGraft = 5600, prostatectomy = 2500):
        self.__appendectomy = appendectomy
        self.__c_Section = c_Section
        self.__cataract = cataract
        self.__skinGraft = skinGraft
        self.__prostatectomy = prostatectomy
        
    #getters
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

    #setters, uses bill object to get get PatientAccount variable
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

#this class has different medications and their cost. The setter methods change the drugCharger variable in PatientAccount
class Pharmacy(PatientAccount):
    def __init__(self, vicodin = 100, simvastatin = 50, lipitor = 120, metformin = 97, amlodipine = 225):
        self.__vicodin = vicodin
        self.__simvastatin = simvastatin
        self.__lipitor = lipitor
        self.__metformin = metformin
        self.__amlodipine = amlodipine

    #getters
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

    #setters, use bill object to get get PatientAccount variable
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

#this main method makes a menu for the different options and then calls the right classes to set and get data
def main():
    #objects of Surgery and Pharmacy classes 
    newCut = Surgery()
    newDrug = Pharmacy()

    #say hi
    print("Hello! Welcome to the Patient Check out and Bill Calculator final edition!\n")

    #while loop that runs for ever if there is errors 
    while 1 == 1:#makes while always true
        try:
            # get number of days 
            days = int(input("How many days has the patient been in the hospital?: "))
            bill.setDays(days) #set number of stays 
        except ValueError:
            print("Error! Please only use whole numbers!")
            continue #make loop keep going 
        try:
            #get surgery option choice 
            cut = int(input(f'''\nWhich surgery did they have?\n1. Appendectomy(enter 1)\n2. A Cesarean Section(enter 2)\n3. Cataract Surgery(enter 3)\n4. A Skin Graft(enter 4)\n5. A Prostatectomy(enter 5)\nEnter option: '''))
            #if statements to call setter functions of surgery class
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
                continue # keep loop running if error 

            #get medication option choice
            drug = int(input(f'''\nWhich medication did they get prescribed?\n1. Vicodin(enter 1)\n2. Simvastatin(enter 2)\n3. Lipitor(enter 3)\n4. Metformin(enter 4)\n5. Amlodipine(enter 5)\nEnter option: '''))
            #if statements to call setter functions of pharmacy class, they also end the while loop since bill is down
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
                continue # keep loop running if error
            
        except ValueError:
            print("Error! Put choose an option betwen numbers 1 and 5!")
            continue # keep loop running if error
        
    # display pretty bill with formatting by calling PatientAccount classs getetrs
    print("\nChecking out Patient and Generating Bill....\n| Patient Bill |")
    print(f"| Days in Hospital: {bill.getDays()}")
    print("| Surgery Cost: " + "${:,.2f}".format(bill.getCutCharge()))
    print("| Medication Cost: " + "${:,.2f}".format(bill.getDrugCharge()))
    print("|--------------------------------------------")
    print("| Patient total hospital bill is: " + "${:,.2f}".format(bill.getTotal()))         
    

# call main
main()

#say bye
print("\nGoodbye!")
