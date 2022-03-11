import sys
sys.path.insert(1, 'app/model/')
from tax_model import TaxModel

class MalaysianIncomeTax:
    class Tax:
        def __init__(self, monthlySalary, kwspContribution):
            self.contribution = ['7', '9', '11', '12', '13']
            self.kwspContribution = kwspContribution
            self.monthlySalary = monthlySalary
        
        def getSocsoRate(self):
            if self.monthlySalary <= 1000: return TaxModel(employee=16.65, employer=4.75).toJson()
            if self.monthlySalary <= 1100: return TaxModel(employee=18.35, employer=5.25).toJson()
            if self.monthlySalary <= 1200: return TaxModel(employee=20.15, employer=5.75).toJson()
            if self.monthlySalary <= 1300: return TaxModel(employee=21.85, employer=6.25).toJson()
            if self.monthlySalary <= 1400: return TaxModel(employee=23.65, employer=6.75).toJson()
            if self.monthlySalary <= 1500: return TaxModel(employee=25.35, employer=7.25).toJson()
            if self.monthlySalary <= 1600: return TaxModel(employee=27.15, employer=7.75).toJson()
            if self.monthlySalary <= 1700: return TaxModel(employee=28.85, employer=8.25).toJson()
            if self.monthlySalary <= 1800: return TaxModel(employee=30.65, employer=8.75).toJson()
            if self.monthlySalary <= 1900: return TaxModel(employee=32.35, employer=9.25).toJson()
            if self.monthlySalary <= 2000: return TaxModel(employee=34.15, employer=9.75).toJson()
            if self.monthlySalary <= 2100: return TaxModel(employee=37.65, employer=10.25).toJson()
            if self.monthlySalary <= 2200: return TaxModel(employee=37.65, employer=10.75).toJson()
            if self.monthlySalary <= 2300: return TaxModel(employee=39.35, employer=11.25).toJson()
            if self.monthlySalary <= 2400: return TaxModel(employee=41.15, employer=11.75).toJson()
            if self.monthlySalary <= 2500: return TaxModel(employee=42.85, employer=12.25).toJson()
            if self.monthlySalary <= 2600: return TaxModel(employee=44.65, employer=12.75).toJson()
            if self.monthlySalary <= 2700: return TaxModel(employee=46.35, employer=13.25).toJson()
            if self.monthlySalary <= 2800: return TaxModel(employee=48.15, employer=13.75).toJson()
            if self.monthlySalary <= 2900: return TaxModel(employee=49.85, employer=14.25).toJson()
            if self.monthlySalary <= 3000: return TaxModel(employee=51.65, employer=14.75).toJson()
            if self.monthlySalary <= 3100: return TaxModel(employee=53.35, employer=15.25).toJson()
            if self.monthlySalary <= 3200: return TaxModel(employee=55.15, employer=15.75).toJson()
            if self.monthlySalary <= 3300: return TaxModel(employee=56.85, employer=16.25).toJson()
            if self.monthlySalary <= 3400: return TaxModel(employee=58.65, employer=16.75).toJson()
            if self.monthlySalary <= 3500: return TaxModel(employee=60.35, employer=17.25).toJson()
            if self.monthlySalary <= 3600: return TaxModel(employee=62.15, employer=17.75).toJson()
            if self.monthlySalary <= 3700: return TaxModel(employee=63.85, employer=18.75).toJson()
            if self.monthlySalary <= 3800: return TaxModel(employee=65.65, employer=18.75).toJson()
            if self.monthlySalary <= 3900: return TaxModel(employee=67.35, employer=19.25).toJson()
            if self.monthlySalary <= 4000: return TaxModel(employee=69.05, employer=19.75).toJson()
            if self.monthlySalary > 4000: return TaxModel(employee=69.05, employer=19.75).toJson()
            return 0x0
        
        def getTaxableRate(self, chargeable_income):
            annual = chargeable_income * 0xC
            
            def isTaxable():
                if annual > 34000: return True
                return False
            
            if isTaxable():
                if annual <= 5000: return 0x0
                if annual <= 20000: return 0x0
                if annual <= 35000: return 0x96
                if annual <= 35000: return 0x258
                if annual <= 50000: return 0x708
                if annual <= 70000: return 0x1130
                if annual <= 100000: return 0x29CC
                if annual <= 250000: return 0xB66C
                if annual <= 400000: return 0x145FA
                if annual <= 600000: return 0x2094A
                if annual <= 1000000: return 0x39F8A
                if annual > 1000000: return 0x1C
                
            else:
                return 0x0
            
        def kwsp(self):
            def isKwspValid():
                if str(self.kwspContribution) in self.contribution:
                    return True
                return False
            
            if isKwspValid():    
                rate = self.kwspContribution / 0x64
                return self.monthlySalary * rate
            return 0x0
        
        def employerRate(self):
            if self.kwspContribution <= 5000: return 0xD
            if self.kwspContribution >= 5000: return 0xC
            if self.kwspContribution > 5000: return 0xC
            return
        
        def getOutput(self):
            return {
                'GROSS_SALARY': self.monthlySalary,
                'SALARY_AFTER_KWSP_DEDUCTION' : self.monthlySalary - self.kwsp(),
                'EMPLOYEE_KWSP_CONTRIBUTION' : self.kwspContribution,
                'EMPLOYEE_KWSP_VALUE' : self.kwsp(),
                'EMPLOYER_KWSP_CONTRIBUTION' : self.employerRate(),
                'EMPLOYEE_PERKESO_CONTRIBUTION' : self.getSocsoRate()['employee'],
                'EMPLOYER_PERKESO_CONTRIBUTION' : self.getSocsoRate()['employer'],
                'TOTAL_PERKESO_CONTRIBUTION' : self.getSocsoRate()['employer'] + self.getSocsoRate()['employee'],
                'INCOME_TAX' : self.getTaxableRate(chargeable_income=self.monthlySalary)
            } 
