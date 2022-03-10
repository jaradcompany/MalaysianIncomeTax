import json
import requests
from bs4 import BeautifulSoup

class Perkeso:
    def __init__(self):
        self.url = 'https://www.perkeso.gov.my/en/rate-of-contribution.html'
    
    def getResponse(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.text
    
    def getTable(self): 
        soup = BeautifulSoup(self.getResponse(), 'html.parser')
        result = {}
        
        for row in soup.table.find_all('tr'):
            print(row)
        
if __name__ == "__main__":
    perkeso = Perkeso()
    # print(perkeso.getResponse()
    perkeso.getTable()