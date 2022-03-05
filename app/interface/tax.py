class MalaysianIncomeTax:
    class Tax:
        def __init__(self): pass
        
        def getTaxableRate(self, chargeable_income):
            annual = chargeable_income * 0xC
            
            def isTaxable():
                if annual > 34000:
                    return True
                return False
            
            if isTaxable():
                if annual <= 5000:
                    return 0x0
                
                if annual <= 20000:
                    return 0x1
                
                if annual <= 35000:
                    return 0x3
                
                if annual <= 50000:
                    return 0x8
                
                if annual <= 70000:
                    return 0xE
                
                if annual <= 100000:
                    return 0x15
                
                if annual <= 250000:
                    return 0x18
                
                if annual <= 400000:
                    return 24.5
                
                if annual <= 600000:
                    return 0x19
                
                if annual <= 1000000:
                    return 0x1A
                
                if annual > 1000000:
                    return 0x1C
            else:
                return 0x0
                
                
            
print(MalaysianIncomeTax().Tax().getTaxableRate(2600))
            
                