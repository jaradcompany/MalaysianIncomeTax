import json
from interface.mykad import MyKad
from interface.tax import *
from beautifultable import BeautifulTable

class Application:
    def __init__(self, id, name, salary, kwsp):
        self.table = BeautifulTable()
        self.id = id
        self.name = name
        self.salary = salary
        self.kwsp = kwsp
        self.tax = MalaysianIncomeTax().Tax(kwspContribution=self.kwsp, monthlySalary=self.salary)
        self.mykad = MyKad(mykad=self.id)
        
    def run(self):
        
        data =  {
            "NAME" : self.name.upper(),
            "IDENTITY_NUMBER" : self.id,
            "PLACE_OF_BIRTH" : self.mykad.getBirthPlace(),
            "DATA" : self.tax.getOutput(),
        }
        
        self.table.rows.append(["NAME", self.name.upper()])
        self.table.rows.append(["IDENTITY NUMBER", data['IDENTITY_NUMBER']])
        self.table.rows.append(["PLACE OF BIRTH", data['PLACE_OF_BIRTH']])
        self.table.rows.append(["GROSS SALARY", data['DATA']['GROSS_SALARY']])
        self.table.rows.append(["SALARY AFTER KWSP DEDUCTION", data['DATA']['SALARY_AFTER_KWSP_DEDUCTION']])
        self.table.rows.append(["EMPLOYEE KWSP CONTRIBUTION", data['DATA']['EMPLOYEE_KWSP_CONTRIBUTION']])
        self.table.rows.append(["EMPLOYEE KWSP VALUE", data['DATA']['EMPLOYEE_KWSP_VALUE']])
        self.table.rows.append(["EMPLOYER KWSP CONTRIBUTION", data['DATA']['EMPLOYER_KWSP_CONTRIBUTION']])
        self.table.rows.append(["EMPLOYEE PERKESO CONTRIBUTION", data['DATA']['EMPLOYEE_PERKESO_CONTRIBUTION']])
        self.table.rows.append(["EMPLOYER PERKESO CONTRIBUTION", data['DATA']['EMPLOYER_PERKESO_CONTRIBUTION']])
        self.table.rows.append(["TOTAL PERKESO CONTRIBUTION", data['DATA']['TOTAL_PERKESO_CONTRIBUTION']])
        self.table.rows.append(["INCOME TAX", data['DATA']['INCOME_TAX']])
        
        print(self.table)
        
        return json.dumps(data, sort_keys=False, indent=4)
    
if __name__ == "__main__":
    while True:
        mykad = input("What's your MYKAD number? ")
        name = input("What's your name? ")
        salary = input("What's your gross salary? (before any deduction) ")
        kwsp = input("What's the percentage of your KWSP contribution? (7%, 9%, 11%) ")
        app = Application(id=mykad, name=name, salary=float(salary), kwsp=int(kwsp))
        app.run()