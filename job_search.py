# Job search will find the specified jobs I want and put them into the search bar of Indeed.com, 
# After scanning through different html code, it will Identify the Job Position, and Company
# Then will be sent to the Word.py so that my Cover Letter can be modified according to 
# Job position and company

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Search:
    def __init__(self, url, position, where, email, salary = None) -> None:
        self.url = url
        self.position = position
        self.salary = salary 
        self.where = where
        self.email = email
        #with open('Password.txt') as f:
         #   self.password = f.readlines()[0]

    def search(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(self.url)
    
    def SignIn(self):
        pass
