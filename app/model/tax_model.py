class TaxModel:
    def __init__(self, employee, employer):
        self.employer = employer
        self.employee = employee
        
    def toJson(self):
        return { 'employee' : self.employee, 'employer' : self.employer }